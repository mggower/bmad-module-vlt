---
title: 'Build #A4-1 — `linkage_ripe` polarity (the check fires the calibration''s absorption signals inverted, and the next ordinary lint on the primary vault surfaces ~97 of 98 notes)'
status: |
  BUILT 2026-07-25 — F1–F6 all landed; verification 1–9 all pass; not released (owner call).

  Shipped surface touched (3 files, 20 insertions / 6 deletions):
  - skills/vlt-lint/SKILL.md — F1 (:43 inputs), F2 (:82 boundary clause), F3 (:88 the projection),
    F4 (:151 report slot; key unchanged)
  - .../governance/_meta/conventions/frontmatter.md — F5 (:138 pointer de-restated; stays version: 4,
    five consumers, NO bump, no consumer walk)
  - .../governance/_meta/vault-operating-contract.md — F6 (two A3-22 prose items after the :224 role
    boundary; last_updated 2026-07-17 → 2026-07-25; not handshaked, no ack obligation)

  DERIVE-VS-STORE CLOSURE (disposition 1). Recorded as required: resolved DERIVE. No graduation-state
  key, no frontmatter@5, no consumer walk. Derive-first holds unbent; the deferred cross-filing ruling
  closes without an exception. The verification-by-residue clause ships as a BOUNDARY on derive-first
  at vlt-lint's candidacy pass, its governance home deferred to A4-2 (which must not create a second).

  OWNER CALLS AT BUILD TIME (2026-07-25):
  - Release: NO. Hold to arc end — no version bump, no tag; the release rides whichever build is last
    in Arc 4. (The brief named a patch-on-A4-1 as plausible; owner declined it.)
  - sources_vs_prose_mismatches (brief Out of scope, "owner to decide"): FILED, not fixed. New filing
    inbox/2026-07-25-193000-report-slot-with-no-check.md — enters the loop for Arc-4 capture; states
    the honest-reporting half is A4-2's general rule (no bespoke report-line fix) and the
    missing-check half is a separate wiki-side question.

  DELIBERATE DEVIATIONS FROM THE BRIEF (2):
  1. F2 placement is a paragraph, not an in-sentence append. The brief said "append one short clause
     to this header paragraph", but that paragraph ends in a colon introducing the two findings —
     appending after a colon would have orphaned the bullets. Landed instead as: header sentence
     terminated with a period (posture text preserved verbatim), then the boundary clause as its own
     indented paragraph, then a one-line "The two findings:" re-introduction before the bullets.
     Wording of the clause matches the brief's stated intent in the file's voice. The reader still
     meets the clause BEFORE the rule at :88, which was the placement's purpose.
  2. The single-home grep returns 5 shipped hits, not the brief's predicted 4. Both extra-vs-predicted
     hits are inside the SAME rewritten bullet (:88 the rule, :93 the historical-name note); the
     mechanic is stated once. The other three are :43 (inputs), :151 (slot label), frontmatter.md:138
     (pointer) — exactly as briefed. No second home exists.

  VERIFICATION (all 9, run at rest before commit):
  1. Re-derivation vs the SPIKE-2 baseline — PASS. All 8 calibration-polarity notes classify RIPE
     under the rewritten :88 as written (acotar-series, empyrean-series, llm-wiki-v2,
     taste-interview, reading-queue-update, fiddleheads, world-cup group-stage, black-opening): none
     carries a cited, inbound-wikilink, or shared-source leg — their only shipped leg was `topic`,
     which F3 drops. Absorbed sample of 18 spanning all three leg patterns classifies ABSORBED ⇒
     EXCLUDED: `shared` only — macdonald-coaching-tree, cost-of-staying, war-room-mock-draft-2,
     kyle-shanahan-tree, nfl-draft-big-board, dual-portfolio, survivor-fandom, severe-calf-strain,
     youtube-to-markdown; `wl,shared` — para-method-categories, transformer-self-attention,
     renewable-energy, survivor-overview, hidden-immunity-idol, social-bookmarks; `topic,wl,shared` —
     spaced-repetition, kettl-jpn-nyc, penny-breed-results. Generalizes: every one of the 90
     absorbed=True notes carries wl and/or shared, so all 90 exclude on a non-topic leg alone.
     RESULT: 8 of 98 ripe (~8%), not ~97. The rule applied unambiguously by hand — no tightening
     needed. Honest asymmetry noted in the brief holds and is the intended agreement.
     Direction check on the widened cited leg: A4-1's leg 1 (frontmatter `sources:` OR prose
     `## Sources`) is BROADER than the baseline artifact's computation, and a broader absorption leg
     can only exclude more — so ≤8, never >8. The fix cannot under-exclude relative to the baseline.
  2. Drain-tracking spot check — PASS. The four since-graduated audit items all classify absorbed ⇒
     excluded (ashwagandha: `wl`; l-theanine-vs-ashwagandha: `topic,shared`; wispr-flow: `topic,wl`;
     youtube-to-markdown: `shared`; kettl cluster: all `topic,shared`/`topic,wl,shared`). The one
     never drained — the world-cup group-stage note — classifies RIPE (`topic` only, absorbed=False).
     Polarity defect demonstrated, not argued.
  3. Single-home grep — PASS (see deviation 2). Mechanic stated once at :88.
  4. Stale-description grep — PASS. Zero hits describing linkage_ripe. The three surviving corpus
     hits are unrelated and correct: vlt-extract:62 (slug/topic proposal), vlt-ingest:99
     (near-duplicate concept compare), wiki-consolidation.md:129 (merge signal phrasing). The tier-1
     `topic:`-is-a-list check and its string→list auto-fix are untouched (disposition 5).
  5. Preserved-posture grep — PASS. `never auto-promoted` + flag_for_human survive at :82; the
     `revisit_due` bullet is BYTE-UNCHANGED (absent from `git diff -U0`), confirmed as A4-2's site.
  6. Handshake bipartite re-check — PASS, unchanged as expected. frontmatter stays @4 with five
     consumers; every consumer's depends_on still pins frontmatter@4 (package-lint Group E).
  7. Packaging lint (mid-arc) — PASS. `uv run tools/package-lint.py` → "A/B/C/E PASS, D SKIPPED —
     vlt 0.7.0". Group D correctly skipped (no --expect-version; not a release build).
  8. Scrub — PASS. Zero hits for vlt-core / vlt-sayari / /Vaults/ / owner name / the audit path / the
     baseline artifact across all three changed shipped files. Note filenames appear in this brief's
     status only (skills/reports/ is gitignored).
  9. Housekeeping — PASS. No .decision-log.md produced anywhere under skills/ (none created: the
     brief is the canonical build record, and the repo standing rule forbids them in the tree). One
     commit for the build.

  ACCEPTANCE: deferred to the Arc-4 roadmap ledger, unchanged (six clauses). Not attempted at build
  time. Rides the next owner-run vlt-upgrade + full lint on the primary vault.
