# `extraction.md`'s grant text survived the model it granted under — on a stock install it authorizes nobody

**Filed from:** `vlt-core` (installed vault, module 0.6.0)
**Found by:** the Chess Coach mint (2026-07-16), which needed the grant and went looking for it.
**Severity:** high — a **shipped skill is told to refuse its own purpose on a stock install**, and two live
partners are unauthorized under the base's own letter today.
**Confidence:** high — every claim below is a file read, quoted verbatim. (Stated explicitly because a
filing from this vault on 2026-07-16 asserted an unverified mechanism and was withdrawn. This one is text.)

---

## 1. The defect

`conventions/extraction.md` §*Personalized extraction* → *Scope of the allowance* (live line 47, `version: 2`,
`last_updated: 2026-07-06`):

> **Scope of the allowance — bounded, opt-in per operation.** This is **not** a standing license, and
> **no skill shipped with the module uses it** — the general `vlt-extract` draws on the wiki only. A domain
> (vertical) partner's operation may use personalized extraction *only* when that operation's own mint
> **explicitly extends this section to name it** (and is gated accordingly)… Absent such a named, gated
> extension, an agent-zone path in a `sources:`/`personalization_sources:` field is a violation, not a
> precedent.

**The section names no operation.** And `vlt-track` — whose entire stated purpose is personalized
extraction — **has shipped since 0.4.0**, which makes "no skill shipped with the module uses it" false in
the same paragraph that makes naming load-bearing.

`skills/vlt-track/SKILL.md:98` then enforces the unsatisfiable condition:

> The calling partner's use of personalized extraction **must already be sanctioned by its own gated mint**
> (the mint that extended `extraction.md`'s *Personalized extraction* to name the op — see that convention).
> If you are running a loop for a partner whose op was never granted the widening, **stop** — the allowance
> is earned through a gated mint, not taken here.

**So on a stock 0.6.0 install, `vlt-track` is instructed to `stop` for every partner it is ever asked to
serve, forever.** Nothing can name the op except a mint that edits the base — and a base edit is the thing
the module's own durability doctrine tells vaults not to make.

## 2. How it got here (the vault's history — offered as diagnosis, not blame)

This vault reached the state by a legitimate route, and the route is the interesting part:

- **2026-06-09** — the allowance was introduced bound *by skill name* (`vlt-track`, n=1).
- **2026-06-13** — a full four-lens council rebound it to a `(partner slug → PARA target)` **registry
  table**, on the reasoning that *"a shared skill's name bounds nothing once more than one partner runs
  it… declaring a profile grants nothing, only a gated row does."* Rows: `dog-trainer`, `health-coach`.
- **2026-06-24** — the 0.2.0 → 0.3.0 upgrade detected the base divergence and the **user ruled**: adopt
  0.3.0's **invariant-based** model, retire the table, migrate the partners off it, keep the invariant
  (`_agent/upgrade-ledger.md:48`).

That ruling was correct and is not in dispute. **What was never done is reconcile the base's prose with
it.** The naming clause is a **relic of the retired table model**; the invariant is what actually governs.
So the paragraph now demands a ceremony that grants nothing and blocks everything.

## 3. Live consequences on a stock install

1. **`vlt-track` is self-refusing.** See above. The only reason vaults function is that partners don't
   actually execute the stop-check — i.e. **the rule is load-bearing in prose and dead in practice**, which
   is the worst of both.
2. **Existing partners are unauthorized by the letter.** `dog-trainer` (`areas/dog-training/{dog}/`) and
   `health-coach` (`areas/health/`) both write personalized extractions today. Neither is named anywhere.
   This is not a future partner's problem; it is the current state.
3. **`consumers:` is mistakable for the grant.** `extraction.md:12` reads
   `consumers: [vlt-extract, vlt-lint, vlt-track]`. The Chess Coach mint read that as the authorization,
   classified itself `non-boundary` on that basis, and was rejected by council. **A reader got this wrong;
   the field name invites it.** If `consumers:` is only a change-notification list, the convention should
   say so where it can be misread.
4. **`vlt-lint` cannot catch any of it.** `vlt-lint/SKILL.md:80` scans only `method_not_in_sources` and
   `method_in_personalization` — the method-grounding invariant. It never asks *"is this partner authorized
   to personalize at all?"* Under the invariant model that is **correct and deliberate** (the 2026-06-24
   ruling retired the registry check with the registry). Noting it so nobody re-adds a check for a rule that
   no longer exists — **the absence is the ruling, not a gap.**

## 4. Exact change to ship

**`conventions/extraction.md`, §*Scope of the allowance*. Bump `version: 3`; run the consumer walk
(`vlt-extract`, `vlt-lint`, `vlt-track` re-pin `depends_on`).**

1. **DELETE** *"and **no skill shipped with the module uses it**"* — false since 0.4.0.
2. **DELETE the naming requirement** (*"only when that operation's own mint explicitly extends this section
   to name it"*) — it is a relic of the retired table model and is satisfiable by nobody. **Recommended**,
   because the invariant model the module itself shipped at 0.3.0 is what governs.
3. **REPLACE with the invariant model, stated positively:** an operation may perform personalized
   extraction when it honors the hard invariant — `sources:` lists only wiki pages, every method/general
   claim traces to one, `personalization_sources:` carries situation and never fact — and `vlt-lint`'s
   scans (a)+(b) are the net. Name `vlt-track` as the shipped op that does this.
4. **`skills/vlt-track/SKILL.md:98` — replace the stop-check** with the invariant re-assert it should have
   become at 0.3.0: don't stop for want of a name; stop if the block's method claims don't trace to the
   wiki.
5. **`conventions/extraction.md:12`** — annotate `consumers:` in the file as *change-notification, not
   authorization*. One clause; it cost this vault a wrong classification and a rejected mint.

**Alternative if the naming clause is deliberate** (i.e. per-op authorization is still wanted): then ship
the section **naming `vlt-track`**, and say explicitly that per-*partner* authorization was retired at 0.3.0
in favour of the invariant. Either way the current text — a naming rule naming nobody — cannot stand.

## 5. Migration for existing installs

None required if the invariant model is confirmed: no vault has rows, the invariant is already enforced by
lint, and the two live partners already satisfy it (the 2026-06-24 ledger entry records both extractions as
invariant-clean and untouched). **This is a prose-reconciliation release, not a data migration** — which is
precisely why it has gone unnoticed for a month: nothing breaks, the rule is simply inert and wrong.

## 6. Open question

Was the 0.3.0 invariant model intended to **replace** per-op authorization entirely, or to sit *under* a
still-live naming gate? The vault cannot tell from the text, and the two readings imply opposite fixes
(§4 vs the alternative). The 0.3.0 changelog framing — *"`vlt-lint` is not gutted… it keeps the load-bearing
invariant and adds overlay/capability/family/convention-coherence/base-divergence checks"* — reads as
**replace**, but that is a vault's inference from a ledger entry, not a module statement.
