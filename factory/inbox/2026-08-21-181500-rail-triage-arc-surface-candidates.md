# Rail-triage residue on shipped surface — verdict-label widening, issue-form/filing-shape alignment, voice-rule single-homing

origin: (factory-observed; no issue — filed directly by the owner)

- **filed:** 2026-08-21 by the owner (via the factory clerk, owner-confirmed in-session),
  classification: **candidate batch** for a future arc (Arc 11+)
- **provenance:** the platform channel's P-1 build (`issue-triage`, factory skill,
  self-accepted 2026-08-21) hit the module-source boundary three times: each cut was
  correct for a platform item, and each leaves an arc-surface candidate that only a
  filing can put in front of capture. Design record: the 2026-08-21 brainstorm memlog +
  P-1's closed entry in `skills/reports/platform-roadmap.md`.

## Candidate 1 — widen the rail's verdict vocabulary (label set)

The field contract's label set (`field-contract.md:54-69`, `rail_contract: 1`) admits
only accept/decline as triage outcomes. P-1's grounded triage wanted three more shapes
and had to express them in comment prose: **needs-info** (a question to the filer, issue
stays `vault-filed`), **duplicate** (of an issue or an existing filing), and a
**decline-reason taxonomy** (out-of-scope / working-as-designed / upstream / superseded).
Prose works but is invisible to `gh` queries — a filer or a future declined-corpus grep
cannot scope by them. Widening the label table is a contract change on shipped surface
(evolution rule: label additions are additive, but the table is the single home three
surfaces derive from) — it belongs to an arc build with the consumer walk.

## Candidate 2 — issue-form fields 1:1 with the filing shape

The issue forms (`.github/ISSUE_TEMPLATE/`) already carry the contract's eight payload
fields, but triage still does archaeology the form could pre-structure: the shared
pattern/candidate form cannot branch labels (noted in the contract's own label table),
and nothing in the form asks for the `file:line` grounding the factory will do anyway.
Candidate: evolve the forms so a filing arrives triage-ready (e.g. a
provenance-with-line-refs field, per-kind forms so `field:*` labels apply true at
filing). Shipped surface (`.github/` is the repo-side half of the field contract) —
arc work, additive under the evolution rule.

## Candidate 3 — single-home the public-voice rule

"The agent never writes to the public tracker unapproved" now exists twice: natively in
`vlt-feedback` (the approval gate section) and natively in the factory's `issue-triage`
skill. Two restatements of one rule is the exact drift shape the single-home discipline
exists to prevent, and any future rail-facing skill would make a third. Candidate: home
the rule once in the operating contract (the rail's durable doctrine host) and cut both
skills to pointers. Small, but it's operating-contract surface — arc work.

## Capture notes

- The three are independently shippable; 1+2 touch the same contract file and would
  naturally pair in one build with the `rail_contract` evolution-rule check.
- None is urgent: P-1 shipped working prose-level equivalents for all three; these are
  legibility/drift hardening, not gaps in function.
