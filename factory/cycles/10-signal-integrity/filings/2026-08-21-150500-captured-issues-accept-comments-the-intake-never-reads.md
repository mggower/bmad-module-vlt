# Captured issues accept comments the intake never reads — amendments have no route into the factory

origin: (factory-observed; no issue — filed directly)

- **filed:** 2026-08-21 by the owner (via the factory clerk, owner-confirmed in-session),
  classification: **defect** in the ingress loop (B9-5, first live exercise)
- **provenance:** a substantive comment landed on `mggower/bmad-module-vlt#1`
  (2026-08-21T14:45:55Z, from app-vault, properly stamped) carrying a second instance of
  the filed class and a scope choice for the fix — and nothing in the factory would ever
  have seen it. The owner happened to mention it in-session; the clerk hand-folded it into
  the A9-3 filing.

## The gap

The field contract's state flow (`vault-filed` → `vault-accepted` → `captured` →
closed-at-archive) has **no amendment channel**. `inbox-capture`'s github-intake Discovery
queries admitted-**open** issues and **excludes** any issue whose `origin:` token already
appears under `inbox/` — correct idempotence (A15(d)), but it makes a captured issue a
write-only surface: filers can comment (GitHub invites it — the issue is open by design
until archival), stamps and all, and the factory is structurally blind to it. The window
is long: an issue stays open across arcs until its build ships *and* passes acceptance.

## Design material for capture (not resolved here)

- **Re-triage label** — the cheap shape: a comment-bearing amendment is admitted by the
  owner applying a label (e.g. re-applying `vault-accepted`, or a dedicated `amended`);
  Discovery adds one query leg for captured+amended and folds the new comments into the
  existing filing (append, never re-materialize — the origin key already exists).
- **Comment-scan in Discovery** — heavier: read comments on all `captured` open issues and
  diff against a high-water mark. Costs a per-run scan and needs a stored watermark.
- **Contract text** — whichever ships, `field-contract.md`'s state-flow table gains the
  amendment verb, and the issue templates' additive-only note should tell filers whether
  comments reach the factory (today they silently don't — an honesty gap in the contract's
  own terms).
- The A15 design intent (nothing mandatory without owner admission) applies to amendments
  too: an unadmitted comment should cost the factory nothing.
