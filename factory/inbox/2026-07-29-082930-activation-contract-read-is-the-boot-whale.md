# Every partner activation reads the full operating contract — ~10K tokens of self-described reinforcement

_Filed 2026-07-29 from the **factory**, prompted by a field signal: owner-observed token expense in
partner sessions on the work-machine consumer vault. Converged out of a token-efficiency ideation
session (`_output/brainstorming/brainstorming-session-2026-07-29-0804.md`, candidate C1); grounding
measured against module source at 9f05579. Owner elected to file (2026-07-29)._

## The claim

All three shipped partners open every activation with a full read of the operating contract —
**38,271 chars (~9–10K tokens)** — and the instruction itself declares the read redundant with the
skill's own content: *"First read the operating `{contract}` (the rules you obey; **also
internalized below — the read is reinforcement**)."* This is the single largest fixed cost of a
partner session, paid before any work happens, on every activation, in every vault, forever.

## Grounding

- `skills/vlt-agent-researcher/SKILL.md:22`, `skills/vlt-agent-librarian/SKILL.md:22`,
  `skills/vlt-agent-creative/SKILL.md:22` — the identical "two-beat ritual" opener; the contract
  read precedes both beats.
- `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md` — 38,271 chars.
- Contrast: **conventions are already lazy.** Every convention reference across partners and
  consumer skills is point-of-use (e.g. researcher `SKILL.md:56` — read `{conventions}/frontmatter.md`
  at end-of-sitting write time, deliberately *not* in activation reads). The module already knows how
  to defer governance reads; the contract is the one surface that predates that posture.

## Why it matters

- It is the boot whale: partner SKILL.md is ~10–11.5K chars; the contract read nearly quadruples the
  fixed boot before orient reads begin. Multiply by hand-offs and consults (filed separately —
  `2026-07-29-082931-*`) and one conversation can pay it several times.
- The skill's own text concedes the rules are "internalized below." What the full read buys beyond
  the skill's restatement is ceremony plus coverage of contract sections the skill does *not*
  restate — but nothing scopes the read to those sections.
- **Ceremony constraint (not incidental):** the identity ruling is *ceremony not sanctum* — the
  two-beat becoming ritual is load-bearing for partner identity. A fix must preserve the beat, not
  delete it. The question is what the partner *reads* during the beat, not whether the beat exists.

## Candidate dispositions (for capture to rule — not pre-empted here)

- **(a) Compiled contract digest.** vlt-setup/vlt-upgrade compile a rule-card digest of the contract
  at apply time (derive-first — build-time compilation, never runtime summarizing); activation reads
  the digest, full contract stays available by pointer for on-demand sectional reads. Regenerate
  whenever the contract changes (the apply step already owns that moment). Preserves the ceremony
  beat at a fraction of the cost. Cost: a new derived artifact to keep honest.
- **(b) Sectional reads via a contract TOC.** No new artifact; the activation instruction names the
  sections a partner must read (or the contract grows a short front-matter map). Cheaper to ship,
  but per-partner section lists are enumeration-shaped and could drift.
- **(c) Keep the full read, on purpose.** If the owner rules the full-contract read is
  identity-bearing ceremony worth ~10K tokens per activation, keep it — but then the cost is chosen,
  not accidental, and the lite paths (hand-off/consult, filed separately) matter more.

Preference, weakly held: **(a)** — it rides existing machinery (own-the-apply as compile point,
version-change as regeneration trigger) and keeps single-home intact (the contract stays the home;
the digest is derived, marked as such).

## Adjacent posture question (raised, not argued)

The ideation session surfaced a deeper trade the owner may want to rule on once, arc-level: how much
governance must be loaded *pre-hoc* versus enforced *post-hoc* by `vlt-lint`/review-council
(optimistic execution, cheap correction). That is a governance-guarantee trade, not an optimization,
so it is deliberately **not** a disposition here — but (a)/(b) sit on its spectrum and a ruling
would settle several filings at once.
