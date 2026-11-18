# The rail's `kind` set has no value for a supersession — P-15 shipped a filing class the transport cannot classify

_Filed 2026-09-01 from the factory, during the posting of the loop's first two `class: supersession`
filings to the remote rail (issues **#17** and **#18**). **`kind: candidate`.** This filing carries no
`origin:` header and is **not** rail-materialized — it is factory-observed, not vault-observed._

⚠ **Routing note, decided before filing rather than left to capture.** This is **cycle-roadmap work,
not platform**, because the majority of its surface is shipped. The channel boundary is explicit —
*"Anything under the shipped surface (`skills/vlt-*`, `.claude-plugin/`) belongs on the arc roadmap,
**no exceptions**"* — and the platform ledger's own **[P-10]** entry says the same thing in its
out-of-scope: *"any change to the field contract or its labels (shipped surface → arc roadmap)."*

---

## What happened

The module has **four** filing classes and its transport carries **three**.

`factory/inbox/README.md` defines a **`supersession`** filing (shipped by platform **P-15**,
2026-08-25): a filing that says *this protection is now redundant, because X now enforces what it was
standing in for.* It is not a defect, not a pattern, and not a candidate — the README is emphatic that
it *"asks for a **retirement**, not another exception"*, and that it carries two mandatory halves no
other class requires.

The remote rail's classification vocabulary was never extended to match. `kind` remains
`defect | pattern | candidate`.

**Observed in anger 2026-09-01**, posting the class's first two real instances: both had to be filed
`kind: candidate`, and both carry an apologetic classification note in the issue body explaining that
the value is a nearest fit rather than the truth. **A classification that has to be explained in prose
is not doing its job** — and the explanation lives in the body, where neither the label filter, the
issue-form router, nor `issue-triage`'s classification check can read it.

## Why it matters beyond tidiness

1. **`issue-triage` cross-checks `kind` against the `field:*` label and treats the body's `kind` as
   authoritative.** With no supersession value, that check can only ever confirm a wrong answer.
2. **A retirement ask and an upstream-this proposal want opposite triage instincts.** A `candidate`
   is graded *is this worth adding?* A supersession is graded *is this still earning its place?* —
   and the second question, per P-15's own filing, is the one the loop had no way to process at all
   until a week ago.
3. **P-15's stated risk is this exact shape:** *"the rail ships and never fires — added, then
   ignored, indistinguishable from working."* A class the transport cannot name is a class the
   transport will under-report.

## The sites — five, and they straddle the channel boundary

| Site | Change | Channel |
| --- | --- | --- |
| `skills/vlt-feedback/references/field-contract.md` | the `kind` row's value set, and a `field:supersession` row in the label table | **shipped → cycle** |
| `skills/vlt-feedback/` (the composer) | emit the new value | **shipped → cycle** |
| `.github/ISSUE_TEMPLATE/` | **a fourth form.** Each existing form hard-codes one kind: `field-candidate.yml:40-46` is a single-option dropdown, and `:7` hard-codes `labels: ["vault-filed", "field:candidate"]`. There is no shared dropdown to widen | repo-side → platform |
| the tracker's label set | a `field:supersession` label | shipped (defined in the contract table) |
| `.claude/skills/issue-triage/` | the classification check's value set | platform |

## Grounding against current module source (v0.17.1)

- `skills/vlt-feedback/references/field-contract.md` — §The payload field set (`kind`: *"`defect` …
  `pattern` … `candidate`"*), §The label set, §Contract version.
- `factory/inbox/README.md` — *When the filing is not a defect — `supersession`*, and its two
  mandatory halves.
- `.github/ISSUE_TEMPLATE/field-defect.yml`, `field-pattern.yml`, `field-candidate.yml` — one form per
  kind, `labels:` hard-coded at `:7`, `kind` a fixed single-option dropdown.
- `factory/platform/roadmap.md` §P-15 (CLOSED 2026-09-01), §P-10 out-of-scope (the routing rule).
- Live instances: tracker issues **#17** and **#18**, both `field:candidate`, both carrying the
  classification note.

## The ask, and its bound

**Additive only — this is deliberately not a contract break.** The contract's evolution rule:
*"adding a payload field does **not** bump `rail_contract` … adding a label is additive (no bump)."*
So the whole change lands **without** a `rail_contract` bump and **without** invalidating a single
filed issue. ⚠ *(Noted because the platform ledger's P-10 entry states the routing correctly but
over-states the bump — corrected there 2026-09-01.)*

**Not asked for:** a fifth class, any change to what the three existing kinds mean, or any change to
the two mandatory halves the README already defines. **Ship-verifiable at rest:** the value set agrees
across all five sites, and a filed supersession routes to its own form and label without a
classification note in its body.

⚠ **Cheap fix, and the honest reason to do it now rather than later:** Cycle 15's ideation is already
scheduled to rule two supersession retirements (#17, #18) at the roundtable's obsolescence beat. That
is the first cycle where the class carries real weight — and the run where the missing vocabulary will
be most visible.
