# The Research-Note Graduation Queue — `revisit_after:` + `ingest:` on research notes, ripeness as a self-draining lint queue (`frontmatter@4` proposal)

_Filed from the `vlt-core` vault out of a **2026-07-11 CIS problem-solving run** (`_agent/artifacts/problem-solution-2026-07-11.md`, vault commit `f0c3b45`). This is the **explicit complement** to the shipped `review_after` freshness work (`inbox/archive/…-091006-review-after-freshness-key.md` → `frontmatter@3`, build-16). That work added a **condition** axis to the *wiki* (is this page still true?) and its Is/Is-Not table **deliberately scoped research notes OUT** ("*datetime-prefixed, written-once — the filename is the accession date*"). This filing fills exactly that hole, for the **research zone**, against a **different question**: not "is it still true?" but **"is this deferred research note now ripe to graduate into the wiki?"** Where `frontmatter@3` shipped the accession *register*, this ships the accession *backlog*._

**Filing status.** **Design-stage proposal, filed at the owner's request** so the next build can pick it up. **Nothing is built in `vlt-core` yet** — no local overlay, no `research.base`, no lint change. The schema decision is settled (two optional research-note keys, a computed orphan projection, a lint-emitted queue); local prototype + first-drain-cycle evidence would follow if the maintainer wants field data before shipping, but the owner's intent is to build this at the module source directly.

## Problem statement + evidence

