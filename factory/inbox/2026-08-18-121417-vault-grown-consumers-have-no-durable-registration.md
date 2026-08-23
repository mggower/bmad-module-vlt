# A vault-grown op has no durable way to register as a convention consumer — the only compliant home is invisible to the machinery that would enforce it

_Filed 2026-08-18 from **vlt-core**, surfaced by a `vlt-mint` convention-edit ceremony that reverted two hand-edited pristine bases, and by the four-lens review council that gated it (`revise`, ten named changes). Every claim below is verified against vlt-core's disk, not inferred. Classification: **defect** — a hole in the durability model's consumer-registration path, with four consequent defects and one preferred fix._

## The claim

A vault that mints its own write op (vlt-core has two: `vlt-sweep`, `vlt-file-feedback`) has **no durable, compliant way to register it as a consumer of a shipped convention**. Both available moves fail, in opposite directions:

| where the registration can go | what happens |
| --- | --- |
| the base's `consumers:` line | durable-by-nothing — it is a hand-edit to a pristine base, re-applied by hand at **every** upgrade |
| the overlay's `consumers:` line | durable by location, but **structurally unreadable** by the coherence check that gives registration its only meaning |

The base path is a treadmill and the overlay path is decorative. There is no third move.

## This is not hypothetical — it ran for three months and cost an upgrade reconcile

`vlt-sweep` was minted 2026-08-15 as a vault-grown heavy capability. Its mint registered it in the `consumers:` lines of **two pristine shipped bases** — `frontmatter.md` and `write-verification.md` — recorded in the vault's decision log as "roster bookkeeping, no rule change." That was the only move available.

At the 0.10.0 → 0.11.0 upgrade (`_agent/upgrade-ledger.md`, 2026-08-17) the treadmill ran exactly as the model predicts. The pre-flight had to detect both edits, classify them as authorized-not-hand-edit, refresh the bases, and **re-apply both** — and for `frontmatter.md` this was a **both-moved-line reconcile**, because upstream had independently edited the same `consumers:` line (v7→v8, `+vlt-setup`, `+vlt-groom`). The correct result was reached, by hand, on a line two parties had moved. That is a merge conflict manufactured by the absence of a registration mechanism, and it recurs at every upgrade forever.

**Worth stating plainly:** nothing was silently lost, and the vault's own backlog item claiming "the next upgrade will silently revert it" was **wrong**. The upgrade machinery worked. The defect is that it should never have had to.

## Finding 1 (primary) — the base names no carve-out for a vault-grown consumer

The operating contract permits an overlay to occupy "a carve-out the base names in its own words," and rules that "an overlay claiming a carve-out the base never cut is a base-rule change in disguise."

`write-verification.md` §Attestation declares its `verified_by` value set as a **flat closed enumeration** — "the three write ops (`vlt-ingest`, `vlt-extract`, `vlt-research`) plus `vlt-lint`" — cutting **no** delegation clause. So when `vlt-sweep` writes `verified_by: vlt-sweep` (its own Verify step instructs it to; four issues under `_agent/research/sweeps/` already carry it), the value is written by the op's own contract and sanctioned by nothing.

vlt-core's council **split** on whether an overlay may extend that set: the architect argued legality on **monotonicity** (every base sentence stays true after the merge); the skeptic and historian read the contract's own test as unsatisfied, the historian noting three entries declined on that exact ground four days earlier. The vault adopted the extension on the user's ruling and **recorded the legality as unsettled** rather than claiming a carve-out it does not have.

A module cannot leave a live install in that position. **The base should name the carve-out in its own words** — one delegation clause is enough to make the whole class legal by construction instead of by generous reading.

### The preferred fix — `local_consumers:` as a vault-writable declared field

Better than blessing the overlay path: **declare a `local_consumers:` field vault-writable on the base itself.** The mechanism already exists and is already sanctioned — `frontmatter.md` *Vault-writable declared fields* names `adoption_first_instance:` and `review_after:` as a live member set, values a vault writes **into a pristine base** without it counting as divergence; the base-divergence surfaces exclude declared fields, and the upgrade's refresh carries local values forward.

Adding `local_consumers:` to that member set retires the treadmill **and keeps the coverage** — the name sits in the base where the coherence check already looks, and the upgrade carries it rather than re-applying it. It trades nothing. It is the only proposal here that resolves the defect without the vault accepting a loss. (Raised by the architect lens; unreviewed by the other three — filed as a proposal, not as panel consensus.)

## Finding 2 — an overlay `consumers:` line is unreachable by the coherence check

The fallback path is decorative, and the shipped text says so:

- `vlt-lint/references/checks.md:36` — the coherence check iterates "each `{conventions}/*.md` carrying a `version:` and `consumers:`". Overlays live in `{overlays}`.
- `vlt-lint/references/checks.md:42` — overlays are "**deliberately unversioned** vault-local additions carrying no handshake axis; an overlay addition is invisible to the version handshake **by design**."

