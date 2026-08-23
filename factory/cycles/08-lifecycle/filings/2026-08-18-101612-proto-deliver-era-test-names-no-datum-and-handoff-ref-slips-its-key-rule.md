# The proto-`deliver` era test names no datum, and a `handoff` with a `ref` slips its own key rule

- **filed:** 2026-08-18
- **vault:** vlt-core
- **kind:** defect / underspecified rule
- **surface:** `vlt-dispatch/references/relay.md:28` (*Backward compatibility*),
  `vlt-dispatch/references/relay.md:41` (the per-shape key rule),
  `vlt-dispatch/references/ledger.md:26` + `:46` (the denominated legacy lanes)
- **found by:** `acceptance-discharge` run 2 (2026-08-18) — the first post-0.11.0
  `vlt-dispatch ledger` run on vlt-core. **Acceptance check B8-2 (4) FAILED against it.**

## What happened

The first post-0.11.0 `ledger` run reported:

> Denominated legacy lanes (counts, never findings): **15 legacy unkeyed pointers
> (pre-shape)** · **0 proto-`deliver` pointers (pre-shape)** … **2 findings**

The Arc 8 acceptance ledger predicted the opposite for this class: the seven 2026-08-15
inline-payload relays — the exact traffic filing `2026-08-17-140000` was written about —
should render **under the denominated proto-`deliver` count, with zero findings for the
class**. A by-hand application of the shipped rules reproduces the check's number, not the
run's.

## The by-hand count

`_agent/dispatch.md` carries 18 shape-annotated relay headers. Seven are **pathless**:

- `:272 :275 :278 :281 :284 :287` — the 21:30–22:10 batch, each `(handoff, ref: <slug>)`
- `:266` — `(handoff)`, no ref

None carries a handoff-zone path. Every payload link is an `[[_agent/research/...]]`
wikilink, which `relay.md:28` explicitly calls **"payload, never the key"** (only a link
resolving under `_agent/handoffs/` or `_agent/specs/` is a key-path).

Applying the shipped rules:

- `relay.md:41` — "a `handoff` keys on its **doc path** exactly as it always has"; `ref`
  is the key for `ask`, `answer`, and `deliver`. A `handoff` with a `ref` and no path is
  therefore **not keyed**.
- `relay.md:28` — "A shape-annotated **pathless** pointer written **before `deliver`
  existed** is **proto-`deliver` traffic** … reported by `ledger` as a denominated count …
  **never as a finding**."

→ **proto-`deliver` = 7, findings for the class = 0.** The run rendered **0 and 2**.

## The two gaps this exposes

**1. The era test has no datum.** `relay.md:28` says "written before `deliver` existed"
and never says *where* it existed. Module ship (2026-08-17, `86efd48`)? Vault upgrade
(2026-08-17 18:10)? First `deliver` written in this record? The run's own two verdicts are
mutually inconsistent under any single answer: it called the **2026-08-17 15:12** pointer
"post-`deliver`-era traffic" while also rendering the **older 2026-08-15** pointer as a
finding — and both predate every candidate datum.

**2. A `ref` on a `handoff` reads as a key, though no rule says it does.** The run counted
the six `(handoff, ref: X)` pointers among its 45 keyed. That is a defensible *reading* —
a `ref` is present, and it does key the pointer for the spam guard — but the shipped prose
assigns `handoff` a path-key and never states what a supplied-but-unrequired `ref` does.
Six pointers change lane on the answer.

## Why it matters beyond the count

B8-2 shipped check (3) on the claim that **"the denominator is reproducible by a second
reader at rest"**, and verified it against a fixture, where it held. The field shows the
*counting unit* is reproducible while the **era boundary and the handoff-key interaction**
are not — and those were never named by (3), so the fixture could not have caught it. A
denominated lane whose membership two readers dispute is the same failure class as
`2026-07-26-124223` (lint has no memory of adjudicated divergence): a count that looks
settled and isn't.

The lanes are counts, never findings, so nothing was mis-written into the vault — the cost
is that the ledger reported a clean proto-`deliver` zero while seven pointers sat in the
lane it was denominating, and rendered two of them as findings a maintainer is asked to act
on.

## Candidate dispositions (not rulings)

- (a) **State the datum** in `relay.md:28` — the strongest candidate is per-record: "before
  the first `deliver` pointer exists in this record", which is derivable at read time and
  needs no version knowledge.
- (b) **State the handoff/`ref` interaction** — either a `ref` on a pathless `handoff`
  keys it (making six of the seven legal-as-written), or it does not (leaving them in the
  proto lane). One sentence either way; the silence is the defect.
- (c) **Give `ledger` a reproducibility check of its own** — the denominated lanes agree
  with a stated derivation, not just with a grep.
- (d) Consider whether the era rule should expire at all, or whether the proto lane simply
  drains away over time (it is already exempt from the key check).
