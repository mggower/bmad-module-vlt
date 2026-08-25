# `vlt-upgrade` names a real install (`vlt-core`) on the shipped surface — the skill must be recipient-agnostic

_Filed factory-side 2026-08-24, off the going-public fresh-eyes review
(`factory/platform/review-going-public-2026-08-24.md`, finding F2). The review's
public-history privacy scan surfaced that the field vault's real **name** appears once
on the shipped surface; the owner ruled it a defect the same day: **a shipped skill must
be agnostic to the recipient vault** — no real install's name belongs in what
`vlt-upgrade` delivers. This filing covers only the shipped-surface instance; the
~179 factory-record files that name `vlt-core` are dev history under the separately
ruled publish-as-is posture (names no path — the vlt-sayari precedent)._

## Problem statement + evidence

`skills/vlt-upgrade/SKILL.md`, Step 3 item 7 ("Upgrade-time rulings — write them
through"), closes with a **"First two instances of this rule"** note whose instance (a)
reads: *"the `vlt-core` firewall ruling that should have superseded the decision log
(`_agent/upgrade-ledger.md` firewall entry)"*. That is a real install's name in a
provenance citation, shipped into every vault by the own-the-apply copy.

- **Which rule it breaks:** CLAUDE.md's publishing rule — shipped content carries no
  personal or vault-local information. The worked-examples rule (build-18) permits
  generic *domain* vocabulary and bans live artifact *paths*; an install **name** in a
  provenance citation sits between those and the owner has now ruled it on the banned
  side for shipped surface.
- **Why it shipped:** the note is provenance ("where this rule's first instance
  happened"), and provenance citations are elsewhere deliberately preserved — but that
  preservation rule was minted for the *factory record*, not for text a vault receives.
  In a recipient vault, "the vlt-core firewall ruling" is a reference to someone else's
  vault that the reader can do nothing with.
- **Grounding note for capture:** this is the **only** shipped-surface instance — the
  review measured the name at 180 tracked files / 1183 hits, 179 of them factory
  record. Verify at capture time with:
  `grep -rn 'vlt-core' skills/ .claude-plugin/`.

## Fix direction (for the build to weigh, not to restate)

Genericize the citation without losing its meaning: e.g. *"a field vault's firewall
ruling that should have superseded its decision log"*. The instance's teaching content
(ruling recorded in the ledger alone; the superseding decision-log entry written when
next reconciled) is vault-agnostic already — only the name does no work. One line;
no rule change, so no convention `version:` bump is expected — confirm at capture.
