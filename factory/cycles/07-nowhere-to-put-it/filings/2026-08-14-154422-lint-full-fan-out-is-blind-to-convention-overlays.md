# `vlt-lint-full.js` is blind to convention overlays — the fan-out judges every page against a base the skill itself says is incomplete

_Filed 2026-08-14 from **vlt-core**, during a `vlt-mint` convention-edit ceremony that created the
vault's first `frontmatter.overlay.md` and then asked whether the new rules would actually be seen.
Evidence is vlt-core + module source, read-only. Classification: **defect** — a shipped consumer
breaks the durability model's central invariant._

## The claim

The operating contract defines a convention as **the base file plus its overlay, merged on read**:

> Any reader of a convention reads the base, then applies its overlay if one exists. The convention is
> the base file *plus* its overlay, merged on read.

`vlt-lint/SKILL.md:17` implements that faithfully:

> Before applying any fix, JIT-read `{conventions}/frontmatter.md`, `{conventions}/wiki-supersession.md`,
> and `{conventions}/wiki-index.md` — read each together with its `{overlays}/{name}.overlay.md` if
> present, honoring the overlay's appended rules.

**Its own full-mode fan-out does not.** `.claude/workflows/vlt-lint-full.js` contains **zero**
occurrences of the string `overlay` (verified by grep against the installed copy). It accepts
`conventionsPath` and nothing else:

- line 22 — `conventionsPath: string   // LIVE abs path to {conventions}`
- line 62 — `const conventionsPath = a.conventionsPath`
- lines 77–78 — the required-args guard names `pages`, `indexPath`, `conventionsPath`; no overlays path
  is accepted, so none can be threaded to the per-page scanner agents (prompt at line 142) or the index
  linter (line 232).

So the skill honors overlays and the workflow it delegates to cannot. The invariant breaks precisely at
the scale it matters most: one agent per page, whole-corpus, which is the mode a vault runs when it
wants a definitive answer.

## Why this is worse than a missing feature

Two distinct failure modes, and the second is the nastier one:

1. **False negatives.** Any rule a vault adds by overlay is invisible to the full sweep. The vault
   believes the rule is watched; the sweep never had it.
2. **False positives against compliant pages.** A page written *correctly* under an overlay rule is
   judged by a scanner agent holding only the pristine base — which may say the opposite. In vlt-core
   today the overlay moves wiki `sources:` onto quoted wikilinks while base rule 4
   (`frontmatter.md:36`) says non-graph list fields hold bare paths. A converted page is compliant with
   the merged convention and looks malformed to the fan-out. `vlt-lint-full.js:95` has the scanner
   return `frontmatter_valid: boolean`, so this lands as a real finding, not a shrug.

The second mode punishes exactly the vaults that use the durability mechanism as designed.

## The ack claims coverage the asset does not implement

`vlt-lint/SKILL.md` carries `depends_on: ["frontmatter@5", …]`, and `frontmatter.md`'s own base-edit
ceremony says:

> A consumer's ack covers its own workflow assets (e.g. `vlt-lint-full.js`).

That ack is therefore asserting that `vlt-lint-full.js` has been reconciled against the frontmatter
convention — including the overlay-merge rule the contract states. It has not been. This is a small
governance point with a general shape worth flagging: **an ack that covers assets by declaration
rather than by inspection will drift silently**, because nothing re-reads the asset when the ack is
bumped.

## Provenance guess — marked as a guess

Likely simply that `vlt-lint-full.js` predates the overlay mechanism, or was written from the *checks*
catalog rather than from the skill's activation contract, and the overlay merge lives in the latter.
The fan-out threads exactly the paths its checks need (`pages`, `indexPath`, `conventionsPath`), which
reads like an argument list grown from the checks rather than from the convention-read contract. **I
have not read the module's git history and this is inference from the shipped file alone.**

Adjacent prior art, not a duplicate: `inbox/2026-07-26-124223-lint-has-no-memory-of-adjudicated-divergence.md`
names `baseline_missing` and `overlay_orphan` while filing a different signal (lint re-litigating
adjudicated governance divergence). The two would plausibly be captured in the same arc.

## Suggested fix

Thread an `overlaysPath` through `vlt-lint-full.js` and have each scanner agent merge base + overlay
before judging, mirroring `SKILL.md:17`. The scanner prompt (line 142) and the index linter (line 232)
both need it — the index linter reads `wiki-index.md`, which is equally overlay-able.

## What acceptance should check

Not "does it accept the argument" but: **a page compliant with an overlay rule that contradicts its
base survives a full sweep with no finding.** That is the case that fails today, and it is cheap to
fixture — vlt-core's `_agent/conventions/frontmatter.overlay.md` plus any wiki page converted to the
wikilinked `sources:` form is a ready-made pair.
