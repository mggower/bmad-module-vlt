# The PARA `type:` carve-out is an enumeration of one, and it penalizes accurate vocabulary

_Filed 2026-08-31 from **`{field-vault}`**, on the **re-derivation of a live parked interim** — the
park against `conventions/extraction.md` (upstream filing **#15**), which `vlt-upgrade`'s
`parked_interims_review` has surfaced on every run since 2026-08-26 with the standing instruction
*"re-derive the unwind against the rules in force now; do not execute the exit as recorded."* The
re-derivation was performed against **`extraction.md` v9** as shipped in v0.17.1. **It does not
unwind.** The ruling the park was waiting on landed, and re-deriving against it surfaced a defect in
the ruling itself. Evidence is `{field-vault}`, read-only._

**⚠ This filing supersedes the premise of park #15, not the park.** The vault is not asking for the
same thing again. #15 asked *which convention's `type:` vocabulary does Layer 3 mean* — that question
was answered at v8/v9 and the answer is `extraction.md`, correctly. This filing reports that the
answer, as written, makes a legitimate shelf illegal and a false statement mandatory.

## The claim

`extraction.md:84` closes the PARA `type:` set and removes exactly one subtree from the population
**by name**:

> A file in the `para_*` population (under `{projects}`, `{areas}`, `{resources}`, **the `{wiki}`
> subtree removed by name at selection time** …) carries a `type:` from the **closed** set …

`{wiki}` resolves to **`resources/wiki/`** — a subtree of `{resources}`, inside the PARA population,
whose files carry **`type: wiki`**: a module-canonical, **non-PARA** type. In `{field-vault}` that is
**146 files**. Under `:84`'s own logic every one of them is a *"mis-typed or mis-placed artifact."*
They are not findings only because the module wrote their shelf's name into the rule.

`{field-vault}` has a second shelf of exactly the same shape — `resources/briefs/`, holding
agent-written periodical issues carrying **`type: research`**, currently **8 files across 3
subscriptions**. It is a finding, on every sweep, forever. **The difference between the two shelves
is not a principle. It is that one of them is named in the rule and the other is not.**

## The carve-out is a completeness-claiming list of one

The module states it as a list, in the singular, at four sites:

| site | text |
|---|---|
| `extraction.md:84` | *"the `{wiki}` subtree **removed by name** at selection time"* |
| `extraction.md:80` | *"the `{wiki}` subtree is not a target folder"* |
| `vault-operating-contract.md:41` | *"an active domain that contains the wiki: the nested `{wiki}` subtree is not PARA"* |
| `vault-operating-contract.md:70` | *"with **one carve-out by name**: the `{wiki}` subtree under `{resources}`"* |

This is the failure the module's own standing discipline names: **lists that claim completeness
drift — they fall behind additions; subset-with-defaults listings don't; prefer point-at-the-map over
full enumerations.** `resources/briefs/` is the addition it fell behind. The carve-out was written
when `{wiki}` was the only typed subtree anyone had, and it encoded that contingency as a rule.

## The inversion: the module penalizes its own correct vocabulary

`:84` admits vault-declared schema — *"any vault-declared schema in `{overlays}/extraction.overlay.md`
(the declare-at-birth rule)"* — and then closes that route for exactly one class of value:
*"never to declare **module vocabulary** as vault-grown overlay schema."*

The consequence, stated as a fact about two hypothetical vaults:

- A vault that types its brief issues **`type: dispatch-brief`** — a word the module does not own —
  declares it at birth in the overlay and is **conformant today**.
- `{field-vault}` typed them **`type: research`**, which is the honest and accurate word for a dated,
  single-pass, `trust: raw` periodical snapshot, and is therefore **permanently non-conformant**.

**The rule is strictest against the vaults that use the module's vocabulary correctly.** A vault is
rewarded for inventing a synonym and punished for naming the thing accurately. That inverts the
purpose of a recognized-vocabulary rule, which exists to make artifacts describable — not to make
accurate description a violation.

## Why the stated legal responses are both refusals

`:84` offers two exits. Neither is available without writing something false.

**Retype to `type: resource`.** A brief issue is not a resource-shaped artifact. It is a dated
snapshot that rests once complete — the exact distinction `extraction.md:28-30` draws between a
research note and an extracted artifact (*"a research note is a dated snapshot … PARA artifacts are
extracted"*). Typing it `resource` would be **a false statement about the artifact, written to close
a checker's finding.**

⚠ **`{field-vault}` has already refused this exact move once, on principle, and the module agreed.**
The sibling park against `write-verification.md` (#16) refused to stamp a rostered `verified_by` on a
file that op did not write — *"stamping any rostered op is a false provenance claim"* — and held an
open finding instead. `write-verification.md` v5 then **ratified that refusal in the convention
text**: *"fusing permission to provenance is the write-path failure this exemption exists to
prevent."* **Falsifying `type:` to satisfy `para_type_unknown` is the same act as falsifying
`verified_by:` to satisfy `para_missing_attestation`.** A module that praised the first refusal
cannot require the second falsification.

**Relocate to `{research}`.** This reverses a deliberate, logged vault decision — the 2026-08-26
`capability-change` that moved the brief shelf to `resources/briefs/` precisely because the shipped
contract admits that address. It also destroys the shelf: brief issues are *serialized per
subscription* (`{briefs}/{slug}/YYYY-MM-DD-issue-NNN.md`), and `{research}` is a flat dated zone with
no per-subscription containment. The relocation is not a re-home; it is a loss of structure.

## The mechanism the module already has, and never joined up

Both halves of the fix exist and ship today. They have simply never been connected:

1. **A declared path.** `skills/vlt-setup/assets/module.yaml:45` declares `wiki: resources/wiki/` in
   the **canonical default map** — *"the SINGLE SOURCE OF TRUTH for the structure map … To add/rename
   a logical path, edit it HERE"* — and `:67` states the override idiom: *"override a single entry
   only if this vault diverges."* **`{wiki}` is already a vault-configurable path.** The carve-out
   keys on a declared path, not on a literal string.
2. **A declared type.** The **declare-at-birth rule** already lets a vault declare schema in
   `{overlays}/extraction.overlay.md`, and `:84` already honours it inside the closed set.

The module can declare *where a shelf is* and it can declare *what a type means*. It has never let a
vault say **"this declared subtree carries this type"** — which is the only thing `{wiki}` actually
needs, and the only thing `resources/briefs/` is missing.

## Candidate direction (not a fix — capture's call)

**Generalize the carve-out into a declarable typed subtree.** A vault declares a subtree of a PARA
zone and the `type:` its files carry; `para_type_unknown` then judges those files **against that
declaration** instead of against the PARA artifact set. `{wiki}` stops being a hardcoded name and
becomes **the module's own first instance of the general rule** — its shipped default, not its
exception. Point-at-the-map, not an enumeration of one.

This is what makes the owner's stated position enforceable. The position is *"any designated type
should be legal as long as it is consistent and intentional."* **`intentional` is not observable, and
a check that cannot see it has no enforcement point** — which is this cycle's entire through-line, and
the reason the position needs a mechanism rather than a permission. Under a declared typed subtree
both halves become checkable: **the declaration is the intention** (made once, at birth, in the
overlay), and **conformance to it is the consistency** (every file in the subtree carries the declared
type).

⚠ **Correction to an earlier draft of this filing, kept visible rather than edited out.** This
direction was first argued as a *stricter* check on the grounds that a stray `type: wiki` under
`{briefs}` is invisible today. **That is false.** `vlt-lint/references/checks.md:19` flags *"a file
in the population carrying a `type:` outside the recognized set"*, and `wiki` is outside it — so a
stray `type: wiki` under `{briefs}` is already a `para_type_unknown` finding. **The direction is
looser, by exactly one declared value per declared subtree, and that is the point rather than a cost
to conceal.** What makes it safe is not added strictness but **scope**: the declaration legalizes one
value inside one named subtree, recorded durably in the overlay, and makes that value legal **nowhere
else in the PARA population**. `checks.md:19`'s stated reason for the prohibition — overlay-declaring
module vocabulary *"would make the vault assert local authorship of a module-level answer"* — is
**correct for the global case and does not reach a subtree declaration**, which asserts only which
shelf holds which kind and answers nothing at module level. The prohibition should keep its
population and lose its overreach.

⚠ **Note what this direction does NOT propose.** It does not reopen `:84`'s closed set, weaken
`para_type_unknown`, or re-admit `frontmatter.md`'s non-exhaustive list as an answer for the PARA
population — that ruling was correct and this filing does not contest it. The closed set stays closed
**for undeclared files in a PARA zone**, which is the population it was written for.

Two secondary questions capture should settle rather than assume: whether the
module-vocabulary prohibition survives at all under a declared subtree (the vault's read: it should
not — the prohibition exists to stop a vault redefining a module word globally, and a subtree
declaration redefines nothing, it states which shelf holds which kind), and whether the declaration
belongs in the overlay, the structure map, or both.

## Grounding against current module source (v0.17.1)

- `skills/vlt-setup/assets/governance/_meta/conventions/extraction.md:84` — closed set, the by-name
  removal, the module-vocabulary prohibition, both legal responses. `extraction.md` is at
  `version: 9`.
- `.../conventions/extraction.md:80` — the `{resources}` → `resource` mapping row and its `{wiki}`
  parenthetical.
- `.../conventions/extraction.md:28-30` — the research-snapshot vs extracted-artifact distinction the
  retype would violate.
- `.../vault-operating-contract.md:41`, `:70` — *"one carve-out by name."*
- `.../conventions/write-verification.md:55` (`version: 5`) — *"fusing permission to provenance is the
  write-path failure this exemption exists to prevent"*, the ratified refusal this filing reasons
  from.
- `skills/vlt-setup/assets/module.yaml:45`, `:67` — `wiki: resources/wiki/` in the canonical default
  map, and the per-entry override idiom.

## Field evidence

- **146** files under `resources/wiki/` carry `type: wiki` — legal only by the by-name removal.
- ⚠ **9** files under `resources/briefs/` carry `type: research` — a standing `para_type_unknown`
  finding, and **the number moved again while this filing was being written.** The park recorded
  **5**; the 2026-08-30 sweep re-measured **5**; three landed 2026-08-31 (**8**); the 2026-09-01 sweep
  reads **"9 brief issues … UP FROM 5"**. The growth rate the park priced — *"one file per
  subscription per cadence for as long as the park is live"* — **has now fired twice in three days.**
  This is not a static debt, and the count in any snapshot of it is stale on arrival. *(The
  no-frontmatter PARA population moved 3 → 4 over the same window — a different finding, noted so the
  two are not conflated.)*
  ⚠ **The park's scope is the `type:`, not the count, so nothing here moves the ruling** — but the
  blast radius of leaving it unruled is compounding, which is the fact the ruling should be made
  against.
- The producer is the vault-local `vlt-brief` capability, which writes `type: research` per the
  research schema. **It is not a defect in the capability**: under the direction above that line
  becomes correct, and under the current rule there is no value it could write that is both accurate
  and legal.

## Disposition on the park

Park #15 is **re-derived and NOT unwound.** The exit recorded at park time is invalid — it assumed
the ruling would make `type: research` legal at that address, and the ruling instead made it
explicitly illegal while leaving an identically-shaped shelf legal by name. Per
`{conventions}/decision-log.md`'s supersession idiom the vault will record a **superseding
`parked-interim` entry** against **this** filing, replacing the hold against #15 — a new park with a
correct premise, not a continuation of the old one.

⚠ **Consequence for Cycle 14, recorded so nothing depends on this being quiet.** Build-3's acceptance
check (6) requires **both** live parks *"re-derived against the rules in force **and unwound**"* plus
`para_type_unknown`'s legal response executed on at least one named file. Under this disposition the
`extraction.md` half is re-derived but **not** unwound and the response is **not** executed, so
**check (6) FAILS, and it is `[ship-verifiable]` and GATES.** That is the honest outcome: the check
fails because the module is wrong, which is what an acceptance check is for. The alternative —
retyping 8 files to a value the vault believes false, in order to turn a gate green — is the failure
mode this whole cycle exists to name.

_Ship-verifiable at rest: a repair is gradeable against shipped convention source and a declaration
fixture, with no field event needed. The field half (the 8 files leaving `para_type_unknown` without
being falsified) rides the next full sweep after the repair._
