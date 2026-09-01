# `class: supersession` — the PARA `type:` enum is location's last proxy for trust

origin: mggower/bmad-module-vlt#17

⚠ **This `origin:` header was HAND-WRITTEN, not intake-written (2026-09-01, owner-ruled).**
`skills/vlt-feedback/references/field-contract.md` assigns the header to the factory intake — *"the
intake writes it; nothing else does"* — because it is the **idempotency key**. This filing was
written factory-side **first** and posted to the rail afterwards, a direction the contract has no
route for: it assumes issue → filing, never filing → issue. Without the key, Cycle 15's
`github-intake` would materialize issue #17 as a **second copy** of this file. The header is
therefore written by hand to preserve exactly the property it exists for, and the deviation is
recorded here rather than left to be inferred. **Do not re-materialize.**


_Filed 2026-09-01 from **`{field-vault}`**, on the owner's re-reading of
`_output/problem-solution-2026-08-25.md` (gitignored; provenance only) against three days of Cycle 14
work. **Cites `ST-2` — location as proxy for trust — which is `status: standing`.** This filing is
the RC1 remainder that `ST-2` names and that Cycle 12 half-retired._

⚠ **This is a `supersession` filing, not a defect filing** (`factory/inbox/README.md`, *When the
filing is not a defect*). It asks for a **retirement**. It carries both required halves below. **It
supersedes `factory/inbox/2026-08-31-152000-…`**, which reported the same friction as a defect and
proposed a new mechanism — *"a filing that ends in a new carve-out has diagnosed the symptom,"* and
that one did. That filing should be **withdrawn at capture** in favour of this one; its grounding
(the `{wiki}` asymmetry, the accuracy inversion, the measured population) is reproduced here and is
not lost.

---

## Half 1 — the rule now redundant

**Site:** `skills/vlt-setup/assets/governance/_meta/conventions/extraction.md:84` (`version: 9`),
restated at `skills/vlt-lint/references/checks.md:19` as legal-response case **(b)**.

**The rule, verbatim:**

> A module-canonical but **non-PARA** `type:` (`wiki`, `research`, `session`, `note`, `idea`) sitting
> in a PARA folder is therefore a **mis-typed or mis-placed artifact** … retype it to the target
> folder's `type:` … or relocate it to that type's home zone — **never to declare module vocabulary
> as vault-grown overlay schema.**

Plus its sole exception, stated as a singular at four sites — *"one carve-out **by name**: the
`{wiki}` subtree under `{resources}`"* (`vault-operating-contract.md:70`; also `:41`,
`extraction.md:80`, `extraction.md:84`).

**What it was standing in for.** The same thing `ST-2` names for `author:` and `trust:`: **the
folder asserting a property the file already declares.** Here the property is *what the artifact
is*. When the contract was authored this proxy was necessary — the honest fields carried no
enforcement, so location was the only protection available. `ST-2`'s RC1, applied to the third field
of the quartet.

**Why it is redundant now, and not merely inconvenient.** Cycle 12 retired the proxy for the other
two. PARA's entry condition became *honest, attested frontmatter* rather than *a named surface*, and
the owner ruled `trust: raw` acceptable in browsable space (2026-08-25). A file at a PARA address now
declares **who wrote it** (`author:`), **how far to trust it** (`trust:`), and **that its writer ran
its verification pass** (`verified_by:`/`verified_at:`) — each checked, across the whole PARA
population, by a shipped net.

**`type:` is the one field of that quartet whose declaration its folder still overrules.** Three of
the four are believed when honest; the fourth is believed only if the folder approves the noun.

**And the rule inverts against accuracy.** The overlay route stays open for *vault-grown* vocabulary
and is closed **only** to the module's own words. So a vault typing agent-written periodicals
`dispatch-brief` is conformant today, and `{field-vault}` — which typed them `research`, the module's
own accurate word for a dated, single-pass, `trust: raw` snapshot (`extraction.md:28-30`) — is
permanently not. **A recognized-vocabulary rule that punishes correct vocabulary has stopped serving
its stated purpose.**

---

## Half 2 — the mechanism that supersedes it

Two mechanisms, both shipped, whose populations are stated rather than assumed.

**(i) The `para_*` honesty nets — same population, same modes.** `checks.md:19-20` ships
`para_type_unknown`, `para_author_unknown`, `para_status_unknown` and `para_writer_unauthorized`
over *"files under `{projects}`, `{areas}`, and `{resources}`"* in **both modes**. **Cycle 11 build-2
(`8290416`) extended them across the entire PARA population**, which is the event `ST-2` identifies
as the one that made the proxy redundant — and which shipped the nets *beside* the prohibition
rather than *in place of* it. Population coverage is exact: the nets judge the identical file set the
enum governs.

**(ii) Declare-at-birth — the same enum's own escape, already trusted.** `extraction.md:84` already
admits *"any vault-declared schema in `{overlays}/extraction.overlay.md`"* **into the closed set**.
The mechanism for a vault to say *"this value is legal here, and I am on record saying so"* exists,
ships, and is relied upon. The prohibition does not doubt the mechanism — it carves one class of
value out of a route it otherwise accepts.

