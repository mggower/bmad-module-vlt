---
id: 'ST-9'
slug: 'one-axis-design-leaves-the-diagonal-empty'
title: 'The cross-partner mechanism set and the capability-ownership model were each designed on one axis, so the cell each one never drew is empty — no seam returns worked results to a caller who keeps the wheel, and a listing reads as a lane'
status: 'standing'
opened: '2026-09-16'
opened_by: 'owner problem-solving session (bmad-cis-problem-solving, 2026-09-16) + roundtable (bmad-party-mode, same day) — reached two coupled causes and a fix shape; opened on the owner''s go'
session: '_output/problem-solution-2026-09-16.md (gitignored, carries {field-vault} specifics — provenance only, never load-bearing; this study is self-contained)'
causes:
  - 'Primary A: the cross-partner mechanisms were designed on ONE axis — does the wheel move? Consult (no), hand-off (yes), relay (later). Nobody drew the second axis — does WORK move? — so the cell "work moves, wheel stays" was never seen, and consult was given "transfers nothing" as its identity to defend the authority boundary. A partner that needs a filed artifact mid-sitting has only the slow diagonal: consult → needs-work → handoff doc → relay → a later sitting.'
  - 'Primary B: capability ownership was drawn on one axis — who LISTS it. The contract makes a hand-listed "What you do" the same kind of thing as a capability, and makes a heavy capability lane-owned; vlt-research is listed under one partner, and {research}''s lane status is never stated (the hygiene table even rows "Wiki + research" together). Partners inferred single-writer ownership from the nearest rule — the wiki''s — for a folder the contract''s own definition of a shared lane (synthesized, single-writer) excludes. The lane exists in prose and in memory, not in any rule.'
  - 'Amplifying: ST-8 weight. The Researcher''s full activation is the costliest way to research (~17.8K words in the field vault), so avoiding it is rational; the avoidance is written into `## Self` at sitting end and read back as instruction (ST-8 cause B), so the ghost lane hardens as memory. The owner hears it as "that''s the Researcher''s lane".'
cited_by:
  - 'factory/inbox/2026-09-16-094501-research-is-not-a-lane-but-partners-enforce-one.md (cause B + amplifying — the lane-status gap and the rung line)'
  - 'factory/inbox/2026-09-16-094502-no-seam-returns-worked-results-to-a-caller-who-keeps-the-wheel.md (cause A — the delegate mode and its population cut)'
  - 'factory/cycles/16-closed-loops/roadmap.md §A16-6 (capture 2026-09-16 of 094501 — GAP CONFIRMED; the filing''s `## Self` recovery grep run and found nothing, so cause B''s memory half is inferred for this instance, module-source half fully grounded)'
  - 'factory/cycles/16-closed-loops/roadmap.md §A16-7 (capture 2026-09-16 of 094502 — GAP CONFIRMED; adds `vlt-dispatch/SKILL.md:18` as a site and the `consult@1` neighbour-list handshake question; carrier bound to A16-3/S-4 as decide-once D6)'
superseded_by: ''
---

# ST-9 — one-axis design leaves the diagonal empty

## The claim

Two independent-looking complaints — *"research needs a second session"* and *"partners say
that's the Researcher's lane"* — are one shape. In both, a design was drawn on a single axis
and the cell the missing axis would have exposed stayed empty. The mechanism set asked only
*does the wheel move?* and so never built the seam that moves work without the wheel. The
ownership model asked only *who lists it?* and so never stated whether `{research}` is a
single-writer lane, leaving partners to infer the wiki's rule for a folder that rule does not
cover. The two holes meet at exactly one seam: a non-Researcher partner, mid-sitting, needing
knowledge the vault does not hold.

The pattern is the same one the Arc 7 roundtable named for the lifecycle (*the joints, not the
parts*): each rule is locally correct; the pathology lives between them.

## The evidence — module source at `caea0d5`, read-only; field observation by the owner, 2026-09-16

**A. The mechanism table has an empty cell.** Contract, *Sessions, sittings, and hand-offs*
(`vault-operating-contract.md:265–293`):

