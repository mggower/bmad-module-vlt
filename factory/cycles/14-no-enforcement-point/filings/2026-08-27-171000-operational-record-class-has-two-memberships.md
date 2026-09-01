# The operational-record class has two different memberships in the same convention, one release old

_Filed 2026-08-27 from the **v0.17.0 upgrade post-flight** on `{field-vault}`
(`{upgrade_reports}/2026-08-27-1157-upgrade.yaml`, `parked_interims_review`) and confirmed at rest
against shipped source at `c02fe3d`. **This is a defect in Cycle 14 build-3, shipped hours earlier
the same day.**_

## The claim

`extraction.md` v8 names the operational-record class **twice, with different members**, and
`write-verification.md` v4's exemption follows the narrower one. A `charter` file is therefore a
recognized PARA `type:` **and** outside the class that recognition places it in.

| Site | Membership |
|---|---|
| `extraction.md:84` — the recognized `type:` set | *"the **operational-record class** `charter \| record \| register`"* |
| `extraction.md:190` — **the class's definition site** | *"`record` and `register` name an **artifact class**…"* — `charter` absent |
| `write-verification.md:55` — the attestation exemption | `record` / `register` — follows `:190` |

`:190` is the single home (*"cited there, defined here"*). `:84` is the operating contract's
Layer-3 entry condition target. They disagree about a member.

## Field measurement (this run, not synthesized)

29 unattested `author: agent|hybrid` Layer-3 files outside `{wiki}`: by `type:` — `area` 22,
`project` 3, `resource` 2, **`record` 1**, **`charter` 1**.

**Only the 1 `record` file is exempted. The `charter` file is not** — despite `:84` placing
`charter` in the class the exemption is written against.

## Why the shipped check did not catch it

Build-3's acceptance check (4) asserted **three-surface agreement**: the class is *named* at four
surfaces and *defined* at exactly one (`extraction.md:190`, one grep hit). Both halves are true.
The check tested **single-home-ness** — that only one site defines the class — and never compared
**membership** between the naming site and the defining site. A class can have exactly one
definition and still be named elsewhere with a different member list; that is this defect, and it
sits precisely in the check's blind spot.

## Why it matters

This is Cycle 14's own through-line reproduced by Cycle 14's own repair: the module states a rule
(the class), names one place responsible for defining it (`:190`), and a second site states the
rule differently — with no enforcement point comparing them. The cycle shipped a check for the
*shape* of single-home discipline and none for its *content*.

Concrete harm today: `write-verification.md`'s park in `{field-vault}` was resolved only partially,
and the post-flight names this as a reason — 28 of 29 files remain in jurisdiction.

## Candidate directions (capture will ground these)

1. **Decide which membership is intended** — the likelier reading is that `charter` belongs
   (`:84` states it deliberately, and a charter is dated, append-shaped and attributed per entry
   like the other two), making `:190` and the exemption the sites to repair. That is a
   `write-verification.md` rule change and a re-ack, not a prose fix.
2. **Give check (4) a membership comparison**, not only a definition-count — the enforcement point
   that would have caught this at rest.
3. Consider whether `moc` has the same latent problem: `:84` lists it among the artifact types, and
   nothing in this filing verified its treatment downstream.

## Bound

Ship-verifiable at rest — the three sites are readable on disk. No field event is needed to grade a
fix. Related: `{field-vault}`'s `write-verification.md` park (upstream filing #16) cannot fully
resolve while this stands.
