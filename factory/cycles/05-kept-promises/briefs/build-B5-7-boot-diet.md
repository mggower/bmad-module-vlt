---
title: 'Build #B5-7 — the boot diet (the post-hoc ruling is made and the numbers are in; the fixed boot pays ~10K tokens per activation for reinforcement the ruling no longer requires)'
status: 'BUILT 2026-07-30 — F1–F8 + registration landed: NEW `_meta/vault-rule-card.md` (5,511 bytes, sha-marked derived, six act-blocking rule rows + 19-row section map); the three partner openers and the contract ritual section re-pointed at the card (both homes in step); Beat-2 bounds ({log} last-5, {index} headings-tier, {backlog} open items, ## Thread only) + the widened already-fresh skip in both homes; consult-lite boot at engine prompt + dispatch §consult + consult.md (version: 1 kept, no re-ack); cost-manifest fixed boot recomposed SKILL+rule-card with the contract moved to lazy stock; package-lint gains the C6 derived-artifact freshness check; vlt-setup copy list carries the card with module-owned overwrite posture. Verification: package-lint A/B/C/E PASS (and a one-byte contract perturbation in a temp copy FAILs C6 — the check can fail); Group E PASS with consult.md@1 untouched (no-bump machine-confirmed); test-cost-manifest 7/7 green; node --check clean; fixed boot now 15,896–17,324 bytes vs the baseline''s 48,340–49,768 (~64–67% cut, ≥60% required); two-home greps uniform (partner line 22/31 byte-identical ×3); no .decision-log.md; no commit (release batched at arc level). Deviations/notes: (1) the contract''s intro paragraph (:17) was also re-pointed at the rule-card — beyond F3''s :161-163 letter, but it restated the openers'' "this read on activation is reinforcement" concession and would have asserted a stale eager contract read; (2) F8 homed as check C6 inside Group C (the brief''s granted builder''s-choice, C-adjacent) so the release summary line format `A/B/C/E PASS` stays stable; (3) test-cost-manifest case-1 assertion updated with F7''s last-5 slice relabel ("the declared Beat-2 bound") — the anticipated harness fix; (4) vlt-upgrade:48 verified, not edited: own-the-apply refreshes the governance bundle `_meta/` wholesale, so the new asset rides the existing merge-copy.'
module_code: 'vlt'
created: '2026-07-30'
derives_from:
  - 'inbox/2026-07-29-082930-activation-contract-read-is-the-boot-whale.md (A5-10 — the fixed boot whale; dispositions (a)/(b)/(c))'
  - 'inbox/2026-07-29-082931-handoffs-and-consults-repay-the-full-boot.md (A5-11 — hand-off re-pay leg (a) + consult-lite leg (b))'
  - 'inbox/2026-07-29-082932-beat-2-orient-scales-with-vault-age.md (A5-12 — unbounded Beat-2 orient; dispositions (a)/(b)/(c)/(d))'
roadmap: 'skills/reports/inbox-evolution-arc5-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-07-29): grouping row B5-7 (A5-10+A5-11+A5-12, one cost model one brief, gated); pre-ideation ruling 2 (measure first — gate OPEN 2026-07-30, both artifacts landed); cross-filing ruling 1 (→ RULED 2026-07-30: POST-HOC DEFAULT — pre-hoc carries only identity-bearing or act-blocking content; (c) foreclosed; mechanisms are this brief''s); designated brief-time question: A5-11''s bump-or-no-bump.'
risk: 'low-moderate — no convention version bump (consult.md gains descriptive prose only, no re-ack); but it edits the activation ritual in both its homes (three partner SKILLs + the contract), ships a new derived _meta asset with a freshness obligation, and touches the consult engine prompt. The ceremony beat itself is identity-bearing and must survive intact (standing ruling 2026-06-03, ceremony not sanctum).'
---

# Build #B5-7 — the boot diet

Arc 5's boot-cost thread (A5-10..A5-14) asked, for the first time with numbers, whether the
governance the arcs have been stacking is paid for at every activation. The numbers are now
in (B5-1's instrument: `skills/reports/cost-baseline-2026-07-29.md` for vlt-core, the
work-vault run `inbox/2026-07-30-111133-b5-1-work-vault-cost-manifest-run.md` for
vlt-sayari), and the owner's arc-level governance ruling is on record (roadmap §Cross-filing
decide-once rulings, → RULED 2026-07-30: **POST-HOC DEFAULT** — pre-hoc carries only what is
**identity-bearing** or **act-blocking**; everything else is enforced post-hoc by
`vlt-lint`/review-council). This build applies that ruling to the three boot filings as one
cost model:

