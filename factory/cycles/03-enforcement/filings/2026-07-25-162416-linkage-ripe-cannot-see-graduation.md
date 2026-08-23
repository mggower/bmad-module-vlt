# Defect: `linkage_ripe` cannot distinguish "ripe for graduation" from "already graduated" — 41/41 false on vlt-core

_Filed 2026-07-25 by the acceptance auditor during the Arc 3 discharge run (pass 6, "full-lint
pass"), from the `vlt-core` `[2026-07-25 15:05] lint (librarian) | full` run — the very run the
2026-07-25 ruling named as build-20's discharging event. The check **FAILED** its acceptance clause;
this filing is the contradiction routed back as field signal per the discharge rubric. **Defect in
module source**, not vault drift (the vault's `vlt-lint/SKILL.md` is byte-identical to factory
source, `diff -q` this run)._

## The finding, measured

The full lint's research-note candidacy pass surfaced **41 `linkage_ripe` candidates. Zero were
real.** Every one resolved to a research note that had **already graduated** into the wiki.

> `_agent/sessions/2026-07-25-150500-lint.md:26` — "41 `linkage_ripe` graduation candidates → **0** —
> all resolved to notes that had *already* graduated" · cost if trusted: "would have re-graduated
> filed material"

That is a **~100% false-positive rate**, against build-20's acceptance clause:

> "the false-positive rate tracks the calibrations (union ≪ naive — A3-8 ~21% vs ~79%, A3-9 ~23% vs
> ~69%) … a naive-level FP storm is a failure"
> (`skills/reports/inbox-evolution-arc3-roadmap.md`, build-20 ledger item)

100% does not merely miss the ~21–23% union target — it is **worse than the ~69–79% naive baseline
the union exists to beat**. The failure signature the brief names is met and exceeded.

## Root cause — structural, not a tuning miss

`skills/vlt-lint/SKILL.md:83` defines ripeness as a union of three signals:

> frontmatter `topic:` overlap with a wiki page **∪** an inbound body `[[wikilink]]` from ≥1 wiki
> page **∪** a shared `sources:` overlap with a wiki page

**All three are the residue that graduation itself leaves behind.** When a research note graduates,
`vlt-ingest` writes a wiki page that cites the note's sources, shares its topics, and links to it.
The union projection is therefore not measuring readiness-to-graduate — on a mature vault it is
measuring *has-graduated*, and it fires hardest on exactly the notes that need it least.

The projection has no way to tell the two apart, because **the research-note schema carries no
graduation state at all**:

- `governance/_meta/conventions/frontmatter.md:136` — research notes are written-once, carry **no
  `last_updated`**, and hold no back-pointer to the page they fed.
- `frontmatter.md:138` — `revisit_after:` is the **only** candidacy key, optional, absence-by-default
  (and separately filed today as unadopted: `2026-07-25-144500-revisit-after-has-no-adoption-path.md`).
- `skills/vlt-ingest/SKILL.md:71-90` — Step 5 writes the note; nothing in the ingest path stamps a
  note as consumed when Step 6 graduates it into the wiki.

So the defect is a **missing state**, not a bad threshold: no exclusion clause can be written today
because there is nothing on disk that says "this note already graduated."

## Why this compounds

The FP rate **rises as a vault matures** — the more research that has been ingested, the more notes
carry graduation residue, the noisier the check gets. That inverts the intended behavior: a queue
meant to surface neglected material gets loudest precisely where the vault is healthiest. And the
cost is not merely noise — the session records the damage-if-trusted as *re-graduating already-filed
material*, i.e. duplicate wiki content.

Note the shape relative to this arc's other findings: the `revisit_after` gap and `spec.md`'s
`deferral_metric` are **silent-zero** scars (non-adoption reads as clean). This is the mirror image —
a **noise storm** that reads as a working detector. Both defeat the same thing: a human's ability to
read the report as signal.

## What the check *did* get right (recorded so a fix doesn't over-correct)

The flag-for-human posture held under a 41-candidate load: the run **surfaced and did not act on**
any of them, and the human caught the class before promotion. `never auto-promoted` is doing real
work here — it is the only reason this cost nothing. Any fix should preserve it.

## Honest limits

1. **The 41-hit list was not preserved.** The finding rests on the vault's own verification of the
   set, not a re-derivable enumeration. A fix build should re-run the projection and capture the list
   before changing it.
2. **How it was computed is not fully established.** `vlt-lint/SKILL.md:43` says the research-candidacy
   pass runs **inline** in the SKILL, not fanned out; the session groups this class alongside genuine
   *delegate* measurement errors (7 false over-length summaries, 55 cross-layer link artifacts from a
   bad `crossLayerSlugs` invocation). Whether an agent computed the union is unknown. **But what was
   verified is computation-independent:** every surfaced note had already graduated — no measurement
   rule error produces that.
3. **The 21% → 100% gap is unexplained and is the sharpest open question.** The A3-8 calibration that
   produced ~21% was measured on **this same vault** on 2026-07-11. The most likely explanation is
   that the calibration sample excluded already-graduated notes — i.e. it measured the projection
   against the population it was *hoped* to run on rather than the one it actually runs on. A fix
   build should re-read the A3-8 calibration method before trusting either number.

## Suggested direction (not a ruling)

The obvious candidates, cheapest first — all of them need the missing state, so the real decision is
where that state lives:

- **`vlt-ingest` stamps the note on graduation** (a `graduated:` / `graduated_into:` key written at
  Step 6). Gives the projection a hard exclusion, costs a `frontmatter` version bump + consumer walk.
- **Derive it instead of storing it** — treat "a wiki page whose `sources:` names this note" as the
  graduated signal, no schema change. Cheaper, but it is inference, and it is exactly the kind of
  derive-vs-record call this arc has ruled on before (derive-first invariant).
- **Invert the union** — require a signal that graduation does *not* produce. Least likely to work;
  all three current components are graduation residue.

Whichever way it goes, the acceptance clause it must satisfy is unchanged: the FP rate has to track
the ~21–23% union calibration on a **live, mature** research zone, measured after the fix.

## Ledger consequence

Build-20's *FP-rate-tracks-calibration* clause is graded **FAILED** (not a waiting tail — it was
exercised and it failed). Its sibling clauses discharged on the same run (legacy-no-noise,
honest-scoping, never-auto-promote), so build-20 now closes on the Arc-4 fix of this defect rather
than on any further lint run.
