# A brief restated a field calibration with its polarity flipped, and nothing in the loop could catch it

_Filed 2026-07-25 from the **factory**, not from a vault. Found while running SPIKE-1/SPIKE-2 of the
Arc-4 ideation session (roadmap: `skills/reports/inbox-evolution-arc3-roadmap.md`, *Ideation rulings
— A3-18..A3-23*). Precedent for a factory-origin filing: `2026-07-25-132141-partner-consult-…` was
filed by the owner out of a factory-side ideation session. **Classification question for capture is
live and stated at the bottom — this may produce no module build at all.**_

## The claim

`build-20` shipped a `vlt-lint` check whose defining sentence **inverts the field measurement it
cites**, and the defect survived: a brief, a build, unit-verification at rest, a release lint, a
tagged release, six acceptance passes, and a graded acceptance clause — until a spike re-read the
source filings 14 days later. No step in the loop re-reads a filing to check what a brief said about
it, so the inversion was never checkable in principle.

## The chain, with citations

**1. What the field measured.** Two calibrations, opposite-profile vaults, both treating the union
as an **absorption test** — linkage means the note is *already absorbed*, so **exclude** it; a note
was ripe when it had **no** linkage:

- `inbox/2026-07-11-153000-graduation-queue-field-calibration.md` §1 and its source artifact
  (`vlt-core` `_agent/artifacts/research-wiki-audit-2026-07-11.md:19`, `:69`): the mechanical orphan
  set is 62 of 90, **49 of those are absorbed anyway**, and "the projection must union: frontmatter
  citation + body wikilinks + shared-source overlap. With that union, the residual orphan set here
  is ~13 notes — and every genuine gap is inside it."
- `inbox/2026-07-12-114837-…sayari-calibration.md:22-26`: "The shared-source-overlap leg did the
  heavy lifting here exactly as in vlt-core… the durable/project-state split working as designed,
  **not orphaning**."

**2. What the capture recorded — correctly.** The Arc-3 roadmap's A3-8 capture: "Naive
frontmatter-only projection is ~79% false-positive (62/90 flagged, 49 absorbed); the union
(frontmatter ∪ body wikilinks ∪ shared-source overlap) is what should ship." Right legs, right
polarity, and it claims **no** false-positive number for the union.

**3. What the brief wrote.** `skills/reports/build-20-graduation-queue.md:210-216` — "a `{research}`
note is graduation-**ripe** when the **union projection** flags it — frontmatter `topic:` overlap ∪
body `[[wikilink]]` inbound ∪ shared-`sources:` overlap… A3-8/A3-9 measured naive at ~79%/~69%
false-positive vs union ~21%/~23%." Three distinct drifts in two sentences:

- **Polarity inverted** — the union now means *ripe*, where the field used it to mean *absorbed*.
- **A leg substituted** — `topic:` overlap replaced **frontmatter citation**. The audit used topic
  overlap only in its Phase-0 index (`:4`), never in the union it recommended (`:69`).
- **A number relabelled** — "union ~21%/~23% false-positive". Neither is a false-positive rate:
  21% is vlt-core's union residual as a share of the *naive flagged set* (13/62); 23% is
  vlt-sayari's union *flag rate over population* (3/13). The union's measured FP rate was ≈**0%**.

**4. What shipped.** `skills/vlt-lint/SKILL.md:83`, verbatim from the brief. Its parenthetical —
"(The term is deliberately distinct from `orphans`, which means the *opposite* — a wiki page with
**no** inbound links.)" — shows the naming tension **was noticed at build time and resolved in
prose, in the wrong direction.**

**5. What it cost.** The 2026-07-25 vlt-core full lint: 41 `linkage_ripe` candidates, **0 real**.
Re-measured during SPIKE-2 after the same run auto-fixed the substrate that was damping it:
**97 of 98 notes surface, 90 already absorbed (≥93% FP)**. The calibration's own polarity on the
same disk surfaces 8 of 98 and correctly excludes the four audit-identified gaps that have since
graduated. One graded-FAILED acceptance clause, one arc-boundary ruling, two spikes, and an
inherited Arc-4 debt trace to those two sentences.

## Why nothing caught it (the actual finding)

Every verification the loop performs is **downstream of the brief**, so all of them are consistent
with a brief that misread its source:

- **Unit-verification at rest** checks cross-file agreement — that the shipped text matches what the
  brief said. It did match. That is exactly the problem.
- **The acceptance clause was authored by the same brief** that misread the source, so it inherited
  the misreading and was **unfalsifiable**: "FP rate tracks ~21–23%" compares an FP rate to a
  set-reduction ratio. Six acceptance passes ran against it; none could have failed for this reason.
- **Capture is the only step that reads filings closely — and it got it right.** The drift entered
  strictly between capture and brief, in the one step with no source-fidelity check.

Stated generally: **a brief's restatement of a filing's evidence is never re-derived against the
filing.** Briefs cite `file:line` into *module source* (rigorously, and that discipline works) but
cite filings only by name.

## Candidate shapes (not ruled — capture/ideation owns this)

1. **Back-cite restatements.** Any brief sentence restating a filing's measurement or recommendation
   carries a `file:line` into the *filing*, and unit-verification re-reads those cites the way it
   already re-reads module-source cites. Cheapest; mechanical; would have caught the polarity flip.
2. **Numbers carry their denominators.** A brief may not cite a bare percentage from a filing —
   it states numerator, denominator and population. "~21%" would have had to be written "13 of the
   62 naive-flagged notes", which is self-evidently not a false-positive rate.
3. **Acceptance clauses state their measurement procedure**, not just a target, so a clause is
   falsifiable by someone who did not write it. A clause naming "hand-verified FP rate on a mature
   research zone" cannot be discharged by a self-report from the pass under test.
4. **A polarity/semantics prompt at brief time** for any check derived from field measurement:
   *does the signal mean the thing is ripe, or that it is already handled?* One question; it is the
   whole defect.

Shapes 1–3 are complementary and independently useful; 4 is nearly free.

## Honest limits

- **One instance.** The class is inferred from a single occurrence; the arc has a standing ruling
  against pre-generalizing from one. Weigh accordingly.
- **The counterfactual is untested.** No evidence that shape 1 or 2 *would* have caught it — only
  that both target the exact failure mode.
- **This is not a quality claim about the brief.** `build-20-graduation-queue.md` is otherwise a
  strong brief with dense, accurate module-source grounding. The failure is structural — the loop
  gives module-source citations a verification step and filing citations none.
- **Single-vault evidence** for the cost half (vlt-core; vlt-sayari unreadable from this machine).
- **Factory-origin, not field friction.** Nothing in a live vault surfaced this; a spike did.

## Classification question for capture (please rule before scoping)

The remedy probably lands in **factory** artifacts — the `build-brief` skill, `CLAUDE.md`'s lifecycle
steps 4–5, possibly the brief template — none of which ship to vaults. If so this filing produces
**no module build**, like A3-18, and belongs in the factory's own process record rather than an arc's
build plan. Alternatively the `091002` precedent applies (the packaging lint was factory-side and
*did* get a build, with `tools/` tracked as public documentation of the release contract), in which
case it is ordinary arc work. **Capture should rule which, before anyone scopes it.**
