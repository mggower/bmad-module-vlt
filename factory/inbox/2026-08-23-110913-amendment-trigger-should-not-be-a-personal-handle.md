# The amendment channel's trigger is a personal handle — move it to the repo's watch/subscription

_Filed by the owner from the factory on 2026-08-23, during the Arc 10 second-half disposition
review (B10-7 disposition 7, ruled **keep literal** for this release with this filing as its
named follow-up). Not a defect: the shipped channel works exactly as designed. This is a
candidate to replace its **trigger mechanism** with one that does not put a personal GitHub
handle into the public shipped surface._

## Problem statement + evidence

B10-7 shipped the rail amendment channel. Its trigger is a literal @mention of the owner's
personal handle in two public issue-template bodies:

- `.github/ISSUE_TEMPLATE/field-pattern.yml:17`
- `.github/ISSUE_TEMPLATE/field-candidate.yml:17`

Shipped text, both files, identical:

> To amend after an issue is labeled `captured`: add a comment with the new evidence **and
> @mention @mggower** — the notification is the trigger for a look; the owner applying the
> `amended` label is what admits the comment into the factory. An unadmitted comment is not read.

**Why it is literal, and why that was right for the release.** A14 names a *GitHub
notification* as the trigger. A prose "@mention the owner" notifies nobody — GitHub fires a
notification only on a real handle — so a non-literal mention would make the amendment
channel's trigger a permanent no-op and strand the mechanism B10-7 built (disposition 4's
consume-on-read append leg). B10-7's disposition 7 reasoned that the handle introduces no new
coupling, because the repo slug `mggower/bmad-module-vlt` is already hardcoded in the same
files (`:14` in all three forms, `config.yml:27`, and 15 times in the label bootstrap block),
so a repo move already edits exactly these files. That argument is sound and was
owner-confirmed 2026-08-23.

**The residue.** CLAUDE.md's publishing rule is that shipped content carries no personal
information. A GitHub handle is personal information in the literal sense, even where it is
already discoverable from repo ownership and commit authorship. The exposure is bounded —
`.github/` is tracked and public but is **not** part of the own-the-apply copy surface, so the
handle never lands inside an installed vault — but the module currently depends on one
person's account name for a mechanism to fire.

**Second-order cost, worth naming:** the trigger is single-person by construction. If the
module ever has a second maintainer, or the owner's handle changes, the channel breaks
silently — filers keep @mentioning a handle that notifies nobody, and the failure looks
exactly like "nobody amended anything."

## The candidate

Replace the personal-handle trigger with a **repo-level notification mechanism** that fires on
comment activity without naming a person:

- the maintainer's **watch/subscription** on the repository (all-activity or
  participating-and-@mentions), so comments on open field issues notify by subscription rather
  than by mention; and/or
- a **repo-owned surface** as the mention target if one is wanted — a team handle, a role
  account, or `CODEOWNERS`-driven notification — none of which is a personal name in shipped
  text.

The template sentence then instructs the filer to *add the comment* (and, if a label is
grantable to filers, apply `needs-info`), with the notification arriving via subscription. The
rest of the channel is untouched: the owner still applies `amended`, and the intake's
consume-on-read leg still clears it.

## What must be preserved

- **The trigger must remain real, not prose.** The whole point of disposition 7 is that a
  trigger nobody receives is a mechanism that does not exist. A replacement ships only if the
  notification demonstrably fires — that is the acceptance evidence, not a design claim.
- **Admission stays owner-gated.** `amended` is what admits a comment into the factory; this
  candidate changes only how the owner learns there is something to look at.
- **`rail_contract` bump check.** Under B10-7 disposition 3 the label set is additive without a
  bump, but changing the amendment instruction's *meaning* may bump — decide at brief time.

## Open questions for capture

1. Does a repository watch actually notify on comments to issues the maintainer has not
   participated in? (Verify against GitHub's current notification semantics — a spike, not a
   memory read.)
2. Is there a filer-grantable label that could serve as an explicit "please look" signal, or
   does the repo's permission model make that owner-only?
3. Does the same residue exist anywhere else in the shipped surface? (The repo slug is
   deliberate and stays; this is about person-names.)

## Provenance

- B10-7 brief: `skills/reports/build-B10-7-rail-amendment-channel.md`, disposition 7.
- Owner ruling 2026-08-23: keep literal for the v0.14.0 release; file this candidate forward.
- Related: B10-7 disposition 4 (amendment append mechanics) — the consumer of this trigger.
