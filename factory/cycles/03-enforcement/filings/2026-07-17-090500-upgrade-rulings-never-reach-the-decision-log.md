# A user ruling that repeals a gated mint lands only in the upgrade ledger — the decision log never learns

**Filed from:** `vlt-core` (installed vault, module 0.6.0)
**Found by:** the Chess Coach mint (2026-07-16) — by being its casualty. This filing exists because the
defect produced a concrete, expensive failure, not because it looked untidy.
**Severity:** high — it silently converts the canonical mint history into a **misleading** record, and it
demonstrably causes confident wrong conclusions.
**Confidence:** high — the failure is in this vault's git history and the mechanism is a read of
`vlt-upgrade/SKILL.md`.

---

## 1. The defect

`vlt-upgrade` detects a locally-diverged convention base, surfaces it, and the **user rules** on it. That
ruling is recorded in `_agent/upgrade-ledger.md`. **Nothing writes it to `_agent/mint/decision-log.md`** —
even when the ruling *repeals a decision the decision log records as ratified*.

The skill's own text closes the loop into the ledger and stops there:

- `vlt-upgrade/SKILL.md:35` — *"A base that **differs** from its baseline was hand-edited locally… record
  it as divergence (do **not** silently clobber it… surface this so the local change isn't lost
  unnoticed)."*
- `:41` — *"Write this snapshot to a working note and **append the opening half of a ledger entry**."*
- `:65` — *"For any base recorded as locally-diverged in Step 1, **surface it in the report** so the user
  can lift the change into an overlay or file it upstream."*

Every path terminates at the ledger or the report. The decision log is only ever *"confirmed to exist"*
(`:37` — *"confirm `_agent/mint/decision-log.md`… exist (agent-zone; expected to survive untouched)"*).
**Untouched is exactly the problem.** The upgrade is the one moment a ratified mint decision gets reversed,
and it is the one moment the log is guaranteed not to be written.

## 2. The concrete failure it caused (this is the argument)

- **`decision-log.md:151`** records the 2026-06-13 council-gated convention edit that installed the
  `(partner slug → PARA target)` registry. **It stands today with no superseding entry.**
- **`upgrade-ledger.md:48`** records the 2026-06-24 user ruling that **repealed** it: *"Adopt 0.3.0's
  firewall model… The vault's extra registry-table bound was **retired**. Migrated `vlt-track`,
  `vlt-agent-dog-trainer`, `vlt-agent-health-coach` off the table (kept the invariant)."*

**A reader of the canonical mint history sees the grant and never its repeal.** On 2026-07-16 that reader
was a mint. It read the decision log, found a ratified grant that was absent from the live tree, and
concluded — confidently, and wrongly — that **an upgrade had silently eaten a council-ratified edit**. It
then:

1. wrote that fabricated root cause into a **convention overlay** — the one artifact upgrades never touch,
   so a false provenance story would have become permanent record future mints cite as fact;
2. **filed a module bug report against `vlt-upgrade`** accusing it of a clobber that never happened;
3. opened two backlog items chasing a phantom defect;
4. **re-granted rows to `dog-trainer` and `health-coach`** — reversing the user's own ruling, without their
   councils, against a decision no artifact it could see even mentioned.

All four were withdrawn after a council caught it. **The durability mechanism had worked perfectly** — it
detected the divergence and forced a human ruling. The record just never said so where anyone would look.

**Aggravating factor:** `upgrade-ledger.md` is **not chronologically ordered** (its entries run 0.5.0→0.6.0,
0.3.0→0.3.1, 0.2.0→0.3.0, 0.3.1→0.4.0, 0.4.0→0.5.0 top to bottom). A reader who tails it or greps it can
miss the entry that governs — which is precisely what happened.

## 3. Why this is a module defect and not a vault mistake

The vault followed the skill. `vlt-upgrade` never told anyone to write a decision-log entry, and the
operating contract makes `_agent/mint/decision-log.md` the canonical home of *what the vault decided*
(`vlt-mint`: *"the permanent record"*, *"a gated change must carry its own rationale"*). The upgrade ledger
is the record of *what an upgrade did*. A **ratified design repeal is a decision, not an upgrade action** —
it is currently filed under the wrong noun, by design.

This is the module's own single-home doctrine being violated by the module's own tooling: one fact
(*the registry was retired*) has one home, and it is the wrong one.

## 4. Exact change to ship

**A. `skills/vlt-upgrade/SKILL.md` — new required step, wherever a divergence is resolved by user ruling:**

> **Ratified rulings go to the decision log, not only the ledger.** When an upgrade resolves a base/skill
> divergence **by user ruling** — adopting stock over a local edit, retiring a local rule, or otherwise
> reversing something `_agent/mint/decision-log.md` records as ratified — **append a superseding entry to
> `_agent/mint/decision-log.md`** citing the ledger entry, and **annotate the superseded entry in place**
> with a one-line pointer (`SUPERSEDED YYYY-MM-DD by <upgrade> — see decision-log entry / ledger:NN`). The
> ledger records what the upgrade *did*; the decision log records what the vault *decided*. A repeal is a
> decision. **Exit gate: the upgrade cannot close while a ledger-recorded ruling repeals a decision-log
> entry that carries no superseding annotation.**

**B. Make the superseded entry self-defending.** Even without (A), a decision log whose entries can be
silently repealed elsewhere should say so at the top. This vault has added a local warning header; the
module should ship the discipline instead, so no vault needs the scar tissue.

**C. `upgrade-ledger.md` — ship it newest-first and say so**, or have `vlt-upgrade` state the ordering in
the file header. Non-chronological append order turns "read the ledger" into a trap for exactly the reader
who is trying to be careful.

**D. Consider: should `vlt-upgrade` refuse to proceed when the decision log records gated convention edits
it cannot account for in the live bases?** That inverts the default from *"refresh and report"* to *"prove
the history survived."* Expensive — and arguably what "durable self-evolution" actually costs. Offered as a
question, not a recommendation.

## 5. Migration for existing installs

Ship a **one-time reconciliation prompt**: for each `_agent/mint/decision-log.md` entry of kind
`convention edit`, check whether its change is present in the live base; where absent, cross-reference
`_agent/upgrade-ledger.md` for a ruling that explains it and **write the superseding entry now**.
**Do not auto-restore anything** — a gated edit that a human retired must not be resurrected by a script,
which is the exact error this filing's originating mint made by hand.

`vlt-core`'s known instance: `decision-log.md:151` (2026-06-13 registry grant) ← repealed by
`upgrade-ledger.md:48` (2026-06-24). **One found. Nobody has swept for others**, and it was found by
accident.
