# Scope extraction.md's "retired as an extraction target" to extraction artifacts — it reads as a general closure of resources/

origin: mggower/bmad-module-vlt#10

- **filed:** 2026-08-24 (GitHub issue opened 14:28:22Z via the vlt-feedback rail)
- **origin vault:** vlt-core · **module_version:** 0.14.0 · **rail_contract:** 1 · **kind:** defect
- **materialized:** 2026-08-24 by the factory intake (github-intake)

---

### what_happened

`extraction.md`'s sentence retiring `resources/` reads, in practice, as a general closure of the folder rather than the scoped retirement of one destination role. A partner in this vault used it to block a proposed `type: research` write to `resources/` — a write the rule never governed — and reported that to the user as a hard blocker, killing a legitimate relocation.

The sentence is technically consistent as written: "extraction" means `vlt-extract` producing `type: project|area` artifacts, and the retirement is scoped to that. But it sits in the same breath as the statement that `resources/` is now the wiki's home, and the combination reads as "this folder is closed" rather than "this folder is no longer an extraction destination."

This is an editorial defect, not a rule defect. The rule is right; the prose does not carry its own scope to a careful reader.

### evidence

`_meta/conventions/extraction.md:81`:

> `resources/` is **retired as an extraction target** as of this version — it is now the wiki's human-browsable home (`{wiki}` defaults to `resources/wiki/`; the operating contract's structure map). Legacy `type: resource` artifacts predating this version stay legal at the `resources/` root indefinitely — no backfill sweep, no re-type (the coexistence posture below, extended to the retired type; the legacy sentence also covers their `status: complete`). Where reference material goes now: **the wiki itself** — the human-browsable `{wiki}` — or `areas/` when it serves an ongoing commitment.

Field trace: partner proposes relocating a vault-grown op skill's output shelf (`type: research` notes) from `_agent/{zone}/{sub}/` to `resources/{shelf}/`; partner greps the conventions, finds this line, cites "retired" as a blocker, and reports the move as illegal. It is not — no rule governed that write either way. The correct blocker turned out to be a different and genuinely open question, filed as the sibling issue, #11.

Proposed fix, editorial only: scope the retirement explicitly to extraction artifacts, and state what else may legally live at that root (or defer that to #11's ruling and point at it).

**Scoping note so the fix is not over-applied:** `extraction.md` is a handshaked convention, but per the standing module rule a prose clarification that changes no rule does **not** bump `version:` and does **not** re-ack consumers. This fix should not churn the handshake.

### provenance_guess

A guess, grounded where possible:

- `_meta/conventions/extraction.md:81` — the sentence itself.
- Shared root cause with the sibling issue: the 0.14.0 relocation of the wiki into `resources/` changed that folder from a PARA leaf into a mixed zone, and the surrounding prose and rules were not revisited as a set. This sentence is the convention-side symptom.
- Sibling on the same root, already captured module-side: **A11-5** (the 0.14.0 wiki-relocation migration walked no vault-local overlay). Related, not a duplicate — that one is the migration's blast radius, this one is the prose left behind.

### kind

defect

### origin_vault

vlt-core

### acceptance_vault

Any vault with the 0.14.0+ governance bundle installed. Acceptance is a read test, not a behavior test: a partner reading the amended sentence cold should be able to answer "may a non-extraction artifact live at the `resources/` root?" without consulting the operating contract. That question's *answer* belongs to the sibling issue #11; this issue's acceptance is only that the sentence stops implying one.

### module_version

0.14.0

### rail_contract

1