| Mechanism | Moves work? | Moves the wheel? | When the answer lands |
|---|---|---|---|
| `consult` (`vlt-dispatch`) | **no** — "a consult transfers **nothing**" (`{conventions}/consult.md`) | no | now |
| `relay` (`vlt-dispatch`) | yes, later | no now | the recipient's next orient — a later sitting |
| hand-off | yes | **yes** — "ends one sitting and begins another" (`:267`) | now, but the caller's sitting is over |
| *(work moves, wheel stays)* | — | — | **no mechanism** |

The consult mode's own routing closes the door: `needs-work` → *"the caller writes the handoff
doc and fires the existing relay path"* (`skills/vlt-dispatch/references/consult.md`, *Route the
return*). The consult engine is read-only by identity (*"It is read-only except its own memory"*).
So a partner needing a filed research note has the diagonal only.

**B. The lane is unstated, and the nearest rule is the wiki's.**
- The only single-writer sentence in the contract is Layer 2's wiki clause (`:64`, *"a
  Librarian-only zone: the Librarian is its only writer"*). `{research}` appears in the same
  sentence as a Layer-2 zone with no writer restriction.
- *Capabilities* (`:248–259`): *"A heavy capability … must be owned by that lane's rightful
  partner"* and *"A partner's hand-listed 'What you do' … and its `capabilities/` folder are the
  same kind of thing."* `vlt-research` is hand-listed under exactly one partner
  (`skills/vlt-agent-researcher/SKILL.md`, *"This is your main work"*), and the Creative routes
  research away (`skills/vlt-agent-creative/SKILL.md:37`, *"send them to the Librarian or
  Researcher first"*).
- The contract's own definition — *"A shared lane is a synthesized, single-writer lane — the wiki
  above all"* (`:255`) — excludes `{research}` (notes are `trust: raw`, dated snapshots, "not
  promoted", `:139`). But nothing says so, and the hygiene table rows *"Wiki + research"*
  together (`:318`).
- `vlt-research` itself tags its log line with *"the active partner"* (its *On Activation*), and
  the attestation value set is *"unconstrained where none declares"* (`write-verification.md`,
  §Attestation) — no `writers:` posture is declared for `{research}` anywhere in the shipped
  surface (grep, this run). A Creative attesting `verified_by: vlt-research` is legal today.

**C. The belief is real and lives in memory.** The owner reports partners declining with
*"that's the Researcher's lane"*. No rule says it. ST-8's evidence gives the mechanism: `## Self`
is written by the partner at sitting end and loaded as instruction on the next activation; a
habit recorded once is a rule thereafter. The Researcher's full activation (~17.8K words) makes
the avoidance rational, so the habit is reinforced every time it is exercised.

## The causal chain

1. Consult was designed to defend the authority boundary; *"transfers nothing"* became its
   identity (A4-5, `consult@1`). Correct, and it fixed the wheel axis as the only axis.
2. Relay and hand-off already covered *work later* and *work + wheel*. With consult covering
   *nothing now*, the set looked complete. The 2×2 was never drawn, so the empty cell was
   never a design item — only ever a symptom ("research takes two sessions").
3. Separately, the Capabilities model unified shipped and vault-grown capabilities by treating
   the SKILL's listing as the object. Ownership-by-location is right for light capabilities
   (own zone) and for heavy ones (single-writer lanes). It is silent about a **non-lane op
   listed under one partner**, and `vlt-research` is exactly that.
4. With the lane status unstated, partners resolved it against the closest rule — the wiki's —
   and recorded the resolution as `## Self`. From then on the lane needed no rule.
5. The two holes are coupled at one seam: the partner that *would* have run the op in place is
   the partner that believes it may not, and the mechanism that *would* have let it delegate
   does not exist. The owner experiences the sum as "multiple sessions to close a task".

## Rejected alternatives

- **Let consult do bounded work (`consult@2`).** Rejected: reopens the identity that defends
  the authority boundary; bumps a convention and re-acks two consumers to add a sibling. The
  empty cell wants a sibling, not a mutation.
- **Boomerang hand-off (same-conversation hand-off with a return leg).** Rejected: two extra
  session notes per fact; fights the sitting unit; pays the Researcher's boot.
- **Ad-hoc Agent-tool spawn from the caller, no engine.** Rejected: mechanics not single-homed,
  depth-1 unenforced, attribution improvised per partner — the honor system the consult engine
  was built to remove.
- **A `remember:` flag that boots a Researcher-lite runner when the interaction "should be
  remembered".** Rejected at the roundtable: the caller would be deciding another partner's
  memory from outside (a cross-partner memory write), and the test is moot — the vault
  remembers by filing the note, and the Researcher's own Phase 2 vault check and Beat 2 log
  read find it. One runner, partnerless, always.
- **Generalize delegate to any op immediately** (Victor's dissent, on record). Rejected for v1:
  for a single-writer lane the wheel *is* the authority, so moving work without the wheel into
  the wiki would hollow out hand-off. The rule is a **population cut** (Arc 9 D5): delegate may
  target only ops whose write target is not a shared lane. Research is the v1 tenant; the
  contract states the rule, not the enumeration.
- **Prose-only fix in the contract.** Rejected as *sufficient*: the belief lives in partner
  memory, which reads the vault rung and `identity.md` before it reads a contract section. The
  sentence goes in the contract once; a pointer line goes on the rung.

## What this session got wrong, on record

- The problem-solving session's first framing was *"should any partner be allowed to call
  vlt-research?"* — a permission question. Grounding showed the permission already exists; the
  question was *how* (context weight, honest attribution) and *why partners believe otherwise*.
- The session's decision matrix scored a mechanism that did not exist against ones that did,
  and scored it highest. The roundtable did not dispute the choice but noted the method: the
  score reflected the diagnosis, not a measurement.
- The `remember:` flag survived into the recommended solution and was killed only at the
  roundtable, for a reason the contract already states (no cross-partner memory writes).
- Quinn's dissent stands unresolved: the *search-and-cite* tier (a single fact fetched and
  cited inline, no note) is bounded by prose and has no instrument. It is kept because without
  it every one-fact gap pays the delegate's ceremony (the cheap verb eats the traffic — the
  PARA lesson, this time with the cheap verb being the honest one), and its blind spot is to be
  named in the rule itself, the way `consult.md` names its own honest limit.