So a consumer registered only in an overlay is never walked. The **larger** consequence is the quiet one: the stale-ack alarm keys off the base `consumers:` roster, so once a vault moves its registration to the overlay, **a future shipped `frontmatter@9` will never flag that consumer's pin as stale** — silently, indefinitely, with the next version bump as the trigger.

vlt-core accepted this trade knowingly and stated it as determined fact in both overlays rather than hedging it. But it is a real coverage loss, taken only because the alternative was an unbounded treadmill.

**Live proof it matters, found during this very mint:** `vlt-sweep` was pinning `frontmatter@7` against a base at `version: 8` — a genuine stale-ack finding, flaggable **only** because `vlt-sweep` sat in the base `consumers:` line the mint was about to revert. Reverting first would have buried a live finding. It was reconciled and bumped to `@8` before the revert. Under the overlay path, that class of finding is undetectable.

## Finding 3 — `frontmatter.md` restates a closed enumeration `write-verification.md` owns

`frontmatter.md:82` states: "The legal value set is the three write ops plus `vlt-lint`." `write-verification.md:47` states the same set. But the two files declare a clean division of labor — `frontmatter.md` "defines only the **fields**"; `write-verification.md` §Attestation "owns the contract around them."

The value set is contract, not field schema, so the `frontmatter.md` sentence is a **duplicated definition of a rule another file owns** — a single-home violation in the governance bundle itself. Its practical cost is immediate: a vault that correctly overlays the extension onto the owning file gets an **internally inconsistent merged reading** — merged `write-verification` says `vlt-sweep` is legal, merged `frontmatter` still says it is not. vlt-core resolved it by ownership (the owner wins) and documented the inconsistency; the fix is for `frontmatter.md` to point rather than restate.

## Finding 4 — one enforcement declaration per file, but overlay content is per-section

`frontmatter.md` *Enforcement declaration* is a set of **flat, file-level keys**. An overlay accretes **sections**, each potentially with its own enforcement posture.

vlt-core's `frontmatter.overlay.md` now holds Rule A (prose not hard-wrapped, `declared` + a deferral scoped to hard-wrapped paragraphs), a retired §B, and a new §C (consumer roster bookkeeping, obliging no one). §C is honestly declarable only because it needs **no** bell — it rides the file's single declaration and states explicitly that it falls outside Rule A's `deferral_metric`. **The next genuinely rule-shaped addition to that file cannot be declared honestly at all**: it would need its own stage and deferral, and there is one slot, already spent.

Per-section-addressable enforcement is needed before that addition arrives — otherwise the schema's own honesty requirement forces either a false declaration or a rule with no bell.

## Finding 5 — no bell in `{overlays}` can ever ring

This one closes the loop, and it means a vault **cannot** self-remediate findings 1–4 by declaring a careful deferral.

- `vlt-lint`'s enforcement-doctrine meta-check walks `{conventions}/*.md` only (`checks.md:37`). So `deferral_expired`, `declared_untripwired`, and `deferral_invalid` **cannot fire on a file in `{overlays}`** — a `review_after:` in an overlay sits in a file no checker opens.
- The `{tripwires}` registry cannot cover it either: a wire's `metric` must name an id from the canonical table in `.claude/hooks/vlt-vitals.py`, and **no id in that table can express an overlay-hosted deferral**. Adding one means editing a shipped module file — the exact treadmill this filing is about.

So the module's own doctrine — *no boundary without a bell* — is unsatisfiable for any rule that lands in an overlay, which is precisely where the durability model sends vault-local additions. vlt-core shipped both overlays with schema-complete deferrals and **stated in the files that nothing reads them**, because the alternative was to imply a mechanism that does not exist. Standing precedent that this class of bell is silent: `frontmatter.overlay.md`'s `review_after: 2026-11-14`, declared 2026-08-14, read by nothing since.

## What vlt-core did in the meantime

Reverted both bases to shipped byte-state (md5-verified against `{overlays}/.baseline/`); moved both registrations into `{overlays}/write-verification.overlay.md` §C and `{overlays}/frontmatter.overlay.md` §C; sanctioned `verified_by: vlt-sweep` in write-verification's overlay §D, **narrowed to the single op name** with the generative membership test demoted to stated admission criteria (a self-executing test would let a skill mint silently confer convention membership with no convention edit and no council); bumped `vlt-sweep`'s ack to `frontmatter@8` before the revert; and marked the 2026-08-15 mint entry's registration clause **superseded-in-part**, so `vlt-upgrade`'s pre-flight cannot read a still-live authorization to restore the base edits it just reverted.

Full record: `_agent/mint/decision-log.md`, entry `[2026-08-18] convention-edit`; plan `_agent/mint/2026-08-18-write-verification-sweep-overlay.md`.

## Bonus — an instrument note worth shipping

The vault-side investigation nearly missed the divergence: a plain `diff` reported "Files are identical" while `md5` disagreed. The cause is a local shell hook rewriting `diff` → `rtk diff`, which prints an `[ok] Files are identical` summary rather than a byte comparison. Not a module defect, but if any module doc or skill instructs a base-vs-baseline comparison, it should specify **checksums or a real line differ**, never bare `diff` — a wrapped `diff` fails toward "no divergence," which is the dangerous direction.