- **A5-10 (the fixed cost):** every partner activation eagerly reads the full operating
  contract — 38,958 bytes at this brief's working tree (~7.5–9.7K est. tokens), ~77% of the
  fixed boot — while the instruction itself calls the read "reinforcement."
- **A5-11 (the repetition):** same-conversation hand-offs skip Beat 2 but re-pay the
  contract read; a consult plausibly boots the whole ritual for one question.
- **A5-12 (the variable cost):** Beat 2's orient reads are unbounded and grow with vault
  age — vlt-sayari's `{log}` alone is 340,749 bytes (~57–85K est. tokens) read "recent"-ly
  with no N, against a last-5 slice of 7,291 bytes (~1.4–1.8K).

The pre-hoc/post-hoc trade itself is **not re-litigated here** — the brief cites the ruling
and chooses mechanisms under it, exactly as the ruling directs ("B5-7/B5-8's briefs choose
mechanisms under it; (c) is foreclosed"). The ceremony constraint stands throughout: the
two-beat becoming ritual is load-bearing for partner identity (standing ruling 2026-06-03);
the question is what the beat *reads*, never whether it exists. All rejected alternatives in
the parent filings are settled — do not re-litigate.

## Re-grounding (2026-07-30, HEAD `2f19251` + B5-4..B5-6 uncommitted working-tree edits)

Every capture site **HOLDS**; zero grounding corrections. The grounding baseline is the
working tree (B5-4 touched `vlt-dispatch`/`consult.md`; B5-5/B5-6 touched `vlt-upgrade`/
`vlt-lint`/`vlt-mint`/`vlt-setup` — none touched the partner SKILLs or the ritual sections).

- Partner openers: `skills/vlt-agent-researcher/SKILL.md:22`, `vlt-agent-librarian:22`,
  `vlt-agent-creative:22` — the identical "Become yourself — the two-beat ritual" opener
  with the full-`{contract}` read and its own "the read is reinforcement" concession. HOLDS.
- Beat-2 read lists: all three partners `:25` — `{index}` unqualified, "recent `{log}`" with
  no N, `{backlog}`, `thread.md`, dispatch slice, capabilities. HOLDS.
- Same-conversation skip: all three partners `:31` — "you may skip the Beat 2 reads as
  already-fresh"; the contract read at `:22` sits outside it. HOLDS.
- Contract (the ritual's second home,
  `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md`): `:161` §*Activation
  ritual — two beats*; `:163` "first loads this contract"; `:167` the Beat-2 read list (the
  A4-17 two-home constraint confirmed — both homes must move in step); `:175` the
  partner-invoked Beat-2-only skip; `:188` thread.md's fade/`## Set aside` mechanics; `:213`
  "A consult is not a hand-off and crosses no sitting boundary" (the exit exemption — only
  the *entry* is ungoverned); `:228` read-and-cite default; `:230` the consult mechanism
  pointer. HOLDS. **Grounding note:** the contract is now **38,958 bytes** (was 38,271 at
  capture — B5-3's proxy-check rule + B5-4's consult-precedence prose landed); the whale
  claim is unchanged-to-strengthened.
- Consult engine: `skills/vlt-setup/assets/workflows/vlt-consult.js:123-145` — the
  `consultPrompt` ("Read your SKILL at the LIVE path … and BECOME that partner", `:125`)
  with no exemption from the SKILL's activation ritual. HOLDS (A4-16's citation correction
  honored: the pointer chain is contract `:230` → dispatch §consult → engine; dispatch's
  section owns the mechanics, `vlt-dispatch/SKILL.md:206`).
