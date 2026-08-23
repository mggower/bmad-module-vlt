# vlt-mint — Verification Notes

_Friction observed running `/vlt-mint` to mint a new partner (**The Creative**, `vlt-agent-creative`) on `vlt-core`, 2026-06-03. For module iteration._

The mint completed end-to-end and the partner is live (it appeared in the session's available-skills list mid-mint, confirming the runtime loaded it). No data was clobbered. But one structural finding (§1) is serious and was only caught by accident, and the "new partner" path has a real gap (§2) the flow doesn't mention. Ordered by impact.

## 1. Mints land in the project tree, but a divergent **plugin-cache copy** of the module also exists — and subagents read the cache

`vlt-mint` resolves `{module-skills}` to `{project-root}/.claude/skills/`, so I authored `vlt-agent-creative/` and edited `vlt-agent-librarian/SKILL.md` there. That tree is what the runtime loads (the new partner showed up in-session). **But there is a second, full copy of the module at `~/.claude/plugins/cache/vlt/vlt/1.0.0/`**, and after the mint the two trees diverge — verified:

- Project `vlt-agent-librarian/SKILL.md`: **6499 B**, carries my edit (the `vlt-extract` → Creative migration). Different inode (`174832114`).
- Plugin-cache `vlt-agent-librarian/SKILL.md`: **6567 B**, **pristine v1.0.0, does not carry the edit**. Different inode (`174738665`).
- `vlt-agent-creative/` exists in the project tree **only** — not in the cache.

Two compounding problems:

1. **Silent revert risk.** If the plugin system ever refreshes/reinstalls the project `.claude/skills/` from its cache (or a `vlt-setup` re-run copies from the manifest), every mint — new partners, capability migrations, persona self-edits — is shadowed or reverted with no warning. The mint's durability depends on an assumption the skill never states: that the project tree is authoritative and won't be overwritten from the cache.
2. **Subagents ground in the cache, not the working tree.** The review-council architect I spawned (see `review-council-friction.md §3`) independently read the Librarian's SKILL.md and resolved it to the **plugin-cache** path — i.e. it reviewed pristine pre-mint state. Harmless here (the parked note was identical), but a mint that edits the project copy *before* the council runs would have the council review stale state.

**Suggested fix:** the mint skill should (a) state explicitly which tree is authoritative and whether mints must also be written back to the plugin-cache/manifest source to survive a refresh, and (b) if the project tree is a plugin install, warn that hand-authored mints live outside the plugin's managed source and document the persistence story. At minimum, Step 4 ("Install and register") should name the cache-divergence hazard. This feels like a real `capability-gap`/`maintenance` candidate — flagged below, not yet filed.

## 2. The "new partner" path has no step for **migrating a capability away from an existing partner**

The Creative was minted to *own* `vlt-extract`, which the Librarian had been holding with an explicit parked note ("will migrate to the Design Partner once that partner is minted"). Transferring it meant editing **another partner's** SKILL.md — removing the `vlt-extract` capability bullet, stripping "extract a PARA deliverable" from its `description`, and removing the parked clause. None of that is in Step 3's **"Mint a new partner"** instructions, which cover only authoring the new partner's own files ("filling persona, non-negotiable, and capabilities" + seeding `thread.md`). The *operation-skill* path does say "update the requesting partner's tool list" — so the flow knows about adjusting a partner's capability list in one direction, but the new-partner path is silent on the reverse (removing/transferring one).

I inferred the migration from the council's verdict, not from the skill. A less careful pass would mint the Creative with `vlt-extract` and leave the Librarian *also* claiming it — two partners advertising the same op, exactly the kind of dual-home the module otherwise polices.

**Suggested fix:** add to the "Mint a new partner" path: "If the new partner assumes ownership of a capability currently held by another partner, edit that partner's SKILL.md to remove it and add a pointer to the new owner — single-home applies to capabilities, not just wiki pages."

## 3. Registration is a manual fan-out across 5+ files, with a quoting-style trap between the two CSVs

Step 4 + the closing instructions require, for one partner, edits to: the new `SKILL.md` and `customize.toml`, the live `_bmad/module-help.csv`, the **mirror** `vlt-setup/assets/module-help.csv`, `vlt-setup/assets/module.yaml` `agents[]` (and I chose to update its `module_greeting`), the seed `thread.md`, the mint `.decision-log.md`, and the `{backlog}`. No helper consolidates these, and they desync easily. Concretely, the two `module-help.csv` files use **different quoting styles** — the live one leaves `description`/`args` unquoted; the mirror wraps them in `"..."`. A copy-paste of the same row between them produces a malformed line unless you notice and reformat.

**Suggested fix:** either provide a small registration helper (à la the existing `merge-help-csv.py`) that writes both CSVs from one row spec, or at minimum normalize the two CSVs to identical quoting so a row is portable between them.

## 4. The `kind → council` table is duplicated verbatim in two skills, and the copies already drift

`vlt-mint` Step 2 and `vlt-review-council` Step 2 both carry the same map. They already disagree cosmetically: mint says `new partner | architect (+moderator)`; council says `new partner | architect + moderator`. Ironic for a module built on single-home discipline — the gate's source of truth is stored in two places.

**Suggested fix:** make `vlt-review-council` the single owner of the table; have `vlt-mint` Step 2 point to it rather than restate it.

## 5. "the new skill carries its own [.decision-log.md]" is ambiguous for a minted partner

The closing line says "note it in this skill's `.decision-log.md` (and the new skill carries its own)." I created `vlt-mint/.decision-log.md` (it didn't exist), but the partner template has no `.decision-log.md` and I didn't create one for `vlt-agent-creative` — it wasn't clear whether a freshly-minted *partner* is supposed to start with an (empty) decision log or whether that clause applies only to minted *operation skills*.

**Suggested fix:** clarify whether the template should seed an empty `.decision-log.md`, and if so add it to the partner-agent scaffold.

## 6. The `customize.toml` "DO NOT EDIT — overwritten on every update" banner is confusing on a hand-authored new file

The scaffold has me author `customize.toml` by hand, but its first line is `# DO NOT EDIT -- overwritten on every update.` For a brand-new partner there's nothing to overwrite yet, so the banner contradicts the act of writing it. It's correct *post-install* (the file is install-managed), but in the mint moment it reads as a warning against the thing I'm doing.

**Suggested fix:** a one-line note in the scaffod ("this banner is for downstream updates; authoring it at mint time is expected") would remove the second-guess.

## What worked well

- **The scaffold is genuinely turnkey.** `partner-agent-template.md` gave a complete, house-styled SKILL.md + `customize.toml` + `thread.md` seed; instantiation was mechanical, and the contract guarantees (four-read activation, single-writer, in-vault `thread.md`) came for free exactly as the skill promises.
- **The "anticipated mint" signal paid off.** The Librarian's parked note pre-cut the hole this partner fills, which made the fit-check fast and gave the council a strong prior. The contract genuinely composed — this is the module's self-evolution thesis working.
- **The gate is fast and unambiguous about *when* to apply friction.** `kind → council` is a lookup, not a judgment call; an operation-skill mint would have skipped the council entirely. Resolving the `kind` by asking the user (not guessing) was the right default and the skill is emphatic about it.
- **The two-tier identity / drift-boundary guidance is clear** — it was obvious that authoring a new partner is a gated mint, and that voice/tone would have been an ungated `## Self` note instead.

---

_Net: the partner mint is conceptually clean and the scaffold is excellent, but its **persistence model is undocumented and fragile** (§1: a divergent plugin-cache copy means a refresh could silently revert any mint), and the "new partner" path **omits capability-migration** (§2), which is exactly the case this mint hit. Registration ergonomics (§3) and the duplicated gate table (§4) are secondary. Two backlog candidates surfaced — §1 (mint persistence vs plugin cache) and §3/§4 (registration helper + single-source gate table); I'll file them only on your say-so._