module_code: 'vlt'
created: '2026-07-25'
derives_from:
  - 'inbox/2026-07-25-162416-linkage-ripe-cannot-see-graduation.md (A3-23 — the graded acceptance failure; root cause re-established by SPIKE-1 as a polarity inversion, not missing graduation state)'
  - 'inbox/2026-07-25-132141-partner-consult-synchronous-channel.md (A3-22 — the two zero-machinery prose items ONLY: the contract prohibition + read-and-cite as documented default. The consult mechanism itself is A4-5.)'
roadmap: 'skills/reports/inbox-evolution-arc4-roadmap.md'
rulings: 'Arc-3 roadmap §Ideation rulings — A3-18..A3-23 (2026-07-25), the binding home: A4-1 = A3-23, ships first (smallest + highest latent severity); carries the two A3-22 prose items as the earliest-shipping build; derive-vs-store deferred to this brief and resolved toward DERIVE by SPIKE-2; verification-by-residue stated as a boundary clause on derive-first, not a new invariant; the silent-zero class gets ONE general rule written by A4-2 — no site briefs a bespoke report-line fix.'
risk: 'low-moderate — no schema key, no convention `version:` bump, no consumer walk (SPIKE-2: derive-first holds unbent). The moderate half is behavioral: this rewrites a live check''s output polarity on every install, and the check is prose-specified and agent-run, so the fix is verified by re-derivation against a preserved baseline rather than by a test.'
---

# Build #A4-1 — `linkage_ripe` polarity

## Intent

`vlt-lint`'s `linkage_ripe` graduation-candidacy projection fires the field calibration's
**absorption** signals as **ripeness** signals. The calibration (A3-8 vlt-core, A3-9 vlt-sayari)
used `frontmatter citation ∪ body wikilinks ∪ shared-source overlap` as evidence a research note
was *already absorbed into the wiki* ⇒ **exclude it**; ripe meant **no** linkage. Shipped
`vlt-lint:83` treats a union hit as ripeness, so it surfaces precisely the set the calibration
excluded as false positives. Two further drifts ride along: `topic:` overlap was substituted for
the calibration's **frontmatter-citation** leg, and the name was borrowed from A3-7's
different `linkage_ripe` ("a newer note cites/links this orphan").

This build restores the calibration's polarity, restores the citation leg (in both the surfaces
the field audit found it on — frontmatter `sources:` **and** the page's prose `## Sources`
section), drops the substituted `topic:` leg, and states the boundary clause on derive-first that
names the general hazard. It also carries the two A3-22 zero-machinery prose items, which ride
the earliest-shipping build by ruling.

