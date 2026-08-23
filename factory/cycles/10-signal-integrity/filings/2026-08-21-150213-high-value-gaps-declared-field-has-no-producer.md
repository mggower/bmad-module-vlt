# Produce high_value_gaps in the full-mode fan-out, or make "unmeasured" expressible — the declared field has no producer

origin: mggower/bmad-module-vlt#5

- **filed:** 2026-08-21 (GitHub issue opened 15:02:13Z via the vlt-feedback rail)
- **origin vault:** app-vault · **module_version:** 0.12.0 · **rail_contract:** 1 · **kind:** defect
- **materialized:** 2026-08-22 by the factory intake (github-intake)

---

### what_happened

The lint report schema declares a full-mode field that the full-mode producer cannot fill.

`skills/vlt-lint/references/report.md` declares, in the report schema:

```
high_value_gaps: [<concept>, ...]     # full mode
```

The `# full mode` annotation means this field is expected precisely when the sweep runs through the
fan-out workflow. But `workflows/vlt-lint-full.js` — the full-mode fan-out — has no gap-candidate
field in its page-scan schema, does not ask for one in the scan prompt, and computes none in its
reduce step. The identifier `high_value_gaps` appears **nowhere** in the workflow.

So the slot is structurally unfillable in the only mode that requires it. A full sweep either omits
the key (reading as "no gaps found") or emits an empty list (reading as "measured, found none") —
when the truth is "never measured".

### evidence

Grepping the identifier across the shipped tree returns exactly one hit — the declaration itself:

```
skills/vlt-lint/references/report.md:  high_value_gaps: [<concept>, ...]     # full mode
```

No occurrence in `workflows/vlt-lint-full.js` or in `skills/vlt-lint/SKILL.md`.

Observed on a real `--full` sweep: the field had to be hand-annotated `NOT PRODUCED — unmeasured this
run, not empty` to keep the report honest, because neither of the two shapes the schema permits could
say that.

This is the honest-reporting failure the module's own never-omit rule exists to prevent, one layer
up: the rule ensures a line is never dropped, but an unfillable line reduces to the same misread.

### provenance_guess

**A guess — please ground it.** Three coherent resolutions, and the choice is a design call:

1. **Implement it** — add a gap-candidate field to the fan-out's page-scan schema and reduce, so the
   declared field is actually produced.
2. **Retire it** — drop the field from the report schema if high-value-gap detection was never
   intended to survive into the fan-out.
3. **Make "unmeasured" expressible** — keep the field but give the schema a third value distinct from
   empty, so a mode that cannot measure it says so rather than implying zero.

(3) generalizes beyond this field and matches the module's stated posture on never letting an absence
read as a finding of none.

Adjacent, same file: the Gap B scoping defect filed separately. Distinct mechanism — that one is a
check measured against the wrong rule, this one is a declared output with no producer — but both
surfaced from the same sweep and both touch `vlt-lint-full.js`.

### kind

defect

### origin_vault

app-vault

### acceptance_vault

Any vault large enough to route `--full` to the fan-out. Expected after fix: a full-mode report either
carries a produced value or states unmeasured explicitly.

### module_version

0.12.0

### rail_contract

1
