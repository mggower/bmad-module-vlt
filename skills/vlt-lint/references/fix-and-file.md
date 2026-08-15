# vlt-lint — reference: Steps 3+4 — fix and file

Read on reaching Step 3 (the router's Standing rules govern every write).

## Step 3: Auto-fix the safe issues

Fix directly (bump `last_updated` on any page you substantively edit — e.g. adding a callout; skip the bump for trivial formatting):

- **Index drift** — add missing pages (structural row + right category per `{conventions}/wiki-index.md`), remove non-existent ones, move resolved stubs out of `## Stubs`; set the index `last_updated`. Do **not** add or "correct" source counts/dates — the index doesn't carry them.
- **Frontmatter / Bases-field drift** — a `category:` with a clear typo for an existing H2 → repoint it. A `topic:` still in old delimited-string form (`a / b` or `a, b`) → convert to a YAML list (general→specific, lowercase) — on **wiki pages and `{research}` notes** alike (`topic:` is a list in both schemas). A missing `summary:` on a page with enough to summarize → draft one ≤160 chars. **Flag, don't mutate:** a `category:` that fits no existing H2 (needs a structural index decision) → `flag_for_human`.
- **Broken wikilinks** — repoint renamed targets; remove links to targets that clearly won't exist.
- **Formatting** — standardize frontmatter and required sections.
- **Unmarked supersession/stale callouts** — add them per the convention.

**Attest what you touched (lint-as-attester, narrowly):** on every file this step's auto-fix substantively edited, re-run tier-1 and write `verified_by: vlt-lint` + `verified_at: <today>` — the auto-fix bumped `last_updated` and would otherwise re-stale the attestation just validated. Never attest a file you merely read (contract: `{conventions}/write-verification.md`).

Do **not** auto-apply anything on the **never-auto-apply list** (router, Standing rules); the adjudicable-contradiction and merge filings land in Step 4 below.

**Write through a lint-time ruling (lint-as-recorder, narrowly):** when a human rules on a governance finding *during a sweep* (overlay-vs-upstream on a base divergence, retire-vs-keep on an orphan overlay), append the ruling to `_agent/mint/decision-log.md` in the shape single-homed at `{conventions}/decision-log.md` — follow it; do not restate the entry mechanics here. A changed disposition is a new entry carrying `supersedes:` — the existing idiom, unmodified. This is recording a human's decision, never lint deciding — the never-auto-apply list above is unchanged — and the write-through **never stamps `adoption_first_instance:`** (the stamp is the authorized ceremonies' — the authority rule, `vlt-mint`, Step 4; `vlt-lint` never writes it). Report each write in `rulings_recorded:` (Step 5) — a write no surface reports is a silent write.

## Step 4: File maintenance backlog items

**The address axis comes before the kind split** (the address rule: `{conventions}/frontmatter.md`, *The address rule*): when an item's bounded closing act **names another partner's act** (e.g. it needs an external source the vault doesn't hold → the Researcher), it is **relayed**, not filed — `vlt-dispatch relay`, shape `ask`, the `ref` naming the question. When the vault's own pages settle it → `maintenance` to `{backlog}`; when nobody can say what closes it → `knowledge-gap` to `{backlog}`.

For each near-duplicate/merge candidate (and any other maintenance worth doing later), append a `maintenance` item to `{backlog}` under `## Open`, then **mention it in-flow** (capture is cheap and never silent):

```
- [ ] Merge <page-a> + <page-b> (maintenance, by: <partner>) — near-duplicate: <signal, e.g. slug stem + 4 shared wikilinks>
```

For each contradiction dispositioned **`adjudicable`** (Step 2 / `{conventions}/wiki-supersession.md`), apply the address axis first — needs a source the vault doesn't have → **relay** (shape `ask`) to the partner whose act closes it; otherwise append its item (`maintenance` when the vault's own pages settle it, `knowledge-gap` when nobody can say what closes it):

```
- [ ] Adjudicate <page-a> vs <page-b>: <the claim in conflict> (maintenance|knowledge-gap, by: <partner>) — closes when: <the bounded act from the callout>
```

Record the filed item — or the relay (`ask: <ref>` and its recipient) — back in the callout's `**Filed:**` line, so the page and the record agree.

For each **entity collision** (Step 2, tier 2), append its item too:

```
- [ ] Verify "<name>" — <page-a> records <A>, <page-b> records <B> (knowledge-gap|maintenance, by: <partner>) — suspected substitution in a machine-transcribed source; closes when: <the name is confirmed against a non-transcribed source, or the claim is recorded without it>
```

Same address-first routing: closing it needs a source the vault doesn't have (a roster, a credited transcript — the usual case) → **relay** (shape `ask`) to the partner whose act closes it; the vault's own pages settle it → `maintenance`; nobody can say what closes it → `knowledge-gap`. **No `**Filed:**` back-write** — there is no callout to write back into, which is the distinguisher showing through: this class produces no contradiction callout by design.

For each **spec candidate** (Step 2, the governance check), append its item too — the named owner and closes-when come from the beat's single home (`{conventions}/spec.md`, *Promotion from candidate*):

```
- [ ] Promote <handoff-doc> to {specs} (maintenance, by: <owning partner>) — spec_candidate: <signal, e.g. 2 relay entries>; closes when: promoted per {conventions}/spec.md *Promotion from candidate*, or declined with reason recorded
```

**Guard:** an existing item for the same doc — open → mention it in-flow, never file a second (the duplicate-filing posture above); closed as **declined** → do not re-file (the recorded decline is honored; the count of honored declines is stated beside the finding in Step 5).

**Duplicate-filing guard for callout-seeded findings:** for a finding marked `(callout-seeded)`, first read the seeding callout — if it records an existing `{backlog}` item (a "Tracked in" / "Filed" line) and that item is still open under `## Open`, do **not** file a second; mention the existing item in-flow instead. If the callout claims tracking but no open item exists, file one and note the mismatch. The no-`**Filed:**`-back-write rule above stands for *unseeded* findings; a seeded finding's callout is the vault's own record and is left as the page's author wrote it. The guard extends across rails: an **open relay pointer for the same question** (same key — the relay idempotency rule makes this checkable) counts as "already filed" — mention it in-flow, never file or relay a second.

The merge itself is resolved later by `vlt-ingest` under the consolidation discipline — lint finds, ingest resolves. An adjudicable contradiction resolves the same way when it needs a source (`vlt-ingest`, holding the new source, applies the supersession rules); when the vault's own pages already settle it, the owning partner resolves it in ordinary work. Either way the callout's disposition is updated or the callout removed when the contradiction is gone — **that is the state transition contradictions previously lacked.**
