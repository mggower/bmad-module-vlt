# Nothing measures what a partner session loads — cost regressions are invisible

_Filed 2026-07-29 from the **factory**, prompted by a field signal: owner-observed token expense in
partner sessions on the work-machine consumer vault. Converged out of a token-efficiency ideation
session (`_output/brainstorming/brainstorming-session-2026-07-29-0804.md`, candidate C4); grounding
measured against module source at 9f05579. Owner elected to file (2026-07-29)._

## The claim

The module has no instrument — factory-side or shipped — that sizes what a partner session reads.
The originating field signal ("some vlt partner sessions are very expensive") arrived as a felt
impression, and this ideation round had to reconstruct the cost anatomy by hand (`wc -c` over module
source plus grepping activation instructions). Every companion filing in this batch proposes a
change whose benefit is a token number, and none of those numbers can currently be measured before
or after — so fixes can't be sized, and regressions (a convention that doubles, a log that grows,
a new mandatory read) accumulate with no bell.

## Grounding

Grounded in absence — verified by search, not by a site:

- No sizing/manifest tool in `tools/` (the factory toolchain is `package-lint.py`-shaped: release
  contract, not cost).
- No cost surface in `vlt-lint/SKILL.md`'s check tiers or report block, `vlt-track`, or the session
  note schema — nothing records what a sitting read.
- The by-hand baseline this batch established (module source at 9f05579): contract 38,271 chars;
  partner SKILLs ~10–11.5K; conventions bundle 86K (frontmatter.md 22.4K); largest skills lint 41K /
  dispatch 38K; all skills ~267K.

## Why it matters

- **Sequencing:** this is the filing the others depend on. The contract-digest, lite-boot, and
  orient-bounds filings each claim savings; without a before/after instrument those claims stay
  vibes, and the orient-bounds filing explicitly defers its bounds to "measure first."
- **The bell principle:** the module's own standing rule is *no boundary without a bell* — costs
  that can only regress silently, will. Token cost currently has no bell anywhere in the loop.
- It closes the field loop for this signal class: with a manifest, "partner X is expensive" arrives
  as a number in an ordinary filing instead of an impression.

## Candidate dispositions (for capture to rule — not pre-empted here)

- **(a) Factory-side static manifest tool.** A `tools/` script that, per partner/skill, resolves the
  declared read surface (SKILL.md + contract + point-of-use conventions + workflow assets) and
  prints chars→est. tokens. Ship-verifiable, zero field footprint, runs at release time next to
  `package-lint.py` — a cost regression gate. Cannot see field-variable reads (index/log/orient).
- **(b) Shipped session self-report.** A line in the end-of-sitting session note (or `{log}` entry)
  recording what the sitting read — sizes the field-variable half (a) cannot see. Cost: a schema
  touch (frontmatter convention consumers, handshake implications) and per-sitting overhead in
  every vault — the instrument itself must not become a tax.
- **(c) A lint mode.** `vlt-lint` grows a cost report tier that sizes the vault-side surfaces
  (index, log, conventions as installed). Lands in existing machinery, but lint is already the
  heaviest skill (companion filing `2026-07-29-082934-*`) — adding scope there cuts against that
  filing.
- **(d) (a) now, (b) only if field numbers are needed.** Static manifest first; it likely answers
  most of the sizing questions, and (b)'s schema cost is paid only if the variable half proves to
  matter.

Preference, weakly held: **(d)** — and whichever lands should run once against the work vault
before the other filings in this batch are briefed, so their dispositions are chosen against
numbers.