## What would close it

Named here as shape; the builds are the filings' to propose and ideation's to rule.

- **Draw the axis** — publish the 2×2 in the contract's *Sessions* section and fill the cell:
  a `delegate` mode (`vlt-dispatch`) with an engine cloned from `vlt-consult.js` (one spawned
  agent, typed return, depth-1 structural), returning `done{notePath, headline, verification,
  wikiCandidate} | incomplete{wipPath} | insufficient-context | needs-human | too-big`. Depth
  `quick|moderate` only; `deep` is a sitting's worth of work and returns `too-big` → relay.
  Runner is partnerless; its governance carriage is A16-3's (pointer to the card and rung in
  the engine prompt, never a second copy) — build with or after A16-3. The runner never offers
  the Librarian hand-off; the caller relays on `wikiCandidate`. Record: a pre-checked
  `delegate:` block (never on the ledger by construction), two `{log}` lines (dispatch + the
  op's own) both tagged with the caller, no session note.
- **State the lane** — one contract sentence in *Capabilities*: `{research}` is not a shared
  lane; any partner may run `vlt-research`. One pointer line on the vault rung so the fleet's
  memory reads it. Creative `:37` becomes "delegate a dive, or search-and-cite." The Researcher's
  "main tool" stays — it is true.
- **Redirect the trapdoor** — consult mode's `needs-work` routing: *delegate if bounded, relay
  if not*. Add delegate to `consult.md`'s neighbour list. Both are clarifications; the brief
  verifies `consult@1` stays bipartite-consistent.
- **Extend read-and-cite to the web** for a single fact used in the caller's own artifact with a
  `sources:` citation, with the blind spot stated in the rule.
- **Watch, not build:** an orphaned `.WIP.md` in `{research}` from an interrupted runner has no
  decay contract today (same as headless); `incomplete{wipPath}` makes it visible to the caller.

Every acceptance check for the delegate is ship-verifiable at rest against a temp-vault fixture
(one agent spawned; typed return on thin / deep / real-quick payloads; one pre-checked block;
caller-tagged log lines; no session note; note passes tier-1). The lane fix is greppable. The
field-contingent tail — a partner that used to decline now delegates — is a watch.
