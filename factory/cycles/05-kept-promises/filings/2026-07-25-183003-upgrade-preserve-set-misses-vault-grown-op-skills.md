# `vlt-upgrade` Step 1's preserve set enumerates only `vlt-agent-*`, so a vault-grown **op skill** is never snapshotted — and `vlt-mint` Step 4 promises it is

**Filed from:** `vlt-core` (installed vault, module 0.7.0)
**Found by:** the `vlt-file-feedback` mint (2026-07-25), while ruling on whether a pointer capability was needed for durability.
**Classification:** `defect`
**Severity:** medium-low in blast radius, high in *trust* — the failure is silent, and the vault is explicitly told it cannot happen.
**Confidence:** high on the text and the enumeration; **explicitly a guess** on whether any vault has actually lost a skill this way (see §4).
**Lineage:** this is a follow-on defect in the *remediation* of `2026-07-17-091000-vlt-mint-step4-registers-local-mints-into-shipped-artifacts.md`. That filing was accepted and fixed in 0.7.0; the fix's wording is what introduces this. Please capture them together.

---

## 1. The defect

0.7.0's `vlt-mint/SKILL.md` Step 4 now correctly forbids writing the shipped manifest, and tells the minter where durability actually comes from:

> A local mint's durability is the merge's job — **B1 preserves its live-registry row** (`merge-help-csv.py`, keyed off the live skill dir still existing) **and B2 restores its body** — never a shipped-asset write.

**B1 is true for any local mint.** `merge-help-csv.py --live-skills-dir` keys off "a `vlt` row whose skill is absent from the bundled source but whose skill dir still exists live" — that test is provenance-based, not name-based, so it covers `vlt-agent-*` and `vlt-*` alike.

**B2 is true only for partners.** B2 (`vlt-upgrade/SKILL.md` Step 3 item 2) restores "each minted-partner dir **in the Step-1 snapshot**". And Step 1's enumeration is name-scoped:

> - **Minted partners** — every **`vlt-agent-*` dir** under the live skills dir whose code is **not** a shipped agent in the incoming module source's `module.yaml agents[]`…

A vault-grown **operation** skill — `.claude/skills/vlt-{op}/` — matches no Step-1 bullet. Not *Minted partners* (wrong prefix), not *Convention overlays*, not *Capabilities* (that bullet scans `{partners}/*/capabilities/*.md`, the agent zone, not the skills dir), not *Mint history*. **It is never snapshotted, so B2 has nothing to restore it from.**

So the sentence a minter reads for reassurance is half wrong, and it is wrong in the half that matters: B1 preserves a *registry row pointing at a directory that is gone*.

## 2. Why the two halves diverge (the underlying shape)

B1 and B2 answer the same question with different tests:

| | test | covers a vault-grown op skill? |
|---|---|---|
| **B1** (`merge-help-csv.py`) | *provenance* — absent from bundled source, dir exists live | ✅ yes |
| **B2** (Step 1 snapshot) | *name* — matches `vlt-agent-*` | ❌ no |

B1 got the general rule; B2 got a special case. The 0.7.0 Step-1 text even shows the authoring intent — its long caveat is entirely about **partners** self-registering into `agents[]` and being misclassified as shipped. That is careful work on the partner path, and it is the reason the op-skill path went unconsidered: the bullet is named *Minted partners*, so nothing prompts the question "what else does a vault mint?"

Note that `vlt-mint` itself answers that question — it mints **heavy capabilities (operation skills)** as a first-class kind, into `{module-skills}/vlt-{op}/`. The two skills disagree about what a vault can grow.

## 3. Evidence

**This vault, today.** The 2026-07-25 mint promoted a Librarian light capability into a shared op skill at `.claude/skills/vlt-file-feedback/` (decision log: `_agent/mint/decision-log.md`, entry `[2026-07-25] add a capability — vlt-file-feedback`). Its registry row is in `_bmad/module-help.csv` (19 rows). It appears in **no** Step-1 bullet. It is the concrete instance.

**A second vault, already.** This is not a vlt-core-only shape — `2026-07-12-114940-sayari-060-upgrade-field-evidence.md` records vlt-sayari minting op skills as ordinary practice: `vlt-hub` (§4, "1 minted skill", grown within two days of an upgrade), plus `vlt-spec-external` (minted 06-29, retired 06-30) and `vlt-project-spec`. **The class is populated at both known installs.**

**Near-miss provenance.** That same filing's §4 flagged Step 1's preserve-set as a standing hazard and asked for derive-from-disk prose. 0.7.0 shipped exactly that — the **Derive-first invariant** ("the preserve inventory derives from disk, never the prior ledger"). The invariant is right and it does not help here: deriving from disk still only finds what the enumeration looks for. **The bug is the glob, not the source of truth.**

## 4. What I am NOT asserting

**No vault is known to have lost a skill this way, and I did not verify that one hasn't.** On the own-the-apply path the exposure is latent, not live: Step 2 is merge-copy with no `--delete` (this vault's `upgrade-ledger.md` 0.6.0→0.7.0 entry confirms *"merge-copy (no `--delete`)"*), so nothing is deleted and B2 is a documented no-op. The gap bites only where B2 is load-bearing — a destructive apply, an installer-driven reinstall, or the bracket path. **Whether any install has ever taken such a path is a factory-side question I can't see.** Marked as a guess, not a finding.

I also have **not** verified this against a live destructive upgrade. The claim is a reading of the shipped text plus one live tree, not an observed loss.

## 5. Exact change to ship

**`vlt-upgrade/SKILL.md` Step 1 — widen the first bullet from a name test to the provenance test B1 already uses.** Suggested rewording of the bullet head (the existing `agents[]`/pristine-source caveat stays as-is, it is correct and worth keeping):

> - **Local mints** — every **`vlt-*` dir** under the live skills dir that is **not** shipped by the incoming module source (for a `vlt-agent-*` dir, "shipped" means present in the incoming `module.yaml agents[]`; for any other `vlt-*` dir, present in the incoming bundle at all). This covers both minted **partners** and vault-grown **operation skills** — `vlt-mint` mints both, and B1's own preservation test is provenance-based, not name-based, so B2's snapshot must be too. Record dir path + its help-registry row(s).

Then B2 (Step 3 item 2) needs only "each **local-mint** dir in the Step-1 snapshot" instead of "each minted-partner dir".

**Second, smaller:** the ledger schema field `mints_preserved:` and the report line "Mints preserved" both read partner-only. If the widened set should be visible in the ledger, either broaden that field's description or add a sibling — maintainer's call, and I'd default to broadening rather than adding a field.

**Third — the sentence that sent me here.** `vlt-mint/SKILL.md` Step 4's "B2 restores its body" should not ship unqualified until the above lands. If the Step-1 widening ships in the same release, it becomes true and needs no edit. If not, it should say B1 preserves the row and the dir survives a non-destructive apply.

## 6. Why this matters more than its severity suggests

The 07-17 filing's closing line was **"the skill should say what the tooling already does."** This is the same sentence with the terms swapped: here the *skill* promises something the *tooling* doesn't do. A minter who reads Step 4 has been told, in the module's own voice, that a durability question is already answered — which is precisely the kind of assurance that stops someone from checking. In this vault it nearly did: the 2026-07-25 mint's council raised a durability objection, and the objection was initially waved off *because Step 4 says B2 covers it*. It took reading `vlt-upgrade` Step 1 directly to find that it doesn't.

**A false reassurance is worse than a silent gap**, because it converts a question someone would have asked into one they won't.
