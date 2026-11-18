# `spec.md`'s blind-spot statement is stale — it says the metric "cannot fire at zero adoption," and adoption is no longer zero

_Filed 2026-08-14 from **vlt-core**, found while reviewing the three deferrals expiring 2026-08-17
(companion filing: `2026-08-14-142624-stock-deferral-dates-expire-with-no-vault-side-review-form.md`).
Evidence is vlt-core, read-only. Classification: **defect** — small, factual, in shipped prose._

## The claim

`_meta/conventions/spec.md@2`, *Enforcement*, ends with:

> **The deferral's blind spot, stated in its own text:** at zero adoption the `deferral_metric` cannot
> fire — "spec version bumps shipping without their relay entries" presupposes a spec that exists, so
> its only attainable value is "fine" — which means it measures **notification discipline once specs
> exist, never adoption itself**.

That was true when written. It is no longer true, and the same file says so four lines up in its own
frontmatter:

```yaml
adoption_first_instance: 2026-06-13 — _agent/specs/2026-06-13-health-coach-to-chef-nutrition-spec.md
```

Adoption is non-zero. Two live specs sit in `_agent/specs/`. The metric's precondition — *a spec that
exists* — is satisfied, so "its only attainable value is fine" no longer holds.

## What the metric actually reads, checked rather than assumed

**It reads 0, and for the right reason.** I checked rather than inferring it from the stale statement,
which is the whole point:

- `_agent/specs/2026-06-13-health-coach-to-chef-nutrition-spec.md` is at **`version: 2`** — the vault
  has had exactly one spec version bump, `last_updated: 2026-06-27`.
- That bump **did** ship with its relay entry: `_agent/dispatch.md:88`, `## [2026-06-20 10:36] relay:
  health-coach → chef`, announcing *"nutrition spec **revised**… calories 2,400 → ~2,150, protein floor
  raised 135 → 150 g…"*, with a second follow-up relay at `:132` (2026-06-27).
- The other spec is at `version: 1` — never bumped.

So: **one bump, notified. Metric = 0. Threshold = 1. Not tripped.**

The correction is therefore to the *statement*, not to the vault's state — but it is worth making,
because a disclaimer saying a metric is structurally incapable of firing is exactly the thing a future
reviewer trusts instead of checking. Had the bump gone un-notified, the standing text would have argued
against looking.

**One wrinkle worth recording.** Both relay entries point at
`_agent/handoffs/2026-06-13-health-coach-to-chef-nutrition-spec`, not the `_agent/specs/` path — because
at bump time (2026-06-20) only the handoff existed; the spec was produced later by the proto-spec
retrofit and inherited the name. Substantively the notification discipline was honored. But a
mechanical `spec_notification_missing` check keyed on the **spec path** would score this bump as
un-notified and trip on a false positive. Worth knowing before that check is built — it is one of the
two deferred checks `spec.md` names.

## Grounding

- `_meta/conventions/spec.md` — *Enforcement*, final paragraph (the stale statement); frontmatter
  `adoption_first_instance:` (the fact contradicting it).
- `_agent/upgrade-ledger.md:196` — the stamp was backfilled by user ruling at the 0.9.0 → 0.9.1 upgrade,
  first exercise of the merge-not-replace carry-forward rule in this vault.
- `_agent/specs/*.md` frontmatter; `_agent/dispatch.md:88,132`.

## Provenance guess — **marked as a guess**

The statement reads like it was written at the same build that declared the adoption axis, when
`spec.md` still shipped `adoption_first_instance: null` and no vault had stamped it — i.e. it was
accurate for the shipped default and went stale the moment the *first* vault backfilled the stamp. If
so, the class of defect is **prose asserting a permanent property that a frontmatter field can
invalidate**, and `spec.md` may not be the only place it appears. I have not audited for others.

## Why it matters

Small in itself; the shape is the point. `vlt-lint`'s honest-reporting discipline exists because a bare
zero is unreadable without its denominator — and this is a shipped convention supplying a *wrong*
denominator ("this can never fire") that a reader would reasonably accept in place of checking. The
enforcement kit's own credibility rests on its disclaimers being as current as its counters.

Cheapest fix: replace the paragraph with the conditional form it should always have had — *while
adoption is zero this cannot fire; once a spec exists it measures notification discipline, never
adoption itself* — which is true in both regimes and never goes stale.