**What the retirement is, precisely.** Retire the **prohibition** at `extraction.md:84` and
`checks.md:19` case (b) — *"never to declare module vocabulary as vault-grown overlay schema."*

⚠ **`para_type_unknown` is NOT retired and this filing does not ask for that.** A genuinely
undeclared value (`type: banana` at an `{areas}` address) must still land loud. The net keeps its job;
it stops being fed a rule that answers a question the file already answered honestly. **Retiring a
prohibition is not retiring its enforcement** — that distinction is the whole of this filing's ask.

**And the `{wiki}` carve-out is retired with it, in the same act.** Once a vault can declare that a
subtree carries a `type:`, `{wiki}` is **the module's own shipped first instance of that
declaration** rather than a name written into four rules. The contract's *"one carve-out by name"*
becomes a default entry, not an exception. ⚠ **This half is not optional.** Retiring the prohibition
while leaving `{wiki}` a named exception converts a category back into an allowlist — *"four
exceptions, zero categories"* is `ST-2`'s measured failure mode, and it is what a minimal scoping of
this work produces. **A build that ships half of this has shipped pass five.**

---

## Why this filing exists now, and what it is correcting

**Cycle 14 build-3 (`e42429d`, v0.17.0) did not inherit this rule — it restated and strengthened
it.** `extraction.md:84`'s closed-set statement and its by-name `{wiki}` removal are build-3's own
text, shipped six days after `ST-2` was opened and P-15 shipped the vocabulary for retiring exactly
this. **The invariant was reinforced by a build in the very cycle whose thesis is that rules without
enforcement points do not bind.**

**And the loop then did what `ST-2`'s RC2 predicts.** Over three days this friction produced: a
defect filing (`2026-08-31-152000`), an owner-ruled hot-fix brief (build-6) explicitly **scoped
minimal** with the `{wiki}` unification cut out, and a drafted `deviation` recording the sibling
exception rather than retiring its rule. Three perimeter moves, each defensible on its own terms.
`ST-2` RC2 contributing factor 3 names the mechanism: *"the repo's own governance quality biases
toward perimeter patches … they make the minimal patch the rational move every time — which is
exactly how a root cause survives four cycles."*

**Build-6 is withdrawn on this filing**, and this is the first use of P-15's `supersession` class —
the rail built on 2026-08-25 for this exact purpose, unused for a week while the thing it was built
for happened again.

---

## The sibling instance, named not folded

**Park #16's `verified_by` roster is the same shape and should be ruled in the same cycle, not the
same build.** `write-verification.md:47` closes the value set to write ops, so a partner authoring a
Layer-3 document during a sanctioned sitting can satisfy every clause of the entry condition except
that one — the same *closed list standing in for an honesty property*. ⚠ Cycle 14 build-5 shipped
`write-verification.md:55` v5 naming the disease in its own words — *"fusing permission to provenance
is the write-path failure this exemption exists to prevent"* — **while writing another instance of
it.**

It is **named here and filed separately** because its retirement is a different act with a different
population (an attestation roster, not a vocabulary), and folding two retirements into one build is
how a structural change becomes unreviewable. Capture should route both to the same ideation.

---

## Field evidence

- **146** files under `resources/wiki/` carry `type: wiki` — legal solely by the by-name removal.
- **9** files under `resources/briefs/` across 3 subscriptions carry `type: research` — a standing
  `para_type_unknown` finding. ⚠ **The population moved 5 → 8 → 9 in three days** (2026-08-26 park →
  2026-08-31 → the 2026-09-01 sweep, which reads *"UP FROM 5"*). The park's scope is the `type:`, not
  the count, so nothing here moves its ruling — but the cost of leaving it unruled compounds.
- The producer is the vault-local `vlt-brief` (`SKILL.md:63`), writing the research schema. **Not a
  defect in the capability:** under this retirement its current line is correct, and under the
  current rule there is no value it could write that is both accurate and legal.
- **Both stated legal responses require writing something false**, and the vault has refused this
  class of move once already — park #16 declined to stamp a rostered `verified_by` on a file that op
  did not write, and build-5 then **ratified that refusal in the convention text.**

## Grounding against current module source (v0.17.1)

`extraction.md:84`, `:80`, `:28-30`, `:11` (`version: 9`) · `vault-operating-contract.md:41`, `:70`,
`:60-68` (the three layers and the Layer-3 entry condition) · `vlt-lint/references/checks.md:19-20` ·
`write-verification.md:47`, `:55` (`version: 5`) · `module.yaml:45`, `:67` (`{wiki}` as a declared,
overridable path — the mechanism a declared typed subtree would reuse) · Cycle 11 build-2 `8290416`
(the nets extended across PARA) · Cycle 14 build-3 `e42429d` (the restatement) ·
`factory/studies/ST-2-location-as-proxy-for-trust.md` (`status: standing`).

_Ship-verifiable at rest: a retirement is gradeable against shipped convention source and a
declaration fixture, with no field event. The field half — the 9 issues leaving `para_type_unknown`
without being falsified, **and a control still reporting** — rides a **scoped** `vlt-lint` run over
`resources/briefs/`, not a full sweep: `checks.md:19` puts the `para_*` nets in both modes._