**Why now.** The graded failure is **latent and worse than measured**. The 07-25 vlt-core lint
reported 41 hits / 0 real, but exactly 41 of the then-96 notes carried a list-form `topic:` at
candidacy time — the same sweep auto-fixed 55 scalar `topic:` → YAML lists (build-20's own F1
fix), silently damping the projection. All 98 notes are list-form now, so the **next ordinary
lint run surfaces ~97 of 98 (≥93% FP)**. Every day unfixed is a day the primary vault's lint
output is noise on that axis, and the fix that caused the amplification was the correct fix.

**All rejected alternatives in the parent filings are settled — do not re-litigate.** In
particular: A3-23's own diagnosis ("missing graduation state ⇒ store a `graduated:` key ⇒
`frontmatter@5` + full consumer walk") is **superseded** by SPIKE-1/SPIKE-2 and is not the build.
Do not add a graduation-state key. Do not open `frontmatter@5`.

**Sources of truth for this build** (read before touching source):
- Binding rulings: Arc-3 roadmap `## Ideation rulings — A3-18..A3-23 (owner-steered, 2026-07-25)`
  — including both **SPIKE CLOSED** records. (Moves to `skills/reports/archive/` at Arc-3
  closeout; read it there.)
- Grounded capture: Arc-3 roadmap `### A3-23` and `### A3-22`.
- Baseline artifact: `skills/reports/spike2-projection-baseline-2026-07-25.md` — both polarities,
  full enumeration, 98 notes × 131 pages.
- Field calibration source: `{field-vault}/_agent/artifacts/research-wiki-audit-2026-07-11.md`
  `:19`, `:69`, `:71` (a live-vault read; not module source, not shipped).

## Grounding at brief time

Re-ground run 2026-07-25 against current source (v0.7.0 @ `dbcf018`).

- **Grounding corrections: 0.** Every `file:line` the A3-23 capture cited still HOLDS exactly —
  `vlt-lint:43`, `:82`, `:83`; `frontmatter.md:136`, `:138`; `vlt-ingest:73`, `:107-124`,
  `:121-122`, `:131`. Nothing shipped between capture and brief. (The capture's *premises* about
  root cause were already superseded in place by the two spike records; no new superseding note
  is owed to the roadmap.)
