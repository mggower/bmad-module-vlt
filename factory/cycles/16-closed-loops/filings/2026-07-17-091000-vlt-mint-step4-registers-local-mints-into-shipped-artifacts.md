# `vlt-mint` Step 4 tells vault-local mints to register into the module's shipped install manifest

**Filed from:** `vlt-core` (installed vault, module 0.6.0)
**Found by:** the Chess Coach mint (2026-07-16), at the moment of registering partner #4.
**Severity:** medium — mostly self-correcting (the instruction fails harmlessly), but it is
**semantically wrong** and it has left a false claim in this vault's permanent decision log.
**Confidence:** high on the live-tree measurement; **explicitly uncertain** on the mechanism, and that
uncertainty is stated rather than resolved by guess (see §3).

---

## 1. The defect

`vlt-mint/SKILL.md` Step 4 — *Install and register*:

> A minted **partner** lives at `{module-skills}/vlt-agent-{name}/`… Register its capability row in
> `{project-root}/_bmad/module-help.csv`, and add its `[agent]` entry to the install manifest
> `{module-skills}/vlt-setup/assets/module.yaml` `agents[]` (mirroring the row into that folder's
> `module-help.csv`).

`vlt-setup/assets/module.yaml` and `vlt-setup/assets/module-help.csv` are **the module's shipped install
manifest** — the bundle `vlt-upgrade` merge-copies into every install (`upgrade-ledger.md`, 0.5.0 entry:
*"Refreshed: … `vlt-setup/SKILL.md` + `assets/{module-help.csv,module.yaml}`…"*).

**Two problems.**

1. **It's futile.** A local row written into a shipped artifact sits in the refresh path.
2. **It's semantically wrong, and this is the real objection.** `module.yaml` `agents[]` is what the module
   *ships to every vault*. A personal chess coach — or a dog trainer, or a health coach — has no business
   there. Following the instruction literally means: **my private chess coach becomes part of your module.**

The durability mechanism that actually works already exists and is documented: `merge-help-csv.py
--live-skills-dir` preserves local rows by scanning the live skills dir (`upgrade-ledger.md`, 0.5.0:
*"all 3 rows kept by `merge-help-csv.py --live-skills-dir` (`local_mints_preserved` confirmed; 14 shipped +
3 local = 17 rows)"*). **Local mints don't need the manifest — the CSV merge is their durability.**

## 2. The measurement

Every local mint on this vault's live tree is **live-CSV-only**; every shipped partner is in all three:

| partner | live `module-help.csv` | `vlt-setup` mirror | `module.yaml` `agents[]` |
|---|---|---|---|
| `dog-trainer` (local) | ✅ | ❌ | ❌ |
| `health-coach` (local) | ✅ | ❌ | ❌ |
| `chef` (local) | ✅ | ❌ | ❌ |
| `librarian` (shipped) | ✅ | ✅ | ✅ |

**3-for-3.** The practice has already, independently, converged on the right behaviour — against the
instruction. The Chess Coach mint followed the *practice*, not the *skill*, and recorded the deviation.

## 3. The part I am NOT asserting

`decision-log.md:64` (the 2026-06-13 Health Coach mint) **claims** it did register the manifest:

> **Registered:** live `_bmad/module-help.csv` (row HC) + mirror; `module.yaml` `agents[]` (health-coach)
> + its mirror CSV.

Both are absent today. **Whether an upgrade reverted them or the entry was aspirational is not
established.** The obvious story (the 0.4.0/0.5.0 refresh overwrote them) is *plausible and unverified* —
and this vault spent 2026-07-16 learning what asserting a plausible-and-unverified mechanism costs: a
fabricated root cause reached an overlay and a module bug report before a council caught it (that filing
was withdrawn; see the two companion filings dated 2026-07-16/17). **So it is recorded as an open question,
not a finding.** The maintainer can settle it in one look at the module's own history; this vault cannot.

Either way it is **evidence for the same fix**: the entry is either a record of work the upgrade silently
undid, or a record of work that never happened. Both are what an ambiguous instruction produces.

## 4. Exact change to ship

**`vlt-mint/SKILL.md` Step 4 — split the rule by provenance, because there are two different objects here:**

> - **A partner shipped *with the module*** registers in all three: the live `_bmad/module-help.csv`, the
>   `vlt-setup/assets/module-help.csv` mirror, and `vlt-setup/assets/module.yaml` `agents[]`.
> - **A vault-local minted partner registers in the live `_bmad/module-help.csv` ONLY.** Do **not** touch
>   `vlt-setup/assets/*` — that is the module's shipped install manifest, refreshed on every upgrade, and a
>   vault-local partner must never ship to other installs. Durability for local rows is
>   `merge-help-csv.py --live-skills-dir`, which preserves them by scanning the live skills dir. **If you
>   are minting into a vault rather than into the module, you are always the second case.**

Apply the same split to the **heavy capability / operation skill** bullet directly above it, which carries
the identical *"mirror it into the install manifest… so a re-install reproduces it"* instruction and the
identical problem. (Note this one has a live precedent pointing the other way: `vlt-track` was a vault-local
op mint that **was** later upstreamed — so the rule should say that upstreaming is a *deliberate
contribution step*, not something a mint does by reflex on the way past.)

## 5. Why this matters more than its severity suggests

The module's central promise is a vault that **grows its own cast**. Step 4 is the last instruction in that
process, and it currently points a vault-local creature at the module's shipped surface. It fails safely
today only because the merge script is smarter than the instruction. **The skill should say what the tooling
already does.**
