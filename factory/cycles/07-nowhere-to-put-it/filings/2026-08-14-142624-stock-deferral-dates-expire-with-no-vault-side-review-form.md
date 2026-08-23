# Stock `review_after` deferral dates expire inside every vault, and the vault has no non-diverging form for the review

_Filed 2026-08-14 from **vlt-core**, during a scoped `vlt-lint` run (2026-08-14 13:36) that surfaced
three deferrals three days from expiry, and the `vlt-mint` convention-edit ceremony that was opened to
review them and could not proceed. Evidence is vlt-core, read-only. Classification: **defect** —
structural, in the enforcement-declaration machinery rather than in any one convention._

## The claim

Three shipped conventions carry a complete deferral triple whose `review_after` is **2026-08-17**:

| convention | version | stage | `deferral_metric` |
| --- | --- | --- | --- |
| `frontmatter.md` | 5 | `checked` | prose/behavior drift lint findings + new conventions minted |
| `spec.md` | 2 | `declared` | spec version bumps shipping without their relay entries |
| `wiki-consolidation.md` | 1 | `declared` | near-duplicate findings carried unresolved across sweeps |

All three are **byte-identical to `_agent/conventions/.baseline/`** — i.e. these are the factory's
dates, shipped to every install, not any vault's ruling. On 2026-08-17 every vault running 0.9.1 starts
reporting `deferral_expired` on the same three conventions on the same day, regardless of what that
vault has actually observed.

**The vault has no good move.** All three roads are blocked or costly:

1. **Edit the base** (bump `review_after`) → the base diverges from `.baseline`, so `vlt-lint`'s
   `convention_base_divergence` fires on all three, every run, until upstreamed. One recurring finding
   traded for another.
2. **Write an overlay** → impossible by construction. `{overlays}/{name}.overlay.md` is **append-only
   and may only add**; `review_after` is an existing base field. A date change has no overlay form.
   (`vlt-mint`, *Edit a convention*: *"An overlay can only add; it cannot change an existing base rule."*)
3. **Promote the stage** → `declared → checked` requires the deferred machinery to exist. For `spec.md`
   that is two unbuilt lint checks (`spec_schema_violation`, `spec_notification_missing`); the vault
   cannot build module machinery.

So the honest vault-side action is *file upstream and wait*, which is what this filing is — but that
leaves the vault reporting `deferral_expired` on every lint run in the interim, for a condition it has
no authority to clear. **A finding the reader cannot act on is the alert-fatigue failure the tripwire
budget exists to prevent**, arriving through the enforcement machinery's own front door.

## Grounding

- `_meta/conventions/{frontmatter,spec,wiki-consolidation}.md` frontmatter vs
  `_agent/conventions/.baseline/{same}.md` — identical on all deferral fields including `review_after`.
- `_agent/lint-reports/2026-08-14-1336-lint.md` — `deferral_expired: []` with the note *"all 3
  review_after 2026-08-17 — 3 days out, not yet due; expect them to fire on the next sweep."*
- `_agent/upgrade-ledger.md:191` — 0.9.0 → 0.9.1 own-the-apply, 2026-08-02; bases refreshed to stock.
- `skills/vlt-mint/SKILL.md`, *Edit a convention* — the overlay-vs-base routing that closes road 2.

## What the vault actually observed, per convention

Offered as field data for whoever does the review, **not** as a recommendation — the dates are the
module's to set.

- **`wiki-consolidation@1`** — expiring on a genuinely clean record. `adoption_first_instance: null`;
  vlt-core has **never performed a consolidation**. Its metric (≥3 near-duplicates carried across 2
  consecutive sweeps) has read **0 on every sweep**; the 2026-08-14 run's three near-misses were all
  documented deliberate splits with written index filing rules forbidding the merge. Nothing has been
  learned that would justify promoting the stage — the deferral is expiring because time passed, not
  because the question ripened.
- **`spec.md@2`** — the metric is now attainable and reads 0 **honestly** rather than vacuously; see
  the companion filing `2026-08-14-142625-spec-blind-spot-statement-stale-after-adoption.md`.
- **`frontmatter@5`** — **the vault cannot evaluate half of this metric.** The threshold is *"2 drift
  findings, **or the 3rd new convention**."* The drift half is clean (0 frontmatter-drift findings in
  the last two lints). The convention-count half is **indeterminate from inside the vault**: vlt-core
  holds 9 conventions and gained `decision-log.md` at 0.9.0, but *the baseline count the threshold
  counts from is recorded nowhere the vault can read*. A vault-side check cannot evaluate a
  threshold whose origin is module-side. Flagging that as a general property of count-since-N metrics
  in shipped frontmatter, not just this one.

## Provenance guess — **marked as a guess**

I suspect these three dates were set together as a uniform ~3-week horizon at the 0.9.0/0.9.1 build
rather than derived per-convention from what each metric would plausibly take to trip — the identical
date across three conventions with very different adoption curves is the tell. I have not read the
build briefs and could easily be wrong; the factory's roadmap will know.

## Why it matters

This is the same **reachability** shape as `2026-07-29-120001-adoption-stamp-unreachable-beyond-mint.md`:
an axis was declared with a reporter but its writer sits somewhere the instance can't reach. Here the
*review* is the unreachable act — the deferral names a date and a metric, the vault surfaces the expiry
faithfully, and then there is no move the vault is permitted to make.

Candidate shapes, none argued for and all cheap to reject:

- **Overlay-writable `review_after`** — an authorized vault-local carry-forward, the way
  `adoption_first_instance:` already is (it has an explicit authority rule making the local stamp
  legitimate and is excluded from the base-divergence diff). The narrowest fix; makes the vault's own
  extension a first-class act rather than a divergence.
- **Per-convention dates derived from the metric** rather than one shared horizon, so three unrelated
  boundaries stop coming due in one alarm.
- **A distinct finding class for "expired, module-owned"** — so a vault can see the expiry without it
  reading as vault debt someone forgot.
- **Say the quiet part in the declaration**: state that a shipped deferral's expiry is reviewed
  upstream and that a vault's only move is to file. Costs nothing and makes today's dead end legible.