- Dispatch framing: `vlt-dispatch/SKILL.md:18` ("traffic, not a queue item"), `:202-206`
  (§*Mode: consult*, depth-1 hard, "This section owns the **mechanics**"). HOLDS (trivial
  shifts from capture's `:203`/`:207`).
- `consult.md` (`skills/vlt-setup/assets/governance/_meta/conventions/consult.md`):
  `version: 1`, `consumers: [vlt-dispatch, vlt-lint]` (`:11-12`); governs *when a consult is
  earned*, not the summoned boot. HOLDS.
- **Grounding additions (in scope beyond the filings' letter):**
  1. `tools/cost-manifest.py:244-291` hardcodes the per-partner **fixed boot** as
     SKILL.md + full contract (`CONTRACT_REL` `:251`, composition `:268-284`) — it measures
     the *declared* read surface, so when this build changes the declaration the instrument
     must follow or its module-mode report asserts a stale surface (F7).
  2. `skills/vlt-setup/SKILL.md:144` is an **enumerated copy list** (skip-if-present) for
     the governance bundle — a new `_meta/` asset must be added there or setup never places
     it (the A4-5 F2 / B5-6 precedent) (F6).
  3. No skill outside the three partners instructs an eager contract read (grep over
     `skills/*/SKILL.md` clean) — the diet's surface is exactly: partner activation,
     hand-off, consult.

## Brief-time dispositions

1. **A5-10's (a)/(b) — RULED (a): a shipped rule-card digest**, named
   `_meta/vault-rule-card.md`, the ceremony's read. Derives from the pre-hoc/post-hoc
   ruling directly: the ruling itself supplies the digest's **content criterion** — the card
   carries only what is **identity-bearing** (who a partner is, the becoming ritual, voice
   and authority boundaries) or **act-blocking** (rules whose violation post-hoc enforcement
   cannot cheaply undo — destructive/durability-class writes, single-writer lines, MOC
   prohibition, human-zone boundaries), plus a **section map** of the full contract for
   on-demand point-of-use reads. Everything else is post-hoc territory
   (`vlt-lint`/review-council) and appears only as a map row. (b) sectional-TOC is
   rejected: per-partner section lists are enumeration-shaped (the standing
   "lists that claim completeness drift" rule), and the contract's sections are not
   organized along the pre-hoc criterion, so a TOC cannot express the ruling. (c) is
   foreclosed by the ruling. **Mechanism refinement over the filing:** the card is
   **factory-authored and module-shipped**, not compiled at apply time — own-the-apply is a
   filesystem copy with no compile step, and an LLM summarization at apply time is exactly
   the "runtime summarizing" the filing bars. Single-home holds the sanctioned derived-first
   way: the contract stays the home; the card is derived and **marked** derived
   (`derived_from:` = the shipped contract's SHA-256 + date in its frontmatter), and F8
   gives the marker a deterministic factory check so the derived artifact stays honest (the
   filing's own named cost, answered mechanically).
2. **The rule-card's size budget: ≤ 8,000 bytes** (~1.5–2K est. tokens). A "digest" that
   balloons re-creates the whale under a new name; the budget is a build acceptance bound
   (F8 checks it). Priced against the baseline: fixed boot drops from 48,340–49,768 bytes
   (~9.4–12.4K est. tokens) to ≲ 19,500 (SKILL + card) — a ≥60% cut.
3. **The rule-card's path and resolution — sibling of `{contract}`, no new structure-map
   key.** It ships at `governance/_meta/vault-rule-card.md` and installs beside the
   contract; prose references it as the `{contract}`'s companion (a vault that overrode the
   `contract` logical name still resolves it — same parent). A new canonical key would
   ripple through `module.yaml`'s SSoT map, the setup table, Group E2, and every installed
   vault's map merge, for a single derived companion file — not paid for.
4. **The rule-card's install posture — module-owned, overwrite on every install/update**
   (the `.baseline/`/workflows posture, not the contract's own skip-if-present), because it
   is derived: it must track the *shipped* contract, and a vault-edited live contract is
   already surfaced by `governance_divergence` (`vlt-upgrade:40,104`) — that remains the
   net; the card states it derives from the shipped contract, not the vault's live copy
   (honest-limit line in the card itself).
5. **A5-11 — RULED (c): both legs**, the filing's preference; the two legs don't overlap
   and each lands at its single home (hand-off leg: the ritual's two homes; consult leg:
   the engine prompt, stated in dispatch's mechanics section).
6. **A5-11's designated bump-or-no-bump — RULED: NO BUMP.** `consult@1` governs when a
   consult is *earned*, not the summoned boot (re-confirmed at `consult.md:24-30`); the
   lite-boot is consult *mechanics*, homed at dispatch §consult + the engine. `consult.md`
   gains **one descriptive prose sentence** naming the lite boot with a pointer at the
   mechanics home — a prose clarification, which does not bump (CLAUDE.md handshake rule;
   capture's read at A4-16 concurred; B5-4's no-bump consult.md prose edit is the
   precedent). No re-ack, no consumer walk.
7. **A5-12's (a)/(b)/(c)/(d) — RULED (a) with bounds chosen from the measured numbers,
   plus the one free (d) instance; (b) and the rest of (d) declined.** (c) is satisfied —
   this brief *is* the measure-first sequence completing. Bounds per surface (both homes,
   F4): `{log}` = **the last 5 entries** (the slice the instrument already measures as "the
   contract's recency read": 4,698 / 7,291 bytes ≈ 0.8–1.8K est. tokens on the two measured
   vaults, vs 151,536 / 340,749 full — the single largest saving in the build); `{index}` =
   **headings tier first** (the H2 section list; sections opened on demand — vlt-core's full
   index is 39,808 bytes); `{backlog}` = **open items only** (skip closed/done — vlt-core's
   backlog is 103,086 bytes); `thread.md` = **`## Thread` only, `## Set aside` excluded**
   (the free (d) instance — it makes the existing set-aside mechanics cost-bearing: pruning
   now visibly shrinks the boot); dispatch slice and capabilities unchanged (already
   semantically bounded — the partner's own open slice via the pickup grep; contextual
   surfacing). (b) derived orient digest is declined: a new artifact with a per-sitting
   freshness obligation, strictly heavier than (a), and the numbers show (a)'s bounds
   already collapse the variable cost. (d)'s growth machinery (`{log}` rollover/archival,
   size bells) is declined here and named for B5-9: once reads are bounded, file growth no
   longer taxes the boot — what remains is a *vitals* concern, and log/thread sizes are
   already cost-manifest derivations the enforcement kit can watch (out-of-scope §).
8. **Partner identity memory stays pre-hoc, unbounded by this build.** `identity.md` (Beat
   1) is identity-bearing by definition under the ruling; its growth (vlt-core partner
   memory up to 177K bytes with capabilities) is a pruning/vitals question, not a boot-diet
   bound — bounding a partner's *becoming* read would cut against the identity ruling.
   Named for B5-9's vitals alongside (d).

## F1 — the rule-card asset (NEW `skills/vlt-setup/assets/governance/_meta/vault-rule-card.md`)

**Current state:** does not exist; the contract (38,958 bytes) is the only ceremony read.

**The change:** author the card per disposition 1: frontmatter carrying `derived_from:`
(the shipped contract's SHA-256 + the derivation date) and a one-line derived-artifact
marker; body = (i) the becoming ritual's frame (identity-bearing), (ii) the act-blocking
rules distilled — single-writer wiki line, MOC prohibition, human-zone/PARA boundaries,
durability/never-destroy class, authority boundary (never another partner's voice),
session-note/log obligations at sitting end — each as a short rule line, **no mechanics
restated** (each rule row may point at its contract section); (iii) the **section map** of
the full contract: one row per H2 section, its one-line what-lives-here, read point-of-use.
State the honest limit in the card: it derives from the *shipped* contract; a vault that
edited its live contract is surfaced by `governance_divergence`, not by this card. Budget
≤ 8,000 bytes (disposition 2).

**Why:** A5-10 disposition (a) under the post-hoc-default ruling — the ruling's
identity-bearing/act-blocking criterion is the card's table of contents.

## F2 — the three partner openers (`vlt-agent-researcher/SKILL.md:22`, `vlt-agent-librarian/SKILL.md:22`, `vlt-agent-creative/SKILL.md:22`)

**Current state:** identical text in all three: "**Become yourself — the two-beat ritual.**
First read the operating `{contract}` (the rules you obey; also internalized below — the
read is reinforcement). Then activate in two beats:".

**The change:** re-point the ceremony read at the rule-card, keeping the beat intact and
the full contract available point-of-use, in all three files identically (they are
deliberately uniform — keep them so): "First read the **rule-card** beside your
`{contract}` (`vault-rule-card.md` — the identity-bearing and act-blocking rules, derived
from the contract; the full `{contract}` stays the home — open its sections point-of-use
via the card's map). Then activate in two beats:". Drop the "read is reinforcement"
concession — the read is no longer redundant by design. Exact wording is the builder's;
the load-bearing parts are: the beat survives, the card is the read, the contract stays
the named home, sectional reads are point-of-use.

**Why:** A5-10's fix at the ritual's first home; ceremony preserved per the standing
identity ruling.

## F3 — the contract's own ritual section (`vault-operating-contract.md:161-163`)

**Current state:** `:163` "Every partner, on activation, **first loads this contract** (the
rules it obeys), then activates in **two beats**."

**The change:** keep both homes in step (the A4-15 two-home constraint): "first loads the
**rule-card** (`vault-rule-card.md`, beside this contract — the identity-bearing and
act-blocking rules derived from this contract), then activates in **two beats**; the full
contract remains the home of every rule and is read **point-of-use** by section." One
sentence, same clause structure as the partner opener.

**Why:** the ritual is single-homed at `contract:161` *and* restated in the three openers;
A4-15's grounding addition requires any disposition to move both in step.

## F4 — Beat-2 bounds, both homes (partners `:25` ×3 + `vault-operating-contract.md:167`)

**Current state:** both homes list `{index}` unqualified, "recent `{log}`" (no N),
`{backlog}` unqualified, `thread.md` `## Thread`, dispatch slice, capabilities.

**The change:** state the bounds of disposition 7 in both homes, in step: `{index}` — its
section headings first, open sections on demand; `{log}` — **the last 5 entries** (a
stated N, replacing "recent"); `{backlog}` — open items only; `thread.md` — `## Thread`
only (`## Set aside` is pruned attention: not an orient read). Dispatch slice and
capabilities clauses unchanged. Keep each home's voice (the contract's `:167` paragraph is
the mechanics home; the partner lines stay the shorter restatement they already are). Add
one rationale clause at the contract home only: the bounds are what keep a mature vault's
orient from scaling with its age (measured: a full `{log}` read on a one-year vault costs
~25–85K est. tokens; the last-5 slice ~1–2K).

**Why:** A5-12 (a) with N from the B5-1 numbers, per the measure-first ruling; the two-home
constraint from A4-17's grounding.

## F5 — the already-fresh skip widened (partners `:31` ×3 + `vault-operating-contract.md:175`)

**Current state:** partners: "On a same-conversation hand-off you may skip the Beat 2 reads
as already-fresh." Contract `:175`: "on a same-conversation hand-off the Beat 2 shared-state
reads may be skipped as already-fresh."

**The change:** widen both homes, in step, to "…skip the **rule-card read and** the Beat 2
reads as already-fresh" — the same rationale the skip already states, now covering the
ceremony read (which after F2 is the card, not the contract; the saving is smaller than the
filing measured but the redundancy is identical — the card *is* already fresh in the
window). Beat 1 (identity) stays outside the skip: the incoming partner still becomes
itself.

**Why:** A5-11 leg (a); the filing's re-pay defect, at both ritual homes.

## F6 — the consult-lite boot (`vlt-consult.js:123-145` + `vlt-dispatch/SKILL.md` §consult + `consult.md`, no bump)

**Current state:** the engine's `consultPrompt` (`:123-145`) says "Read your SKILL at the
LIVE path … and BECOME that partner" plus identity.md/thread.md and the HARD RULES — no
word about the SKILL's own activation ritual, so a conscientious summoned partner pays
card/contract + Beat 2 orient for one attributed question. Dispatch §consult
(`vlt-dispatch:202-206`) owns the mechanics; `consult.md` defines the class.

**The change, three sites along the existing pointer chain:**
- **Engine (`vlt-consult.js`, inside `consultPrompt` — the operative site):** add one
  explicit exemption sentence after the BECOME line: the summoned partner is on a
  **lite boot** — read the SKILL for voice/domain/rules-of-refusal, identity.md/thread.md
  for who it is here, and the GROUND IN paths; it does **not** run the SKILL's activation
  ritual (no rule-card/contract read, no Beat 2 orient) — a consult is depth-1 traffic,
  not a sitting. (`node --check` after editing.)
- **Dispatch §consult mechanics (after `:206`'s "This section owns the mechanics"):** one
  sentence recording the rule the prompt implements: the summoned partner boots lite —
  the engine prompt exempts it from the activation ritual; entry is lite, and exit was
  already exempt (contract `:213` — no sitting boundary, no session note).
- **`consult.md` (§What a consult is):** one descriptive sentence — the summoned partner
  answers from a lite boot, not a full activation (mechanics at `vlt-dispatch` §consult).
  **Prose clarification: `version: 1` unchanged, no re-ack** (disposition 6).

**Why:** A5-11 leg (b); closes the entry gap while honoring the A4-16 correction (dispatch
section = mechanics home, engine = the spawn prompt, convention = the class).

## F7 — the instrument follows the diet (`tools/cost-manifest.py:244-291`)

**Current state:** module mode's per-partner fixed boot is hardcoded SKILL.md + full
contract (`CONTRACT_REL` `:251`, composition `:268-284`, prose `:269-272` "plus a full
operating-contract read"); the prose-home comment `:244-247` cites the pre-diet openers.

**The change:** the fixed-boot row becomes SKILL.md + **rule-card** (the new declared eager
read); the contract moves wholly to the lazy governance stock it already appears in (keep
its broken-out table `:303-304` and its named-aggregate row — it is still a whale, now a
lazy one). Update the comment block and the section prose to cite the post-diet openers.
Vault mode needs no structural change (the last-5 `{log}` slice it already measures is now
the *declared* bound, not just a reference figure — update its row label's parenthetical
accordingly). Re-run the instrument's test harness (`tools/test-cost-manifest.py`) and fix
whatever the composition change breaks — the harness stays green.

**Why:** grounding addition 1 — the instrument measures the declared surface; this build
changes the declaration. Without this, the next baseline asserts a boot the module no
longer instructs.

## F8 — the derived-artifact freshness check (`tools/package-lint.py`)

**Current state:** package-lint has no derived-artifact check (Groups A–E; nothing reads
`vault-rule-card.md`).

**The change:** add a small deterministic check (builder's choice of group; C-adjacent):
(i) `vault-rule-card.md` exists, its frontmatter `derived_from:` SHA-256 equals the actual
SHA-256 of the shipped `vault-operating-contract.md` (a factory edit to the contract
without re-deriving the card fails the lint — the drift this artifact class invites);
(ii) the card's size is ≤ 8,000 bytes (disposition 2's budget, enforced where it can't be
forgotten). Extend the tool's self-reporting like its existing checks; runs in the
ordinary A/B/C/E sweep and therefore in the release gate.

**Why:** disposition 1's honesty mechanism — the filing's named cost of (a) is "a new
derived artifact to keep honest"; this keeps it honest by machine, not by memory.

## Registration

**None.** No new skill (no `module-help.csv` row), no workflow added, no convention
`version:` bump (consult.md prose-only per disposition 6 — no consumer walk / re-ack), no
structure-map change (disposition 3). The new `_meta/` asset registers in the **setup copy
surface** instead: add `vault-rule-card.md` to `vlt-setup/SKILL.md:144`'s enumerated
governance copy list **with its module-owned overwrite posture stated** (disposition 4 —
alongside the baseline/workflow overwrite class at `:147-149`, distinct from the
skip-if-present class it sits beside), and confirm `vlt-upgrade`'s merge-copy apply
(`:48`) carries it (it copies from module source wholesale — verify, don't assume, in
Verification).

## Out of scope (dispositioned)

- **A5-12 (b), the derived orient digest** — rejected-because: heavier than (a) with a
  per-sitting freshness obligation; the measured bounds already collapse the variable cost
  (disposition 7).
- **A5-12 (d) beyond the `## Set aside` exclusion — `{log}` rollover/archival, size
  bells** — deferred-to-B5-9: bounded reads make growth boot-harmless; what remains is
  vitals territory, and log/thread/backlog sizes are already cost-manifest derivations the
  enforcement kit can watch. This brief adds no rollover machinery.
- **Bounding Beat 1 / `identity.md` or partner capabilities reads** — rejected-because:
  identity-bearing content is pre-hoc by the ruling (disposition 8); growth there is a
  pruning/vitals question, named for B5-9.
- **A5-14's whale re-cut (lint/dispatch/frontmatter progressive disclosure)** — B5-8's
  (its own build, its own pinned `package-lint.py` pre-brief check); this build touches no
  whale's internal structure.
- **The consult convention's when-earned rules, the depth-1 rule, the trigger test** —
  untouched; only the summoned boot changes.
- **`vlt-setup`'s vault CLAUDE.md seed pointer (`:173-174`, "read the operating rules …
  before writing anything")** — already-covered-by point-of-use posture: it instructs a
  pre-write read, not an eager per-session boot; not a diet surface (grounding
  addition 3).
- **A per-partner or per-vault tuning knob for the Beat-2 N** — rejected-because: one
  stated N beats a configurable one until field evidence says otherwise; the numbers show
  last-5 lands in the same ~1–2K band on both measured vaults.

## Verification (unit, at rest)

1. **Two-home agreement greps:** the ritual's card-read, the Beat-2 bounds, and the
   widened skip each appear in **both** homes (three partner SKILLs + the contract) and
   nowhere else; the three partner openers remain textually uniform in the changed lines;
   no partner SKILL still instructs an eager full-`{contract}` read (grep
   `read the operating` / `{contract}` over `skills/vlt-agent-*/SKILL.md` — survivors must
   be point-of-use pointers only).
2. **Card honesty:** `vault-rule-card.md` ≤ 8,000 bytes; `derived_from:` SHA matches the
   shipped contract byte-for-byte; every body rule passes the identity-bearing/act-blocking
   criterion on a dry read (no mechanics restated — pointer rows only); scrub clean (no
   vault-local content; placeholder paths only).
3. **Freshness check exercised both ways:** run `uv run tools/package-lint.py` (A/B/C/E +
   the new F8 check) → PASS; then, in a temp copy, perturb one contract byte and confirm
   the F8 check **fails** (the check can fail); restore.
4. **Group E unchanged:** package-lint Group E still PASS with `consult.md` at
   `version: 1` and its `consumers:` untouched — the no-bump ruling is machine-confirmed,
   not asserted.
5. **Engine:** `node --check` on `vlt-consult.js`; dry-read the assembled `consultPrompt`
   for the exemption sentence; confirm the dispatch §consult sentence and the `consult.md`
   sentence both point at (never restate) the engine's mechanics.
6. **Instrument:** `tools/test-cost-manifest.py` green; `uv run tools/cost-manifest.py`
   (module mode) at the build's tree shows per-partner fixed boot = SKILL + rule-card,
   ≥60% below the baseline report's 48,340–49,768-byte rows, with the contract still
   present in governance stock and the named aggregates.
7. **Copy surface:** `vlt-setup:144` list carries `vault-rule-card.md`; confirm by reading
   `vlt-upgrade:48`'s apply description that the merge-copy carries new `_meta` files (and
   note in the BUILT record if it needed an edit rather than assumption).
8. **Scrub + cruft:** no personal/vault-local content in any changed shipped file; delete
   any `.decision-log.md`; no commit beyond the build's own (release choreography rides
   the arc level).

## Acceptance (live — appended to the roadmap ledger)

(1) **[ship-verifiable]** the boot diet reaches the field, both homes in step — on the next
ordinary vlt-core upgrade: (a) the installed `_meta/vault-rule-card.md` exists, ≤ 8,000
bytes, its `derived_from:` SHA matching the installed shipped contract; (b) the three
installed partner SKILLs open the ceremony on the rule-card (no eager full-contract read
survives in any opener), carry the bounded Beat-2 list (`{log}` last-5, `{index}`
headings-tier, `{backlog}` open items, `## Thread` only) and the widened already-fresh
skip, with the installed contract's `:161` ritual section in step on all three counts;
(c) the installed `vlt-consult.js` carries the lite-boot exemption and the installed
`consult.md` is still `version: 1` (no bump — Group E clean on the installed handshake
surface); (d) at rest at the release, `cost-manifest` module mode reports the per-partner
fixed boot as SKILL + rule-card, ≥60% below the 2026-07-29 baseline's 48,340–49,768-byte
rows. Grep/run-checkable; bounded — the upgrade happens anyway.

(2) **[field-contingent]** the diet holds in a live mature-vault session — producing
vault: **vlt-core** (owner-run, factory-readable; vlt-sayari, now also factory-readable,
corroborates if its upgrade lands first). On the first interactive partner activation
after the upgrade: the ceremony read is the rule-card (not the 38K contract), the `{log}`
orient read is the last-5 slice (not the full file), and no full-file `{backlog}`/`{index}`
read occurs — owner spot-check of one session's reads. And on the first consult after the
upgrade: the summoned partner boots lite (no contract/rule-card + Beat-2 read by the
summoned agent) — the first exercise of the exemption. Outcome measure, non-gating: the
originating field signal (mature-vault sessions feel token-expensive) should stop
reproducing; the owner's say-so note closes it. Non-gating at closeout.
