# `local_metrics:` cannot express a content-filtered count — the exact derive class issue #1 lost has no vault-local home

_Filed 2026-08-23. Evidence: the attempted B10-4(4) discharge in vlt-core (session
vlt-core-d4, no commit — the declaration was honestly refused), factory-grounded
against module source (`skills/vlt-setup/assets/hooks/vlt-vitals.py:251`).
Classification: **defect** (an acceptance check no vault of this shape can discharge)
carrying a **pattern** (the silent-supersession contributing cause). Provenance: the
B10-4(4) BLOCKED grade — this filing is its rubric-mandated routing._

## The bound

B10-4 shipped `local_metrics:` as the durable vault-local metric home, bounded to
three kinds — `LOCAL_METRIC_KINDS = {"file_count", "bytes", "days_since_newest"}`
(`vlt-vitals.py:251`), locators pure glob/path with **no content predicate**
(`file_count` is `sum(1 for f in vault_root.glob(spec) if f.is_file())`).

vlt-core's lost derive — the metric B10-4's own acceptance check names — is
`pages_with_review_after`: the count of wiki pages whose **frontmatter carries**
`review_after:`. It is the denominator for the canonical `expired_pages`; without it
`expired_pages: 0` is ambiguous between *nothing is stale* and *nothing carries the
key* (the M0 audit said exactly this in 2026-07). A key-filtered count has no kind:
declaring it as `file_count` over `{wiki}/**/*.md` counts all pages and labels them
key-carriers — a fabricated metric. The registry header's own text agrees: "a derive
beyond those kinds has no vault-local home; its route is an upstream filing." This is
that filing.

Consequence: **B10-4(4) is BLOCKED for any vault whose lost derive was
content-filtered** — which is the shape issue #1 itself describes.

## Candidate directions (for capture, not answered here)

1. A content predicate on `file_count` — an optional `matching:`/`frontmatter_key:`
   filter on the glob (smallest change; keeps the bounded-kinds posture).
2. A fourth bounded kind (`frontmatter_key_count` or similar).
3. Promote `pages_with_review_after` to the canonical `METRICS` table — it is the
   natural denominator for a metric the module already ships, and the honest-reporting
   rule ("state the denominator") argues it belongs beside `expired_pages` regardless
   of what happens to the kinds.

Directions 1/2 solve the class; direction 3 solves this instance and is defensible on
its own merits. Not mutually exclusive.

## Contributing pattern: the silent supersession

The loss mechanism was **not** an upgrade clobber. vlt-core never hand-edited
`vlt-vitals.py` (4 commits, all upgrades; ledger entries at 0.12.0/0.13.0/0.14.0 each
confirm no local edit overwritten). The vault's pre-module `_agent/vitals.sh` (6
derives) was superseded by the shipped hook at 0.9.0; five derives carried into
canonical `METRICS`, `pages_with_review_after` did not, and **no divergence report
named the drop** — supersession-at-install has no analogue of the divergence net that
guards upgrades. A vault-authored derive could disappear with no artifact naming it.
Worth a look whether install/first-provision owes a "superseded local instrumentation"
report line; held here as context rather than a second filing.