- **Grounding additions: 4** — sites the capture did not name that must move with the fix:
  `vlt-lint:43` (the pass's declared inputs), `vlt-lint:141` (the report-key slot description),
  `frontmatter.md:138` (a pointer that restates the mechanic it points at), and the operating
  contract's `## Sessions, sittings, and hand-offs` (the home chosen for the A3-22 prose).

## Brief-time dispositions

1. **Derive-vs-store → DERIVE. Stated explicitly, not arrived at by default.** (Ideation left
   this open with a live home: *"The brief states the call explicitly; it may not arrive at
   derive-or-store by default."*) SPIKE-2 §6: absorption is computable from disk today, surfaces
   8 of 98, and **tracks the drain** — of the audit's five hand-verified ripe items, the four
   since graduated now read absorbed ⇒ correctly excluded, and the one never drained still
   surfaces. No graduation-state key is needed; **derive-first holds unbent**, and the deferred
   cross-filing ruling closes without an exception. Record that closure in the build's `status:`.

2. **The verification-by-residue boundary clause is STATED in this build, at the site where the
   hazard bit; its governance home is deferred to A4-2.** *(Owner-ruled 2026-07-25 at brief
   time.)* Ideation ruled the clause is stated as a boundary on derive-first rather than a new
   standalone invariant, but named no home — and grounding finds **no shipped derive-first
   doctrine file**: the phrase appears once, at `vlt-upgrade:44`, about the upgrade preserve set.
   The two candidate homes both cost more than the clause: `frontmatter.md` §Enforcement
   declaration would make it a **rule change** (bump 4→5 + re-ack five consumers), contradicting
   this build's ruled shape; a new convention is out of proportion. So A4-1 writes it generally
   worded at `vlt-lint`'s candidacy pass (F2), where the next reader of derive-first meets it.
   **A4-2 already must choose a governance home for the general honest-reporting rule; both rules
   are 'how a check may establish truth', and one home chosen once by the build that must choose
   anyway is the single-home posture.** A4-2 either relocates this clause into that home or
   points at it — named in Out of scope so it cannot be dropped.

3. **The finding keeps the key `linkage_ripe`; the prose carries the correction.** *(Owner-ruled
   2026-07-25 at brief time.)* After inversion the name reads backwards ("linkage ⇒ ripe" is
   exactly the bug), and `:83`'s parenthetical — *"deliberately distinct from `orphans`, which
   means the opposite"* — becomes **false**: post-fix the two share polarity (both mean "nothing
   points here"). Renaming was weighed and declined: the key is referenced by build-20, the
   Arc-3 ledger, and the **inherited FAILED clause** whose discharge is measured against it, and
   key stability keeps that chain traceable. The remedy is prose — `:83` states the polarity
   unambiguously, marks the name historical, and replaces the false parenthetical with a
   same-polarity note.

4. **Prose `## Sources` entries are IN SCOPE, as part of the citation leg.** SPIKE-2 §5 asked
   whether an implementation reads the legs the audit found load-bearing and found nothing
   shipped addresses prose Sources entries. The audit (`:69`) is explicit that pages
   back-reference notes via body wikilinks **and** prose Sources entries, and that frontmatter
   `sources:` entries are *sometimes human prose, not paths* — so a citation leg that reads only
   frontmatter re-creates a known blind spot, and a blind spot in an **absorption** test is a
   false positive (a note called ripe that was in fact absorbed). Cost is near zero: the
   inbound-wikilink leg already requires reading wiki page bodies. The leg is therefore defined
   as **cited by a wiki page** — in the page's frontmatter `sources:` *or* its prose `## Sources`
   section, by path or unambiguous reference.

5. **The substituted `topic:`-overlap leg is DROPPED from the projection.** It was never a
   calibration leg (the audit used topic overlap only in its Phase-0 index, `:4`, never in the
   recommended union, `:69`), and the audit's §2 verdict is that `topic:` tags cannot support a
   topical projection as-is (four serialization styles, vocabulary drift and cross-domain
   collision — `football` is NFL *and* soccer at note level). **This does not touch the tier-1
   `topic:`-is-a-YAML-list check or its string→list auto-fix** (`vlt-lint:60`, `:94`), which stay
   exactly as they are — that is schema hygiene, not candidacy.

6. **No honest-reporting / report-line work in this build.** The silent-zero decide-once ruled
   ONE general rule, written by A4-2, cited by the rest: *no site briefs a bespoke report-line
   fix.* Post-fix `linkage_ripe` will legitimately return small counts and sometimes zero — that
   zero's honesty is A4-2's rule to govern. A4-1 changes the report slot's **description** only
   (F4), because it currently states the old mechanic.

7. **The 41-hit baseline precondition is DISCHARGED by SPIKE-2's artifact; do not re-run it.**
   The attached evidence debt required the projection be re-run and the hit list preserved
   *before any change lands*. SPIKE-2 did exactly that, in both polarities, and preserved the
   enumeration at `skills/reports/spike2-projection-baseline-2026-07-25.md`. Carried caveat,
   stated so no later reader over-reads the artifact: **the original 41-hit list is permanently
   unrecoverable** — its substrate (the scalar-`topic:` cohort) was destroyed by the auto-fix in
   the same run. The preserved file is a *current-state* baseline, not that list.

8. **Honest limits carried as context, not tails** (ideation: not-blocking). The candidacy pass is
   **prose-specified and agent-run, not code** — SPIKE-2's re-run *models* it faithfully but is
   not the same computation (the 41↔41 list-form correspondence is corroboration, not proof); the
   8-note ripe set is **mechanical**, without the audit's 9-agent hand-verification (3 of 8 map to
   audit-identified items); and the measurement is **vlt-core only** (vlt-sayari is unreadable
   from this machine). These bound how strongly the verification below can be stated — they do
   not gate the build.

9. **The two A3-22 prose items land in the operating contract, together, in one home.** They are
   a rule and its documented default and must not separate. Home chosen: the contract's
   `## Sessions, sittings, and hand-offs` section, immediately after **Role boundary at the
   seam** (`:224`) — the existing home of cross-partner authority boundaries. The contract is
   **deliberately not handshaked** (single-home + pointers), so this adds no `version:`/consumers
   obligation. Read-and-cite also carries the future mechanism's trigger rule (*spawn only when
   the interaction should be remembered*), which is why it ships ahead of A4-5 rather than with
   it.

## F1 — `vlt-lint/SKILL.md:43` — the candidacy pass's declared inputs

**Current state** (`:43`, inside the Step-0 fan-out note; verified 2026-07-25):

> …**and the `{research}`-zone graduation-candidacy pass (`linkage_ripe` / `revisit_due` + the
> widened `topic:` check, Step 2)** stay yours; fill those report slots from your own pass. The
> research-candidacy pass runs **inline** here (per-note reads of `revisit_after:` + `sources:` +
> frontmatter `topic:`), **not** fanned out — for the first cut and typical research-zone sizes
> that is fine…

**The exact change.** Correct the declared inputs to what the fixed projection actually reads,
and make the wiki-side read explicit (it is load-bearing and currently unstated):

- Replace the parenthetical `(per-note reads of `revisit_after:` + `sources:` + frontmatter
  `topic:`)` with the true input set: **per-note reads of `revisit_after:` + `sources:`, cross-read
  against every wiki page's frontmatter `sources:`, body `[[wikilinks]]`, and prose `## Sources`
  section**.
- Leave `+ the widened `topic:` check` in the list of things that stay this SKILL's own — it
  refers to the tier-1 `topic:`-is-a-list check on `{research}` notes, which is untouched
  (disposition 5). If the sentence reads ambiguously after the edit, disambiguate it explicitly
  as *the `topic:`-is-a-list schema check* — do not delete it.
