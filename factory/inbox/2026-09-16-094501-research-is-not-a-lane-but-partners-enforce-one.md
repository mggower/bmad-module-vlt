# `{research}` is not a shared lane, but partners enforce one — the lane status is unstated and the belief lives in memory

_Filed 2026-09-16 by the **factory**, from an owner problem-solving session (`bmad-cis-problem-solving`)
and a same-day roundtable (`bmad-party-mode`); session artifact gitignored. Evidence is module source at
`caea0d5` plus the owner's field observation. Kind: `candidate`. Cause: **`ST-9`**
(`factory/studies/ST-9-one-axis-design-leaves-the-diagonal-empty.md`, cause B + amplifying) — cited,
not restated. Owner elected to file._

## The claim

Partners in the field decline research mid-task with *"that's the Researcher's lane"*. No rule says
it. `vlt-research` is an operation skill whose `{log}` tag is "the active partner"; the only
single-writer lane the contract names is the wiki; no `writers:` posture is declared for `{research}`
anywhere in the shipped surface, so the attestation value set is unconstrained there. A Creative
running `vlt-research` and attesting `verified_by: vlt-research` is legal today.

The belief has a source anyway: the contract's *Capabilities* section makes a SKILL's hand-listed
"What you do" the same kind of thing as a capability and makes a heavy capability lane-owned;
`vlt-research` is listed under one partner only; and the contract never states `{research}`'s lane
status while its hygiene table rows "Wiki + research" together. Partners inferred the wiki's rule
for a folder the contract's own definition of a shared lane (*synthesized, single-writer*) excludes,
and recorded the inference as `## Self` (ST-8 cause B) — so the fix cannot live only in the
contract, which memory does not read first.

## Grounding (module source, `caea0d5`)

- **No single-writer rule covers `{research}`.** `vault-operating-contract.md:64` — the Layer-2
  sentence names `{research}` notes beside the wiki and restricts *only* the wiki ("a Librarian-only
  zone: the Librarian is its only writer"). `:255` — "A shared lane is a *synthesized, single-writer*
  lane — the wiki above all." `:139` — research notes are dated snapshots, "not promoted".
- **The op tags the active partner, not the Researcher.** `skills/vlt-research/SKILL.md`, *On
  Activation*: "Note the **active partner** for the log tag." Contract `:155` lists `research` as a
  log type with the ordinary `(<partner>)` tag.
- **Attestation is unconstrained there.** `write-verification.md` §Attestation: the `verified_by`
  value set is "whatever the nearest declaring container's `writers:` join admits; unconstrained
  where none declares." `grep -rn "writers:"` across `skills/vlt-setup/assets/` and `skills/vlt-lint/`
  finds no research posture (this run).
- **The belief's author.** Contract `:248–259` (*Capabilities*): "must be owned by that lane's
  rightful partner"; "hand-listed 'What you do' … the same kind of thing." Listing sites:
  `skills/vlt-agent-researcher/SKILL.md` ("Run `vlt-research`… This is your main work");
  `skills/vlt-agent-creative/SKILL.md:37` ("send them to the Librarian or Researcher first rather
  than thinning out an artifact"). The hygiene table `:318` rows "Wiki + research (incl. `{index}`)"
  under "the wiki lane's own machinery" — true for graduation/decay, read as ownership.
- **Where the belief lives.** ST-8, cause B and its evidence table: `## Self` is written by the
  partner and loaded as instruction on every activation; the vault rung `_agent/reflexes.md` is read
  in Beat 1 by every partner (contract `:226`). A fleet-wide correction reaches memory through the
  rung, not through a contract section opened point-of-use.

## Specimen manifest

The observed set is the owner's report of partner speech in `{field-vault}` sittings ("that's the
Researcher's lane"), not persisted on disk by any instrument — **count only; no slugs to recover.**
The minimal triggering fragment is the pair of contract sentences at `:253` and `:257` read in
sequence, plus the single-partner listing in `vlt-agent-researcher/SKILL.md`. A capture that wants
a set can grep `{field-vault}/{partners}/*/identity.md` for `Researcher` under `## Self` (read-only).

## Candidate dispositions (for capture to rule — not pre-empted here)

1. **State the lane, once.** One sentence in *Capabilities*: `{research}` is **not** a shared lane —
   research notes are raw, dated, multi-author by design; any partner may run `vlt-research`, tagged
   as itself. Prose clarification — no convention version bump (verify at brief).
2. **Reach the memory.** One pointer line on the vault rung `_agent/reflexes.md` (seeded by
   `vlt-setup`, merge-not-replace on upgrade) pointing at that sentence — the surface every partner
   reads in Beat 1. The rung's cap and promote-in/edit-one-out rule apply.
3. **Fix the route-away cue.** `vlt-agent-creative/SKILL.md:37` → "delegate a dive
   (`vlt-dispatch` delegate — companion filing `2026-09-16-094502`), or search-and-cite for a single
   fact." The Researcher's "main tool" line stays — it is true.
4. **Disambiguate the hygiene row** `:318` with a clause: the row is about decay machinery, not
   write ownership.
5. **Extend read-and-cite to the web** (contract, *Sessions*, the read-and-cite paragraph): a single
   fact may be fetched and cited inline in the caller's own artifact with a `sources:` entry;
   anything that should be *findable later* earns a note (in-place `vlt-research` or a delegate).
   **State the blind spot in the rule**: the bound is prose with no instrument; the delegate record
   is the visible half (the pattern `consult.md` uses for its own honest limit).

Dissent on record (roundtable): the search-and-cite tier is an honor-system hole (Quinn). Kept
because without it every one-fact gap pays the delegate's ceremony and the cheap verb eats the
traffic; the blind spot is to be named in the rule itself.

## Acceptance (proposed, all ship-verifiable at rest)

- grep: the *Capabilities* sentence exists; the rung seed carries the pointer line; Creative `:37`
  no longer routes research away; the hygiene row carries the clause.
- Handshake: `consult@1`, `frontmatter@14`, `write-verification@6` unchanged and bipartite-consistent
  (`package-lint`).
- Field-contingent (watch, not gate): a partner that formerly declined now runs, delegates, or cites.
