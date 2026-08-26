# State which convention's type: vocabulary the Layer 3 entry condition means — frontmatter.md ships a non-exhaustive list, extraction.md ships a closed set

origin: mggower/bmad-module-vlt#15

- **filed:** 2026-08-26 (GitHub issue opened 12:55:29Z via the vlt-feedback rail)
- **origin vault:** vlt-core · **module_version:** 0.16.0 · **rail_contract:** 1 · **kind:** candidate
- **materialized:** 2026-08-26 by the factory intake (github-intake)

---

### what_happened

0.16.0 replaced Layer 3's location test with an **entry condition**: partner-touched content reaches PARA by carrying honest, attested frontmatter — an honest `author:`, an entitled `trust:` rung, **a recognized `type:`**, and the write-verification attestation pair — plus admission by the nearest declaring ancestor charter's `writers:`.

Three of those four legs name their own home. The fourth does not. **"A recognized `type:`" does not say recognized by which convention — and the module ships two conventions that answer differently.**

- `frontmatter.md` states the `type:` list is **non-exhaustive** and names `research` among its canonical values.
- `extraction.md` / the lint check `para_type_unknown` define a **closed** recognized set for the PARA population: the artifact types `project|area|resource|moc`, the container types `charter|record|register`, and any vault-declared schema in the extraction overlay.

A file carrying a type that is canonical under the first and absent from the second is simultaneously well-formed and a loud finding. Nothing in the contract picks a winner.

**Why this bites now rather than before.** Under the retired location rule the question could not arise: an agent-lane type never reached PARA, because agent-lane *files* never did. 0.16.0 made the write legal on domain, surface and posture — and the type vocabulary is the one leg that did not move with it.

**The precedent that shows a general mechanism is missing.** The module already met this exact shape once: a Layer-2 subtree living at a browsable `{resources}` address. It solved it by **removing that subtree from the PARA population by name at population time** — explicitly "by name, never by location," so no type check ever runs on it. That is a correct solution for the one case shipped, and it is **hard-coded to that one case**. A vault that lands a second agent-lane subtree at a browsable `{resources}` address has no general form of the same move available: it can retype its files away from the vocabulary its own lane uses, or declare a local overlay answering — quietly, locally, permanently — a question that looks like it wants a module answer.

**This is an ask for a ruling, not a proposed answer.** Any of these is usable; the current silence is not:

1. The entry condition's "recognized" means `frontmatter.md`'s non-exhaustive list, and the closed PARA set is narrowed to a *status-enum* concern rather than a type gate.
2. The closed set is authoritative, and `frontmatter.md`'s non-exhaustiveness is scoped explicitly to the agent lane — with the overlay declaration named as the intended and expected route for a vault-grown lane.
3. A general carve-out mechanism, so a declared agent-lane subtree at a `{resources}` address can be excluded from the PARA population the way the shipped one is — the by-name exclusion generalized to a declared list.
4. Ruled working-as-designed: overlay-declare it, every time, and the two conventions are consistent once read in the intended order.

### evidence

Composed from three shipped surfaces:

- **The operating contract, Layer 3** — the entry condition, requiring "a recognized `type:`" without naming the recognizing convention.
- **`frontmatter.md`** — "The `type:` list is **non-exhaustive.** Canonical values include `wiki`, `research`, `session`, `note`, `project`, `area`, `resource`, `idea`, and the PARA container files…"
- **`extraction.md` / the lint checks reference** — `para_type_unknown`: "a file in the population carrying a `type:` outside the recognized set (the artifact types `project|area|resource|moc`, the container types `charter|record|register`, and any vault-declared schema in `{overlays}/extraction.overlay.md`)".
- **The same checks reference, the population rule** — the PARA population is files under the three PARA keys "with the `{wiki}` subtree under `{resources}` excluded **by name, never by location**".

Compose the first two: `research` is canonical under `frontmatter.md` and outside the recognized set under `extraction.md`. Compose the third: the module's own answer for an agent-lane subtree at a browsable address is a by-name population exclusion, available to exactly one subtree.

**Live instance that forced the question.** This vault runs a vault-grown scheduled op that publishes periodical issues to an output shelf. The issues are agent-authored and carry `type: research`, honest `author: agent`, `trust: raw`, and the attestation pair. The shelf was parked in the agent zone pending the ruling on #11; 0.16.0's retirement of the location and surface-count prohibitions cleared every axis of that park **except** the type vocabulary. Moving the shelf to a `{resources}` address today puts a growing set of well-formed, honestly-attested, correctly-typed-for-their-lane files into the PARA population as recurring `para_type_unknown` findings. The vault is proceeding under a recorded `parked-interim` against this filing rather than resolving the conflict locally by overlay, because a local overlay would be a vault answering a module-level question.

### provenance_guess

A guess, grounded where possible:

- The operating contract, *The three layers and the hard write boundaries*, Layer 3 — the entry condition clause carrying "a recognized `type:`". This is where the pointer is missing.
- `frontmatter.md`, the `type:` section — the non-exhaustiveness claim.
- `extraction.md` v7 plus the `vlt-lint` checks reference, `para_type_unknown` — the closed set.
- The `vlt-lint` checks reference, the `para_*` population rule — the by-name `{wiki}` exclusion, i.e. the precedent.
- **Root cause guess:** 0.16.0 moved the entry condition from location to attestation and walked `author:`, `trust:` and the attestation pair to their homes, but `type:` inherited a recognized-set that had only ever been read against PARA-native files. Before 0.16.0 no agent-lane type could reach the population, so the two conventions never had to agree.
- **Lineage:** downstream of #11 and of the Cycle 12 A12-3 residue that issue's owner comment names ("PARA using location as a proxy for trust"). Related, not a duplicate — #11 asked which zone, its ruling answered which surface, 0.16.0 answered on what discipline, and this asks under whose vocabulary.

### kind

candidate

### origin_vault

vlt-core

### acceptance_vault

Any vault with the 0.16.0+ governance bundle. Acceptance is that a partner about to file an honestly-attested, agent-lane-typed artifact into PARA can determine from the bundle alone whether its `type:` is recognized — without escalating to the user, and without the answer depending on which of two conventions it happens to read first. A ruling of "overlay-declare it, always" satisfies this as fully as a ruling that widens the set, provided the contract's entry condition points at the convention that owns the answer.

### module_version

0.16.0

### rail_contract

1