- Keep the **inline, not fanned out** statement and its second-cut note verbatim.

**Why.** After F3 the pass no longer reads note `topic:` for candidacy and unambiguously requires
a wiki-side read; a stale input list is how the next builder mis-implements the pass. Single-home:
`:43` names *what the pass reads*, `:83` owns *the rule*.

**Out of scope here.** Giving the `vlt-lint-full` workflow a `{research}` zone remains the named
second-cut work; this build does not fan the pass out.

## F2 — `vlt-lint/SKILL.md:82` — the boundary clause on derive-first

**Current state** (`:82`, the candidacy-pass header; verified 2026-07-25):

> - **Research-note graduation candidacy** (candidacy pass; both modes) — a **`{research}`-zone
>   read**, run **inline** in this SKILL's own jurisdiction (like the governance checks above),
>   **not** by the `vlt-lint-full` workflow (which sweeps `{wiki}` only — Step 0). Two surfacing
>   findings, both `flag_for_human`, **never auto-promoted** (routing a ripe note to a partner for
>   graduation is judgment work, the merge-candidate / `review_due` posture):

**The exact change.** Append one short clause to this header paragraph, generally worded, marked
as a boundary on derive-first rather than a new law. Wording to this effect (match the file's
voice; keep it to two sentences):

> **Boundary clause on derive-first.** Derive-first does not license deriving a state from the
> residue of the very process that produces it — where the only available signal is the process's
> own leavings, the state must be recorded, not inferred, or the check must be read in the
> polarity the evidence actually supports. This pass derives *absorption* (evidence the wiki has
> taken a note up), never *graduation* (the event), which is why absence of linkage is the signal
> and presence of it is not.

**Preserve verbatim:** `never auto-promoted` and the flag-for-human posture. That clause is the
only reason the 41-candidate load cost nothing, it **discharged** on the same run that failed the
FP clause, and any fix that weakens it over-corrects.

**Why.** Discharges the verification-by-residue decide-once ruling (stated, not legislated), and
per disposition 2 this is its stated home until A4-2 chooses a governance home.

## F3 — `vlt-lint/SKILL.md:83` — the projection itself (the build's core)

**Current state** (`:83`, verified verbatim 2026-07-25):

> - **`linkage_ripe`** — a `{research}` note is graduation-**ripe** when the **union projection**
>   flags it: frontmatter `topic:` overlap with a wiki page **∪** an inbound body `[[wikilink]]`
>   from ≥1 wiki page **∪** a shared `sources:` overlap with a wiki page. Surface the note and
>   which projection component fired. The **union** — not naive frontmatter-`topic:`-only — is
>   mandatory: field calibration measured the naive projection at a ~69–79% false-positive rate
>   versus ~21–23% for the union across two opposite-profile vaults, so a naive-level
>   false-positive storm is the failure signature. (The term is deliberately distinct from
>   `orphans`, which means the *opposite* — a wiki page with **no** inbound links.)

**The exact change.** Replace the whole bullet. Every clause below is load-bearing:

- **Polarity.** A `{research}` note is graduation-**ripe** when the **absorption union finds
  nothing** — no evidence any wiki page has taken it up. Presence of linkage means **already
  absorbed ⇒ exclude**.
- **The three legs** (all absorption evidence; any one hit excludes the note):
  1. **Cited** — a wiki page names the note in its frontmatter `sources:` **or** in its prose
     `## Sources` section, by path or unambiguous reference (frontmatter `sources:` entries are
     sometimes human prose rather than paths — disposition 4).
  2. **Linked** — an inbound body `[[wikilink]]` from ≥1 wiki page.
  3. **Shared-source** — the note and a wiki page share an entry in `sources:`.
- **Report what is missing, not what fired.** The old bullet said "surface … which projection
  component fired"; under the inverted polarity nothing fires on a ripe note. Surface the note
  and, where cheap, the nearest-miss context (e.g. *no citing page; nearest topical page X*).
- **The calibration statement, restated honestly.** Do **not** carry the `~21–23%` figure as a
  false-positive rate — SPIKE-1 established it was never one (21% = vlt-core's union residual as
  a share of the naive flagged set, 13/62; 23% = vlt-sayari's union flag rate over population,
  3/13). State instead: *the naive orphan signal (frontmatter citation alone) measured ~79%
  false-positive on a mature zone; the absorption union measured ≈0% false-positive across two
  opposite-profile vaults, surfacing ~8–14% of the research zone. **A high surfacing rate is the
  failure signature** — if this pass flags most of the zone, the polarity or a leg is wrong.*
- **The `orphans` note.** Delete the false "means the *opposite*" parenthetical. Replace with:
  *the name is historical — it marks candidacy decided **by** linkage, not candidacy caused by it;
  post-fix this shares polarity with `orphans` (both mean "nothing points here"), the difference
  being layer (`orphans` = a wiki page with no inbound wiki links; `linkage_ripe` = a research
  note no wiki page has absorbed).*
