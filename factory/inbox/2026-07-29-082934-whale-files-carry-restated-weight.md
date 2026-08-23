# The three whale files (lint 41K, dispatch 38K, contract 38K) — editorial weight and load scope

_Filed 2026-07-29 from the **factory**, prompted by a field signal: owner-observed token expense in
partner sessions on the work-machine consumer vault. Converged out of a token-efficiency ideation
session (`_output/brainstorming/brainstorming-session-2026-07-29-0804.md`, candidate C5); grounding
measured against module source at 9f05579. Owner elected to file (2026-07-29)._

## The claim

Three files account for ~116K of the module's ~267K shipped skill chars, and each is loaded whole
whenever its surface is touched:

- `skills/vlt-lint/SKILL.md` — **41K**, and its run modes reference **7 of 8 conventions**, making a
  full lint the single heaviest possible invocation in the module (41K + up to ~70K of conventions).
- `skills/vlt-dispatch/SKILL.md` — **38K**, loaded in full even when the call is one `consult` or a
  `ledger` glance; four modes' mechanics ride in one file.
- `vault-operating-contract.md` — **38K**, read at every partner activation (own filing,
  `2026-07-29-082930-*`; here it counts as editorial surface).

The claim is **not** that these files are bloated by negligence — single-home discipline is largely
holding (lint already JIT-reads conventions before fixes, `SKILL.md:17`; dispatch delegates consult
protocol to the engine, `SKILL.md:207`). The claim is that at this size, *structure* is now the
lever: whole-file loading of multi-mode skills, and worked examples/pedagogy inline with rules,
charge every invocation for content most invocations don't use.

## Grounding

- Sizes: `wc -c` at 9f05579 — lint 41,202 / dispatch 38,285 / contract 38,271; all skills Σ267,254.
- Lint's convention span: `vlt-lint/SKILL.md:17,53,57,60,69,72,75,78,79,80` — frontmatter,
  wiki-supersession, wiki-index, write-verification, spec, extraction, consult all appear across its
  tiers/modes.
- Dispatch's four modes in one file: `vlt-dispatch/SKILL.md:54` (mode dispatch), `:75` (daily
  watermark mechanics), `:203` (consult mechanics) — a `consult` caller carries `daily`'s watermark
  prose and vice versa.
- The conventions bundle carries the same inline-pedagogy pattern at smaller scale
  (`frontmatter.md` 22.4K is the whale there) — same lever, same disposition space.

## Why it matters

Fixed cost, paid on the module's hottest paths (every lint run, every dispatch call, every partner
activation), and it compounds with the other filings' costs in the same context window. Progressive
disclosure is also the direction the surrounding skill ecosystem already treats as canonical for
large skills: thin SKILL.md router, depth in on-demand reference files.

## Candidate dispositions (for capture to rule — not pre-empted here)

- **(a) Per-mode/per-tier progressive disclosure.** Dispatch: SKILL.md keeps identity + mode
  dispatch + the shared pointer-line contract; each mode's mechanics move to a reference file loaded
  on mode entry. Lint: same shape per run mode/tier, and a scoped run loads only the conventions its
  scope touches (a frontmatter-only lint has no need of `spec.md`). Biggest structural win; the
  cost is more files and cross-file agreement to keep lintable.
- **(b) Editorial pass under a word budget.** Hunt restated mechanics (single-home violations are
  now token bugs too) and move worked examples out-of-line to pointer-referenced files across the
  three whales + `frontmatter.md`. Smaller win, no structural risk, composable with (a).
- **(c) Contract-specific: fold into the digest disposition** of `2026-07-29-082930-*` — if a
  compiled digest ships, the contract's inline weight stops taxing activations and its editorial
  urgency drops to (b)-level.
- **(d) Measure first.** Let the load-manifest instrument (`2026-07-29-082933-*`) size per-mode
  actual loads before choosing (a)'s cut lines.

Preference, weakly held: **(b) soon** (safe, composable), **(a) briefed against (d)'s numbers** —
cut lines chosen from measured per-mode loads, not guessed.
