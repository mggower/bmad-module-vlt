# Reconcile Layer 3's open entry condition with write-verification's closed verified_by roster

origin: mggower/bmad-module-vlt#16

- **filed:** 2026-08-26 (GitHub issue opened 14:14:18Z via the vlt-feedback rail)
- **origin vault:** vlt-core · **module_version:** 0.16.0 · **rail_contract:** 1 · **kind:** defect
- **materialized:** 2026-08-26 by the factory intake (github-intake)

---

### what_happened

The Layer 3 entry condition and `write-verification.md`'s attestation contract disagree, and the
disagreement makes a legal write impossible to complete.

The operating contract draws Layer 3's boundary as an **entry condition, not a list of doors**, and
says so explicitly — it names extraction and container maintenance as shipped dispositions and then
states:

> they are the shipped set, **not** a closed one: another verb filing an honest, attested document
> under the condition above is legal.

One of the conditions it requires is "the write-verification attestation pair".

`write-verification.md` §Attestation then closes that pair's value set to a named roster:

> the `verified_by` value set is this file's `consumers:` **that are write ops**, plus write-op
> `local_consumers:` registrants... The roster is **membership and ceiling**, never an automatic
> grant.

So the contract says the set of legal writers is open; the attestation contract says the set of
legal attesters is closed, and it is closed to **operation skills**. A partner that writes a Layer 3
document during an ordinary sitting — not by running one of the shipped write ops — satisfies every
other clause of the entry condition (honest `author: agent`, an entitled `trust:` rung, a recognized
`type:`) and then has no value it may honestly put in `verified_by`. Every value on the roster names
an op that did not write the file.

**A partner writing legally to Layer 3 cannot satisfy the condition of its own legality.**

This surfaced when one partner's health check flagged another partner's planning document as missing
attestation and relayed it with two closing routes — "re-run your tier-1 verify pass and write
`verified_by: <your op>`, **or** rule the file human-authored". Neither is available: the writing
partner has no op (the document was authored in a facilitated ideation sitting), and the file is
genuinely agent-authored, so the human-authored ruling would be false. The relay was written in good
faith by a partner reading the same shipped rules; the gap is in the rules, not the relay.

Note the failure is **silent in one direction only**: the flagged partner can either fake a
provenance claim or leave the finding permanently open. Nothing in the shipped rules tells it which,
and the cheaper of the two is the dishonest one.

### evidence

Measured in the origin vault before filing, not asserted:

- **27** Layer 3 files outside the wiki subtree carry `author: agent|hybrid` with **no** attestation
  pair — spread across six different partners' domains, in `{projects}/{container}/{file}.md` and
  `{areas}/{container}/{file}.md`.
- **5** Layer 3 files outside the wiki subtree **do** carry the pair. **All five were written by an
  operation skill.**
- **Zero** partner-sitting-written Layer 3 documents in the vault are attested, and under the
  current value set none can be.

The population is not an artifact of one careless partner: it includes documents from the module's
own shipped partner roster and from vault-minted partners alike, produced by ordinary sanctioned
work over roughly ten weeks.

Reproduction needs no vault history — it is a rules read:

1. Have a partner write a document to a `{projects}` or `{areas}` container during a normal sitting,
   under the entry condition (honest `author: agent`, entitled `trust:`, recognized `type:`).
   The contract's "not a closed one" clause makes this legal.
2. Apply `write-verification.md` §Attestation. No legal `verified_by` value exists.
3. Run the health check. The file is in jurisdiction per §Scope rule (self-marker) — it carries vault
   frontmatter with `author: agent`, and it is not a bare human file, a daily note, or a container
   record — so it is flagged, with no route to clear the flag.

### provenance_guess

A guess, not a finding — the factory should ground it:

- `_meta/conventions/write-verification.md:47` — the `verified_by` value set bullet. The
  ops-only qualifier ("this file's `consumers:` **that are write ops**") is the clause that closes
  the set.
- `_meta/vault-operating-contract.md:66` — Layer 3's entry condition, including both the
  "attested frontmatter" requirement and the "not a closed one" clause that authorizes non-op verbs.
- `_meta/conventions/write-verification.md:54` — §Scope rule (self-marker), which puts the
  resulting files in the health check's jurisdiction. Its existing exemptions (daily notes, raw
  source deposits, human-authored Layer 3 files) are the natural place for a jurisdiction-shaped fix.
- `_meta/conventions/extraction.md:188` — the container-file attestation carve-out
  ("operational records, not knowledge artifacts... they carry **no** pair"). **This is precedent for
  the cheaper fix**: the module has already ruled one class of Layer 3 file out of attestation
  jurisdiction rather than inventing a value for it.

Two directions, both cheap; the maintainer's call which is right:

1. **Widen the value set** so a non-op partner write has an honest value — e.g. admit a partner
   identifier, or a sentinel meaning "verified in-sitting by the authoring partner". Keeps every
   Layer 3 artifact attested, but weakens the field's current meaning (an op name) and needs a story
   for what the value is checked against.
2. **Narrow the jurisdiction** so partner-sitting writes are exempt the way container files already
   are, and say so in §Scope rule. Cheaper, has shipped precedent, and is honest about what the pair
   actually records today — that a *write op* ran its checklist. Cost: a real class of Layer 3
   artifact stops being covered by any structural check.

Worth noting for triage: this may be the same shape as the open filing about the decision log's
Writers roster having no route for a shipped write op that legitimately discovers a deviation
mid-run. Both are **a closed roster meeting an actor the surrounding rules authorize.** If two
instances is enough to make it a pattern, the pattern is worth naming once rather than patching each
roster as it is hit. Filed as a `defect` rather than a `pattern` because this instance blocks a
concrete write today; the maintainer may prefer to reclassify.

### kind

defect

### origin_vault

vlt-core

### acceptance_vault

Any vault with at least two partners and at least one `{projects}` or `{areas}` container holding a
partner-authored document that was not produced by a shipped write op. Acceptance is a rules read
plus one health-check run — no domain content and no vault history is needed to reproduce it.

### module_version

0.16.0

### rail_contract

1

