# Module feedback: chess-coach persona prose seeds fabricated-time violations

**Filed:** 2026-07-18 · **Source vault:** vlt-core · **Partner:** chess-coach (Ana)
**Class:** shipped-prose defect (latent, re-seeds on every install)

## Problem statement + evidence

The chess-coach `SKILL.md` persona section ships an illustrative line:

> *"I can't make you see the fork; I can make sure you spent Tuesday playing instead of memorizing the Najdorf."*

This line names a concrete weekday ("Tuesday") as an idiom for "your limited study time." In live use the
partner **echoes the stock phrasing back at the user as if it referred to a real day**, producing a
fabricated-time reference — exactly the failure the module's own *invent nothing* non-negotiable forbids.

Observed three times in vlt-core, the third *specifically* traceable to this line:
1. "it cost you whole games in weeks one and two" — partner minted the day before (no weeks existed).
2. "on Tuesday" when it was Friday.
3. (2026-07-18) "I'd rather you spent that Tuesday playing" — **twice**, echoing the persona line above.
   This one **got past an existing local guard** because the guard watched for calendar *decoration*, not
   a weekday riding inside a *figure of speech*.

The user (Mikey) flagged all three and characterizes fabricated temporal color as the most corrosive
failure mode: it signals unreliability and distracts from an otherwise-solid claim. Instance #3 is worse
than #1–2 because the partner *had* a written guard and still slipped — the seed is in the shipped prose,
so a guard that doesn't name the idiom class can't hold.

## Decision + rationale

The persona line is doing real characterization work (the "coach the allocation, not the openings" thesis
in one vivid sentence), so **don't delete it — defuse the concrete weekday.** Two viable fixes:

- **(Preferred) Replace the weekday with a non-temporal stand-in for "your scarce time":**
  *"…I can make sure you spent your practice hours playing instead of memorizing the Najdorf."*
  Keeps the rhetorical punch, removes the fabrication seed entirely.
- **(Alternative) Keep the line but add a guard note** in the persona's non-negotiable/`## Self` seed that
  the illustrative "Tuesday" is a figure of speech and must never be reproduced as a specific day to the
  user. Weaker — relies on the partner remembering a caveat about its own prose.

Recommend the first: a seed you have to remember not to step on is a worse seed than one that can't trip you.

## Exact changes to ship

1. **`agents/chess-coach/SKILL.md`** (or wherever the persona prose lives in the module) — edit the "+10–12
   points a year / 241-point spread" paragraph's closing line: `spent Tuesday playing` → `spent your
   practice hours playing` (or equivalent non-temporal phrasing).
2. **Broaden the *invent nothing* / no-fabricated-time guidance wherever it's stated** (contract and/or the
   partner seed) to explicitly cover **time words inside idioms**, not just calendar decoration — the idiom
   is the exact hole instance #3 fell through. Suggested wording: *"A fabricated weekday/week/month counts
   even inside a figure of speech ('spend your Tuesday on X'); strip the day, don't launder it."*

## Upgrade / migration path for existing installs

- Existing installs carry the un-defused line in their local `SKILL.md` copy. On `vlt-upgrade`, the persona
  prose is module-shipped, so the reconcile should pick up the corrected line unless the install has a local
  persona override. Flag in the upgrade note so any vault that has *already* accreted a local guard (like
  vlt-core has, in `_agent/partners/chess-coach/identity.md ## Self`) can keep its guard and also get the
  source fix — belt and suspenders, not a conflict.

## Latent bugs surfaced

- **The seed generalizes:** any shipped persona prose across the module that uses a concrete weekday/date as
  rhetorical flavor is the same trap. Worth a grep across all `agents/*/SKILL.md` and the contract for
  weekday names / "last week" / "last month" used illustratively. (Not audited here — flagging the class.)

## Open design questions (module-wide)

- Should the *invent nothing* clause in the operating contract carry the idiom-time refinement centrally
  (so every partner inherits it), rather than each vertical partner re-learning it in its own `## Self`?
  vlt-core's chess-coach learned it the hard way three times; centralizing would spare the next install.