- **Do not add** a `graduated:`/`graduated_into:` key or any stored graduation state (disposition
  1).

**Why.** This is the defect. It restores the polarity two vaults' field calibration validated,
restores the leg the module dropped, removes the leg the module invented, and replaces an
unsatisfiable published target with the measurement that actually exists.

**Grounding note on the third leg's writer.** The A3-23 capture recorded that `vlt-ingest` never
authors a wiki→research `[[wikilink]]` (page template `:107-124` has no such field; Connections
`:131` is page-to-page), so the linked leg fires only on hand-written links. **Verified still
true 2026-07-25.** This build does **not** add such a writer — under the restored polarity a
never-firing absorption leg is conservative (it can only fail to exclude), where under the shipped
polarity it was a silent two-leg reduction. Recorded so a later reader does not re-derive it as a
missing fix.

## F4 — `vlt-lint/SKILL.md:141` — the report-key slot

**Current state** (`:141`, inside the Step-5 `flag_for_human` block; verified 2026-07-25):

```yaml
  linkage_ripe: [<research-note — union projection: topic ∪ inbound wikilink ∪ shared sources>, ...]
```

**The exact change.** Key name **unchanged** (disposition 3). Slot description restated to the
new rule, as a short label — the mechanic's single home is `:83`, not here:

```yaml
  linkage_ripe: [<research-note — no absorption linkage: cited ∪ inbound wikilink ∪ shared sources>, ...]
```

**Out of scope here.** No honest-limit / silent-zero line is added to this slot or to the report
block (disposition 6) — that is A4-2's general rule.

## F5 — `governance/_meta/conventions/frontmatter.md:138` — the pointer

**Current state** (`:138`, tail of the `revisit_after:` paragraph; verified verbatim 2026-07-25):

> …`vlt-lint` **surfaces** a past-due `revisit_after` and the union-projection linkage finding
> (`linkage_ripe`); it never auto-promotes a note into the wiki — graduation is judgment work
> (see `vlt-lint`).

**The exact change.** Delete the restated mechanic; keep the pointer:

> …`vlt-lint` **surfaces** a past-due `revisit_after` and the linkage finding (`linkage_ripe`);
> it never auto-promotes a note into the wiki — graduation is judgment work (see `vlt-lint`).

**Why.** `union-projection` describes the mechanic this build replaces, in a file that is not its
home. Single-home discipline: this line *points*, it does not restate — which is also what keeps
it immune to the next change at `:83`.

**Handshake: NO BUMP.** `frontmatter.md` stays at `version: 4`, consumers unchanged
(`vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-mint`). This is a prose clarification that
*removes* a restatement — no rule the convention states changes, so no bump and **no consumer
walk** (CLAUDE.md version-handshake rule; a rule change bumps, prose does not).

