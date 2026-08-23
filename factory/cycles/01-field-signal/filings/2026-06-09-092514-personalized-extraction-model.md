# Personalized extraction: a bounded provenance widening for domain partners

**Filed:** 2026-06-09 · **Origin:** dog-trainer mint in `vlt-core` (council-gated, `revise` verdict) · **Targets:** `extraction.md`, operating contract (`{log}` types), `vlt-agent-creative` SKILL — and the partner/op **templates** in `vlt-mint`

## Problem statement + evidence

The vault gained its **first vertical (domain) partner** (a Dog Trainer) whose primary deliverable is a *personalized training protocol* — a PARA artifact that is part general knowledge (how a method works, which belongs in the wiki) and part the user's lived state (this dog's progress, which the dog-agnostic wiki deliberately does not hold).

This collided with the contract's **single most load-bearing rule** (the three-layer write boundary: *PARA is written only through extraction, which draws from the wiki only*). A naive "let the partner write `areas/`" would have opened a **second PARA write-path** — the exact thing the Creative's non-negotiable forbids. But keeping the protocol in `_agent/` only would deny the user a filed, human-facing deliverable they want.

Evidence this is a recurring shape, not a one-off: any future domain partner whose output is *user-specific* (a fitness coach, a meal planner, a study-plan tutor) will hit the identical wall — general method in the wiki, personal state in the agent zone, deliverable wanted in PARA.

## Decision + rationale

Amend `extraction.md` with a **bounded provenance widening** rather than a new write-path. Extraction stays the *one* verb into PARA; we widen only **what a single extraction may cite for personalization**, holding the real firewall fixed.

- **Hard invariant (unchanged, load-bearing):** every general/method claim in an extracted artifact's body traces to a wiki page in `sources:`. This is the firewall; the council confirmed it (not the path-count) is the actual safety property.
- **Soft parameter (the one widening):** a *personalized extraction* may additionally read a partner's own **agent-zone operational data** for personalization, cited in a **separate** `personalization_sources:` frontmatter field — never in `sources:`. Keeping the two roles in distinct fields is what keeps "is every method claim wiki-grounded?" mechanically checkable (a method claim supported only by `personalization_sources` is a visible violation).
- **Not a second write-path:** same verb (extraction), same supersession/filename/trust discipline. The Creative's `vlt-extract` is unchanged (wiki-only); the allowance is **bounded n=1** to the Dog Trainer's `vlt-track` by name — a future op must extend the convention through its own gated mint, not inherit it.
- **Operational-log discipline:** the agent-zone source holds **state, never method/general knowledge** (which would create a second home and break single-home). Enforced by a `vlt-track` verify-step; a `vlt-lint` check is the deeper follow-up.

This design carries a council `revise`→pass verdict (full panel). The panel's key finding: the safety guarantee shifts from *structural* (wiki-only provenance) to *behavioral* (method-grounding discipline), so the discipline must be made legible — which the separate-field design does.

## Exact changes to ship (module-side)

1. **`_meta/conventions/extraction.md`** — add the **`## Personalized extraction — drawing on agent-zone state`** section (hard-invariant / soft-parameter framing; `sources:` wiki-only vs separate `personalization_sources:`; n=1 scope bound to `vlt-track`; operational-log discipline). Add the pointer clauses in *What extraction is*, *Required frontmatter* (commented optional `personalization_sources:`), and *Skill flow*. **The full amended file is in the vault at `_meta/conventions/extraction.md` as of commit `4154b12` — lift it verbatim.**
2. **Operating contract (`vault-operating-contract.md`)** — the `{log}` `<type>` set is now stated **non-exhaustive** (ops may coin their own type, e.g. `vlt-track`'s `track`), mirroring the non-exhaustive `type:` frontmatter set. One-line change in the `{log}` section. (Lift from commit `4154b12`.)
3. **`vlt-agent-creative` SKILL.md** — one-line carve-out pointer in the non-negotiable: a domain partner's personalized extraction may list an agent-zone path under `personalization_sources:`; that is the same single write-path with a bounded widening, not a second one. (Prevents a reader of the Creative file alone from misreading a non-wiki source path as a violation.)
4. **`frontmatter.md`** — *no change needed*: it already defers PARA-artifact frontmatter to `extraction.md` as the canonical reference, and `personalization_sources:` is a bare-path list covered by YAML rule 4. (Single-home held — the new field is documented only in `extraction.md`.)
5. **`vlt-mint` templates / docs** — consider documenting the **vertical (domain) partner** as a recognized partner archetype alongside the horizontal (function) partners (librarian/researcher/creative). The `partner-agent-template.md` works as-is, but a note that a vertical partner (a) names its domain self-awarely, (b) typically needs its own operation skill, and (c) may need a bounded convention widening like this one would help the next domain mint.

## Upgrade / migration path for existing installs

- `extraction.md` + contract + Creative edits are **additive and reversible** (council-confirmed): a new section + pointer clauses + one field. No existing extracted artifact changes — `personalization_sources:` is optional and absent on every standard extraction.
- Rollback cost is ~the few `vlt-track`-produced protocol files (relocate to `_agent/`), per the pragmatist's assessment.
- On reinstall/refresh, installs that adopt a domain partner get the amended convention; installs without one are unaffected (the allowance is dormant).

## Latent bugs / observations surfaced

- **n=1 generalization risk:** the convention is written for one partner by name. If a second vertical partner arrives, decide whether to (a) add it by name (keeps the bound tight) or (b) generalize to a tested class predicate. Don't pre-generalize (historian's caution).
- **Enforcement gap (filed to vault backlog):** the method-traces-to-wiki firewall is currently prose + a verify-step checkbox. The skeptic wanted a `vlt-lint` check as a *precondition*; it was accepted as a deferred follow-up since frontmatter segregation already makes it lint-able. **Module should ship the `vlt-lint` check** that flags: (a) an `areas/dog-training/` (or any personalized) artifact whose body method-claims aren't covered by its wiki `sources:`, and (b) a training/operational log containing method/general knowledge. This closes the structural-vs-discipline gap the council left open.
- The council arg-passing bug from the sibling filing (`2026-06-09-...-vlt-mint-phases-and-planning-doc.md`) was hit during *this* mint's gate — see there.

## Open design questions (module-wide)

1. Should `personalization_sources:` be a **general** PARA-frontmatter field (any extraction may have one) or stay **gated per-op** by `extraction.md`'s named-allowance? Current design: gated per-op. Generalizing it would simplify the convention but weaken the n=1 bound.
2. Is "vertical vs horizontal partner" worth promoting to a **first-class concept** in the operating contract / `vlt-mint` (with its own template guidance), now that n=1 exists? Or wait for n=2?
3. Should the deferred `vlt-lint` firewall check be a **precondition** for shipping personalized extraction in the module (skeptic's position), rather than a follow-up? In the vault it was deferred; the module may want to ship them together so no install gets the widening without the enforcement.