- **Write-time-only ripeness gate; no re-evaluation loop.** A research note's fitness for wiki ingestion is judged once, in the session that creates it. If deferred, it enters `_agent/research/` and loses all inbound gravity: unlinked → undiscoverable → never reconsidered. Discoverability is defined **solely** as "linked as a source in a wiki page," so an un-ingested note is invisible the moment its creating session ends.
- **The deferral is legitimate — that's what makes this hard.** The Researcher routinely returns a note that is real but not yet wiki-worthy (too thin for its own page/category; no durable home yet). The fix must *not* auto-ingest; it must make deferral **safe and reversible** so the note resurfaces when ripe.
- **Ripeness is accretion-triggered, not calendar-triggered.** The owner's stated condition — *"ready when more information becomes available and the content is now durable"* — fires when *sibling material accretes around the note's topic*, which a write-time date cannot predict. A pure `revisit_after` (the owner's first instinct, and the obvious mirror of `review_after`) is the cheap 80% but **misses the actual trigger**.
- **Five-Whys root cause:** the vault has an accession **pipeline** (research → maybe ingest → done) but no accession **backlog** — no first-class state for *deferred-pending-re-evaluation*, and no loop that re-scores that state as the zone evolves. This is the precise mirror of `frontmatter@3`'s root cause ("catalog schema without an accession/condition axis"): that added a *condition* axis to the wiki; this adds a **candidacy** axis to the research zone.
- **Scale/evidence:** ~88 research notes in `vlt-core` today across ~10 heterogeneous domains (NFL, dog training, protein science, cooking, homelab, reading logs). Many are **terminally standalone** (taste interviews, reading-progress updates) and must never nag — the naive "list all orphans" surfaces dozens of these and trains the reader to ignore the queue.

## The decision and its rationale

The obvious proposal — one `revisit_after` date, a straight `review_after` twin — was pressure-tested and found **necessary but insufficient**. The population splits three ways, and **two of the three states are already mechanically computable**, which shrinks the real problem dramatically:

1. **"Ingested" is free to detect — no key.** A reverse index over every wiki page's `sources:` yields the **orphan set** (research notes cited by no wiki page). This is the research-zone twin of the `review_after` filing's key insight that the ledger needed no schema — the *same pure-projection move*, pointed the other way. Discoverability becomes visible at zero schema cost.
2. **"Terminal/standalone" needs one cheap opt-out key** (`ingest: exempt`). Absence = graduation candidate. This is what makes the queue survive an 88-note heterogeneous zone: the terminal notes opt out once and stay silent.
3. **Only "pending" needs scoring**, and it's scored by a **union of three signals**, not the calendar alone:
   - **Time** — `revisit_after: YYYY-MM-DD`, the deliberate deferral date (the owner's original instinct; kept, because it's the cheap rail for genuinely time-bound notes and doubles as the **snooze**).
   - **Topic cluster** — an orphan whose `topic:` tag is now shared by ≥K notes (K=3 to start) with no wiki home → the accretion signal that actually models "more information arrived."
   - **Linkage** — an orphan a *newer* note cites in `sources:`/`[[…]]` → the strongest per-note signal (a later write literally built on it).
4. **The mechanism is self-draining.** Ingesting a ripe note back-links it out of the orphan set — the queue converges instead of accumulating, with **no separate "mark done" write**. This is the load-bearing property; it's why a *pull queue* beats every push/auto variant.

**Semantics copied verbatim from `review_after`** (one vocabulary, not two): store the **resolved date, never a duration**; **absence means something** (`revisit_after` absent = unscheduled; `ingest` absent = candidate); **lint FINDS, the human DECIDES** (the drain resolves each note to exactly one of three outcomes — **ingest now / defer (set-or-bump `revisit_after`) / exempt** — mirroring the wiki review queue's three-outcome discipline).

**Rejected alternatives** (documented so they aren't re-litigated):

- **Auto-ingest ripe notes** — the most instructive rejection: it *destroys the legitimacy of deferral*, which is the research zone's whole reason to exist. If deferral auto-resolves into the wiki, the Researcher can't stage half-formed knowledge without polluting the catalog, and the Librarian loses the single-writer gate. Invisibility is the disease; a *pull queue*, not *auto-push*, is the cure.
- **`revisit_after` only** (the naive twin) — misses accretion + linkage, i.e. the actual ripeness trigger.
- **Orphan-list only, no scoring** — an 88-note firehose over a heterogeneous zone; trains the reader to ignore it (alarm fatigue).
- **Overload `status:`** (`status: filed`/`archived` for terminal) — re-conflates *research-progress* with *wiki-destiny* on one word; the exact axis-mixing the `review_after` filing warned against (trust ≠ freshness → here, research-status ≠ graduation-candidacy). Keep candidacy its own keys.
- **Sidecar backlog file** (`_agent/research/_backlog.md`) — reintroduces the dual-write failure mode; the computed queue is strictly better.
- **Embedding/semantic clustering** — over-engineered; violates the plain-markdown ethos; `topic:` tags + linkage get ~90%.

**v2 candidates parked deliberately** (do **not** ship in `frontmatter@4`): `revisit_when: "<free-text condition>"` ("revisit when the protein RCTs land") — a ripeness-condition hint, the research-side analogue of the parked `review_note:`; and fuzzy/semantic topic-matching for the cluster signal if exact `topic:` tags prove too sparse.

## Exact module-side changes to ship

1. **`skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md`** — bump `version: 3 → 4`. In *Research notes (`{research}`)*, add **two optional keys** to the schema block plus a semantics paragraph each:
   - `revisit_after: YYYY-MM-DD` — a deliberate deferral/revisit date, set at write time when the note is knowingly deferred pending more material. **A resolved date, never a duration.** **Absence = unscheduled** (the note still rides the accretion + linkage signals). Doubles as the **snooze** — bump the date to dismiss "not now." Reuse the `review_after` definition wording; state explicitly that research notes remain **written-once** (this is a deferral-*intent* field set at write, not a `last_updated`-style mutable edit field — a correction is still a new note).
   - `ingest: exempt` — terminal opt-out; the note will never graduate (personal/one-off: taste interviews, reading-progress logs). **Absence = graduation candidate.** Set by the Librarian when triaging the queue. (Single legal value `exempt` for now; a future `ingest: pending`/`ingest: ingested` axis is unnecessary — those states are *computed*, not stored.)
   - Note that research notes now carry two `ingest`/`revisit` intent keys but **still no `last_updated`** — the written-once rule is unchanged.
2. **`skills/vlt-lint/SKILL.md`** — bump `depends_on` to `frontmatter@4`. Add an **orphan projection** (reverse-index all wiki `sources:` → research notes cited nowhere) and **three findings over the orphan set, minus `ingest: exempt`**, emitted as a **Graduation Queue** section under `flag_for_human` (never auto-ingest — graduation is Librarian judgment):
   - `revisit_due` — `revisit_after` past **and** still orphaned.
   - `cluster_ripe` — orphan's `topic:` now spans ≥K notes with no wiki page for that topic (ship K=3 as a documented, tunable default).
   - `linkage_ripe` — a newer note cites/links this orphan.
3. **`skills/vlt-setup/assets/workflows/vlt-lint-full.js`** — add the orphan/graduation findings to the per-page (and cross-page reduction) schema so the `--full` fan-out reports the queue. The cluster + linkage signals are **cross-page** — the reducer, not the per-page agent, computes topic co-occurrence and reverse-links; spec this in the workflow so a fan-out worker isn't asked to see the whole zone. (Per the convention-coherence rule, `vlt-lint`'s ack covers this asset.)
4. **`skills/vlt-research/SKILL.md`** — bump `depends_on` to `frontmatter@4`; add a write-step rule + verify checkbox: "if the note is being **deliberately deferred** (real but not yet wiki-worthy), set `revisit_after:` to a resolved date; otherwise omit it." This is where the deferral *intent* is captured at the source.
5. **`skills/vlt-ingest/SKILL.md`** — bump `depends_on` to `frontmatter@4`; add the **ingest-time probe** (the sharp end): when filing a source, reverse-check the research zone for non-exempt orphans sharing the new source's `topic:` and surface them as candidate sources / graduation prompts ("3 orphaned research notes touch this topic — pull them in / graduate one?"). This delivers ripeness *at the moment of maximum relevance*, ahead of the periodic lint sweep.
6. **`skills/vlt-dispatch/SKILL.md`** (optional surfacing) — the `ledger` (open-items board) mode gains a Graduation-Queue line so ripe orphans show on the existing cross-partner board, not only in a lint run.
7. **The `research.base` question** — mirror the `review_after` filing's owner ruling: **ship the schema + skill lines, keep Bases vault-local as documented reference** (an "Un-ingested" view — orphans sorted `created` ASC — plus a "Graduation Queue" view). If the module later ships bases, the packaging shape from that filing's change 5 stands (`skills/vlt-setup/assets/bases/`, a `bases:` row in `module.yaml`'s `vault_structure`, create-if-absent provisioning).

## Upgrade / migration path for existing installs

- **No backfill required for the keys** — absence = candidate (`ingest`) and absence = unscheduled (`revisit_after`) *are* the migration path; legacy research notes degrade gracefully.
- **One-time exempt pass, optional, capped.** Ship guidance (not a migration step) for a single Librarian pass to mark the obviously-terminal orphans `ingest: exempt` so the first queue isn't noisy — cap it, scope it to clearly-personal categories, don't clobber judgment.
- **`depends_on: frontmatter@4` bumps** ride the normal skill refresh; `vlt-lint`'s convention-coherence check confirms the handshake post-upgrade.
- **Overlay-subsumption** — if a vault prototypes these keys locally first (via `frontmatter.overlay.md`), the same overlay-retirement gap flagged in the `review_after` filing (latent bug 2 there) applies on upgrade; the subsumption pass proposed there covers this filing too. No new upgrade machinery needed beyond what that filing already requested.

## Latent bugs / drift surfaced

1. **Discoverability was under-specified as "wiki links only."** The reverse-index makes orphans visible with no link at all — worth stating in the operating contract that the research zone has a *computed* discoverability path (the orphan projection), not only the inbound-link path. Otherwise the next partner re-derives "unlinked = lost."
2. **Cross-page signals in a fan-out lint.** `cluster_ripe`/`linkage_ripe` cannot be computed by a per-page `vlt-lint-full` worker (no worker sees the whole zone). If the workflow schema isn't explicit that these are **reducer-stage** findings, a future edit could wrongly push them per-page and silently under-report. Spec it now (change 3).
3. **`status:` overload temptation.** The shipped research-note schema already carries `status: draft | in-progress | complete`; a maintainer may be tempted to add a `status: graduated`/`archived` value instead of the dedicated `ingest:` key. Flag explicitly: graduation-candidacy is orthogonal to research-progress — keep them separate keys (same lesson as trust ≠ freshness in `frontmatter@3`).

## Open design questions to decide module-wide

1. **K (cluster threshold) as shipped default.** Start K=3? It wants field calibration — too low spams `cluster_ripe`, too high stays silent. Ship as a documented, tunable value (in the convention prose, not code) and let vaults tune. `vlt-core` will supply first evidence if prototyped locally.
2. **`topic:` tag consistency is assumed for clustering.** The `review_after` filing had the same "verify Bases date syntax" caveat; the analogue here is "are `topic:` tags consistent enough to cluster on?" In `vlt-core` they're mixed (single-string vs list; broad vs narrow). If too sparse, ship `revisit_after` + `linkage_ripe` first and defer `cluster_ripe` to a point-release. **Recommend a Slice-0 zone sample before committing the cluster signal.**
3. **Ingest-probe scope.** Should the probe (change 5) match on any shared `topic:` tag, or only the most-specific one? Broad match = more surfacing + more noise. Lean most-specific first, loosen on evidence.
4. **Where does an aging queue escalate?** Same question the `review_after` filing raised for the review queue: if a `cluster_ripe` note sits unworked for two drain cycles, is that a `vlt-lint` promotion or an enforcement-kit tripwire? Lean tripwire (lint finds, it shouldn't also nag) — and unify the answer with the review-queue escalation so the module has one policy.
5. **Does `review_after` (wiki) and `revisit_after` (research) being near-homophones invite confusion?** They're deliberately parallel (both resolved dates, both absence-means-something, both lint-flagged). Considered `graduate_after`/`ingest_after` to disambiguate; kept `revisit_after` for vocabulary continuity with `review_after`. Maintainer's call — but pick one and document the pair together.

## Provenance

- Vault: `vlt-core`. CIS problem-solving session 2026-07-11 — full analysis (Is/Is-Not, Five-Whys, force-field, morphological/SCAMPER solution generation, decision matrix, slices, metrics) at `_agent/artifacts/problem-solution-2026-07-11.md`, vault commit `f0c3b45`.
- Direct predecessor / sibling: the shipped `review_after` work — `inbox/archive/2026-07-06-091006-review-after-freshness-key.md` and its pressure-test `_agent/artifacts/problem-solution-2026-07-06-ingestion-ledger.md` (→ `frontmatter@3`, build-16). That session's Is/Is-Not explicitly deferred the research zone; this filing is the deferred half.
- Filed at design stage on 2026-07-11 at the owner's request, ahead of any local prototype, so the next build can sequence it.