**Untouched at this file, deliberately:** `:133` and `:136` (the research-note schema and its
written-once / no-`last_updated` rule) and `:242` (the adoption axis — A4-2's site).

## F6 — `governance/_meta/vault-operating-contract.md` — the two A3-22 prose items

**Current state.** The contract's `## Sessions, sittings, and hand-offs` section carries **Role
boundary at the seam** at `:224` — *"The handing-off partner conveys what changed and what it
complicates; the **receiver chooses the mechanism** … The hander does not dictate filing
mechanics — that reaches across the single-writer line."* No rule anywhere in the shipped bundle
forbids a partner from answering **as** another partner. Verified 2026-07-25: no such rule in the
contract, in any `{conventions}/*.md`, or in `{personas}` (which holds the five council lenses —
architect / historian / moderator / pragmatist / skeptic — not partner personas).

**The exact change.** Add one short subsection immediately after the `:224` role-boundary
paragraph, carrying both items together (disposition 9):

1. **The prohibition** — *a partner never speaks in another partner's voice; it consults, or it
   cites.* Frame it as the authority sibling of the existing mechanism boundary: the role boundary
   says a partner does not dictate another's *mechanics*; this says it does not borrow another's
   *authority*. Answering out of another partner's domain in that partner's voice manufactures
   authority the answer does not have — strictly worse than declining, because a cited answer is
   checkable and an impersonated one is not.
2. **Read-and-cite as the documented default** — when a partner needs another's domain, the
   default is to **read that partner's zone / the wiki and cite it**, in its own voice, attributed.
   State the trigger rule the default implies, because it is load-bearing for the later mechanism:
   **spawn another partner only when the interaction should be remembered** — memory is what
   justifies a consult's cost, and is therefore also the test for when *not* to have one.

**Why.** Both are ruled to ship independently of the consult channel and sooner (ODQ #9), and to
ride the earliest-shipping build (A4-1). Read-and-cite works the day it lands and hands A4-5 its
own affordability test.

**Out of scope here — hard boundary.** No `consult` dispatch mode, no `{conventions}/consult.md`,
no `vlt-lint` out-of-authority check, no `vlt-dispatch` edits of any kind. All of that is A4-5,
and it does not ship without its governance pairing. If the prose above seems to want a mechanism
sentence, that sentence belongs in A4-5.

**Handshake / registration.** The operating contract is **deliberately not handshaked** (CLAUDE.md
standing rule: single-home + pointers, no `version:`/`consumers:`) — this adds no ack obligation
anywhere. Bump the file's frontmatter `last_updated:` to the build date.

**Scrub.** Contract prose is shipped surface: no vault-local names, no install-specific paths,
worked illustrations use placeholder paths.

## Registration

**None.** No new skill, no new workflow, no new mode — so no `module-help.csv` row and no help-CSV
touch (the four-site dispatch registration surface belongs to A4-5). No convention `version:`
moves, so **no consumer walk and no re-ack**. The `linkage_ripe` report key is unchanged
(disposition 3), so no dashboard/report contract changes.

## Out of scope (dispositioned)

- **A graduation-state key (`graduated:` / `graduated_into:`), `frontmatter@5`, a consumer walk** —
  *rejected-because*: SPIKE-2 resolved derive-vs-store toward DERIVE; absorption is computable from
  disk today and tracks the drain. Derive-first holds unbent.
- **The governance home for the derive-first boundary clause** — *deferred-to-A4-2*, which must
  choose a home for the general honest-reporting rule anyway (disposition 2). A4-2 relocates this
  clause into that home or points at it; it must not create a second home.
- **The general honest-reporting rule and any report-line silent-zero fix** — *deferred-to-A4-2*
  by the decide-once ruling (disposition 6).
- **Renaming `linkage_ripe`** — *rejected-because* key stability keeps the inherited FAILED
  clause's discharge chain traceable (disposition 3); the prose carries the correction.
- **Writing a wiki→research `[[wikilink]]` in `vlt-ingest` Step 6** — *rejected-because* under the
  restored polarity a never-firing absorption leg is conservative (see F3's grounding note). If a
  vault later wants it, it is an ingest-template change, not a lint fix.
- **`cluster_ripe`** — *already-covered-by* build-20's deferral; the audit's §2 verdict (four
  `topic:` serialization styles, vocabulary drift and cross-domain collision) still stands and
  this build removes the only place that verdict was being violated.
- **Fanning the candidacy pass out to `vlt-lint-full`** — *deferred*: the named second-cut work
  (`vlt-lint:43`), unchanged by this build.
- **`sources_vs_prose_mismatches` (`vlt-lint:128`)** — *out of scope, observed not fixed*: the
  report slot exists in Step 5 but no Step-2 check defines it (verified by reading Step 2 in full,
  `:55-88`). Adjacent to F3's prose-`## Sources` leg but a different finding on the wiki side.
  **Recommended: file to `inbox/` so it enters the loop as a filing** rather than being fixed
  off-brief here. *(Owner to decide — the same posture the roadmap takes on the brief-time drift
  class.)*
- **The brief-time drift class** (the roadmap's own open item — no check compares a brief's
  restatement against the filing it cites; this inversion entered at
  `build-20-graduation-queue.md:211-216`) — *out of scope*: it is an unfiled lifecycle-tooling
  question, not module source, and the roadmap already recommends filing it.

## Verification (unit, at rest — lifecycle step 5)

The pass is prose-specified and agent-run, so verification is re-derivation against the preserved
baseline plus cross-file agreement greps. Run all of it before committing.

1. **Re-derivation against the SPIKE-2 baseline (the load-bearing check).** Take the rewritten
   `:83` rule as written and apply it by hand to a sample from
   `skills/reports/spike2-projection-baseline-2026-07-25.md`: **all 8** calibration-polarity notes
   (must be classified ripe) and **at least 10** of the 90 absorbed notes spanning all three leg
   patterns (`shared` only, `wl,shared`, `topic,wl,shared` — must be classified absorbed ⇒
   excluded). A rule that cannot be applied unambiguously by hand to those 18 is under-specified
   — tighten `:83` until it can. **Expected outcome: ~8 of 98 ripe, not ~97.** Record the sample
   and result in the build's `status:`.
   - *Note the one honest asymmetry:* the baseline's `topic`-only-leg notes (acotar-series,
     empyrean-series, llm-wiki-v2, reading-queue-update, fiddleheads, world-cup, black-opening)
     are absorbed=False and ripe under both the calibration polarity and the new rule — dropping
     the `topic:` leg is what makes them agree.
2. **Drain-tracking spot check.** Against the same artifact, confirm the four audit items since
   graduated (ashwagandha, wispr-flow, youtube-to-markdown, kettl routing failure) classify
   **absorbed ⇒ excluded**, and the one never drained (the world-cup group-stage note → the still
   unbuilt `fifa-world-cup-2026` page) classifies **ripe**. This is the polarity defect
   demonstrated rather than argued; if it does not reproduce from the written rule, the rule is
   wrong, not the artifact.
3. **Single-home grep.** `grep -rn 'linkage_ripe' skills/` — expect exactly four shipped sites
   (`vlt-lint:43`, `:82-83`, `:141`, `frontmatter.md:138`) and no others. Confirm the mechanic is
   stated **once** (`:83`); every other site is a pointer or a slot label.
4. **Stale-description grep.** `grep -rniE 'union projection|union-projection|topic.{0,12}overlap' skills/`
   — expect **zero** hits describing `linkage_ripe`. (Hits on the tier-1 `topic:`-is-a-list check
   at `:60`/`:94` are expected and correct — verify each hit is that check, not the projection.)
5. **Preserved-posture grep.** Confirm `never auto-promote` / `flag_for_human` posture survives at
   `:82`, and that `revisit_due` (`:84`) is byte-unchanged — it is A4-2's site, not this build's.
6. **Handshake bipartite re-check.** No convention `version:` moved, so the expected result is
   *unchanged and consistent*: `frontmatter` stays `@4` with five consumers, every consumer's
   `depends_on` still pins `frontmatter@4`. Run the check to prove nothing moved by accident.
7. **Packaging lint (mid-arc).** `uv run tools/package-lint.py` Groups A/B/C — exit 0. (Group D /
   `--expect-version` is the release gate, not this build's.)
8. **Scrub.** No personal or vault-local content in any changed shipped file. **Specifically:** the
   vlt-core note filenames, the audit path, and the baseline artifact are named **in this brief
   and in the build's `status:` only** — `skills/reports/` is gitignored. None of them may appear
   in `vlt-lint/SKILL.md`, `frontmatter.md`, or the contract.
9. **Housekeeping.** Delete any per-skill `.decision-log.md` the build produced; one commit for
   the build; rewrite this brief's `status:` to a BUILT record with numbered deviations.

## Release

**Not a release build by default.** Arc 4 runs A4-1 → A4-5; the dual version bump
(`.claude-plugin/marketplace.json` `"version"` + `skills/vlt-setup/assets/module.yaml`
`module_version`) and the pre-tag `uv run tools/package-lint.py --expect-version X.Y.Z` gate ride
whichever build is last in the version. Do not bump either string in this build.

**Named because it is plausible and the builder should not have to rediscover it:** the defect is
live and worsening on the primary vault (~97 of 98 latent), so the owner may elect to cut a patch
release on A4-1 alone. If so, the release obligations attach here unchanged — both version
strings, `--expect-version` gate (tag only on exit 0, PASS line in the release commit message),
then ff-merge to `main`, tag, push main + tag. That is an **owner call at build time**, not a
default this brief takes.

## Acceptance (live — appended to the roadmap ledger)

Rides the next ordinary `vlt-upgrade` + full-lint run on vlt-core (owner-run).

1. **The inherited Arc-3 debt discharges here, against the restated target.** On a full `vlt-lint`
   run over the mature vlt-core research zone, `linkage_ripe`'s false-positive rate is
   **hand-verified** — a human checks whether each surfaced note is genuinely un-absorbed — and is
   near the calibration's **≈0%**, and in no case exceeds the naive signal's **~79%**. An FP rate
   against an FP rate; **not** self-reported by the pass under test, and **not** compared to the
   `~21–23%` set-reduction ratio (the wording that made the original clause unsatisfiable).
   Baseline for comparison: `skills/reports/spike2-projection-baseline-2026-07-25.md`.
2. **Surfacing rate collapses.** The run surfaces on the order of **~8 of ~98** notes (≈8% of the
   research zone / ~14% of the naive orphan set), not ~97. A surfacing rate near population is the
   failure signature and means the fix did not take.
3. **The projection tracks the drain.** Notes graduated since the 07-11 audit are **not** surfaced;
   the never-drained one still is. Same disk, opposite behavior from the 07-25 run.
4. **The never-auto-promote posture survives.** Every candidate is surfaced for a human; none is
   promoted into the wiki by lint. (This clause discharged once already on the 07-25 run — it must
   not regress under the new polarity.)
5. **The two prose items reach the field.** After upgrade, the installed vault contract carries the
   partner-voice prohibition and read-and-cite as documented default (base-convention refresh path;
   any local overlay survives untouched).
6. **Second-vault check, if reachable.** If vlt-sayari (13 notes / 34 pages, the opposite profile
   the calibration used) becomes readable, confirm the surfacing rate there is of the same order —
   the calibration's 3/13. Not blocking: SPIKE-2's measurement is **vlt-core only** and this
   remains an unverified second axis.

## Handoff

Build in a fresh session via `bmad-workflow-builder`. Exit obligations: rewrite this brief's
`status:` to a BUILT record with **numbered deliberate deviations** (record the derive-vs-store
closure and the F1-9 verification sample there), delete any `.decision-log.md`, one commit for the
build. Acceptance is deferred to the ledger — do not attempt it at build time.
