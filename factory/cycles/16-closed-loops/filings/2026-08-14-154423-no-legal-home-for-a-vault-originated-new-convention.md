# The durability model has no legal home for a vault-originated **new** convention subject — so the rule lands somewhere wrong and goes invisible

_Filed 2026-08-14 from **vlt-core**, surfaced by the review council during a `vlt-mint` convention-edit
ceremony (architect lens, unrebutted by the other three). Evidence is vlt-core, and the defect is
demonstrated by the very mint that found it. Classification: **defect** — a gap in the durability
model, not in any one convention._

## The claim

The durability model gives a vault two moves and no third:

- **Add to a shipped convention** → write `{overlays}/{name}.overlay.md`, append-only. Durable.
- **Change a shipped rule** → edit the base, bump `version:`, walk `consumers:`, file upstream.

Neither covers a vault that originates a convention **subject the module never shipped**. Every
available landing zone is non-compliant:

| where you could put it | what happens |
| --- | --- |
| a fresh file in `{conventions}` | no stock copy in `{overlays}/.baseline/` → `baseline_missing` |
| an overlay with no base | `overlay_orphan` |
| appended to an unrelated base's overlay | lands outside that base's declared scope |

The third is not a finding today, which is exactly why it is the one that gets chosen.

## This is not hypothetical — it happened in the mint that found it

vlt-core needed a **body-prose** rule: *a paragraph is one unbroken line; a newline is a semantic break,
never cosmetic* (Obsidian renders a single newline as a line break, so column-wrapped prose reaches the
reader as ragged stacks). There is no shipped convention on prose formatting. Taking the third row, it
now lives in `_agent/conventions/frontmatter.overlay.md` — the overlay of a **frontmatter** convention
whose base opens by declaring itself:

> This file is the **single source of truth** for the frontmatter schemas across every note type the
> vault uses. (`frontmatter.md:25`)

A body-prose rule is not a frontmatter schema. It landed there because the system offered nowhere else,
and the vault recorded the placement as knowingly provisional rather than pretending it fits.

## The sharpest consequence — the rule is invisible to its own watchdog

From the historian lens, and this is the part worth building against rather than merely noting.
`frontmatter.md:247` carries a *Narrow-convention escape hatch*, a recorded scope decision tripwired on
**"prose/behavior drift lint findings + new conventions minted."** That tripwire exists to detect
exactly this pressure — a convention accumulating subjects that should be split out.

An overlay-resident prose rule is **structurally invisible to it**. It is not a new convention minted
(nothing was created in `{conventions}`), and it generates no prose-drift lint finding (no check exists
for it). So the one mechanism installed to catch this failure mode cannot see the instance sitting
inside the file it guards. The vault exempted the rule from that tripwire explicitly, because counting
it would be counting the wrong thing — but that is a vault papering over a module gap.

Compounding it: `vlt-lint`'s `overlay_not_append_only` check (`vlt-lint/references/checks.md:42`) fires
only when an overlay section heading duplicates a base heading **verbatim**. A novel heading — which is
precisely what a new-subject rule has — sails through. The guard reads stronger than it is, so nothing
downstream flags the placement either.

## Provenance guess — marked as a guess

The overlay mechanism looks designed for the *additive-to-an-existing-subject* case, which is the
common one, and the new-subject case appears never to have come up in a live install before. The
`.baseline/` comparison is what makes base files safely refreshable, and a vault-originated convention
has no baseline by definition — so the gap may be a consequence of the divergence-detection design
rather than an oversight in the overlay design. **Inference from the shipped contract and lint checks;
I have not read the module's design history.**

## Suggested shape

A sanctioned **baseline-exempt local convention**: a vault-originated file in a known location that
carries its own enforcement declaration, is explicitly exempt from `baseline_missing`, and is read by
consumers the same way overlays are. The two things it must do that the current options cannot are
(a) exist without a stock counterpart and (b) be visible to the narrow-convention split tripwire as a
convention in its own right.

## What acceptance should check

That a vault can originate a new convention subject and have it land somewhere that generates **no**
lint finding while remaining **visible** to the split tripwire. Both halves — a landing zone that is
merely silent would reproduce today's outcome with better manners.
