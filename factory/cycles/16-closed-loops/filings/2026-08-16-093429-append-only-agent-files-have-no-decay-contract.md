# The agent zone's append-only files ship with no decay contract — everything accumulates, nothing decomposes

_Filed 2026-08-16 from **vlt-core**, classification: **candidate**. Prompted by owner-observed
volume growth in the agent zone at ~10 weeks of live use; converged out of a vault-hygiene
ideation session (`_agent/artifacts/brainstorming/brainstorm-vault-hygiene-2026-08-16/` — memlog +
`brainstorm-intent.md` hold the full idea set). Grounding measured against vlt-core at 1c15099 and
module source at b117d81. Owner elected to file (2026-08-16)._

## The claim

Every operational file the module scaffolds into the agent zone is append-only or grow-only, and
none carries any retention, rotation, or compaction contract. The ops that write them (`{log}`
appends from every sitting, dispatch routing, backlog filing, thread/identity updates) are
producers; the module ships **no decomposer** — no op, convention, or tripwire whose job is decay.
Growth is therefore linear with use, unbounded by design rather than by oversight.

## Grounding (vlt-core at ~10 weeks, first ingest 2026-06-06)

- `_agent/log.md` — **259K / 656 op lines**; one line per *operation*, though most detail is
  already duplicated into `_agent/sessions/` records the line points at. Linear extrapolation:
  ~2.5MB at one year — unloadable as a whole-file read.
- `_agent/dispatch.md` — **155K / 337 lines**; sections whose every item is checked off (`[x]`)
  never leave the board. The drain empties items, not the file.
- `_agent/backlog.md` — **181K / 221 lines**; items are essay-length, and resolved items have no
  archive destination defined.
- `_agent/partners/` — 16K (dog-trainer) to **240K (librarian)**; threads accumulate sitting after
  sitting with no fold-line between current-self and history.
- Contrast, module-side: `_agent/tripwires.yaml` exists and `lint-debt` shows the module already
  owns tripwire machinery — but no mass/age tripwire watches any of the above.
- Adjacent, not duplicate: the 2026-07-29 boot-whale filings (`2026-07-29-082930-*`, `-082934-*`)
  cost out *shipped module text* (contract, skill files). This filing is the runtime twin: the
  *vault-side data files* that grow with use. Both tax the same wake-context budget and compound.

## Why it matters

- The cost is read-side, not disk-side: partners grep/read these files at wake and mid-flow
  (dispatch drains, ledger, backlog scans). What a partner must load to answer "what's open?"
  grows without bound.
- It worsens silently — no bell. The SessionStart relay-overdue warning proves the vitals pattern
  works, but nothing watches mass.
- Every live vault will hit this; vlt-core is merely first. A fix adopted at week 10 costs a
  656-line migration; at one year it is an archaeology project.

## Candidate dispositions (for capture to rule — not pre-empted here)

- **(a) Retention declared at birth.** The conventions/templates for accumulating files carry a
  decay contract in frontmatter (e.g. `retention: 90d → digest`); a new accumulating file cannot
  be scaffolded or minted without one. Hygiene becomes execution of declared contracts, not
  judgment. Deepest fix; touches the governance bundle and mint templates.
- **(b) A three-verb hygiene taxonomy, one verb per file class.** *Rotate* logs (mechanical,
  schedulable — quarterly rotation to an `annals/` sibling, mirroring the `sessions/` pattern);
  *drain* boards (scavenger-sweep fully-closed dispatch sections past an age threshold; move
  resolved backlog items to a done-archive); *tend* identity/threads (deliberate rolling-summary
  header + prunable tail — never scheduled). The taxonomy is what keeps "scheduled pruning"
  from ever touching identity.
- **(c) Safety model making (b) council-free: git-as-archive + idempotent watermarks.** Every
  append already pairs with a commit, so compaction is never destruction; compaction is mechanical
  or lossless-by-reference (interpretive digests only *add*; raw moves to `_archive/`); each file
  carries `compacted-through:` frontmatter (the dispatch `routed through line N` idempotency
  pattern, generalized); every hygiene run is itself a logged, committed operation.
- **(d) Trigger via existing machinery.** Mass/age tripwires join `tripwires.yaml` beside
  `lint-debt`; SessionStart vitals generalize relay-overdue into hygiene vitals; execution is a
  scheduled headless run filing its digest as a dispatch pointer for human review. Micro-prunes
  over heroic cleanups.

Preference, weakly held: **(b)+(c) as the shippable core** (they ride patterns the module already
trusts: `sessions/` foldering, dispatch watermarks, commit-per-write), with **(a)** as the durable
convention so the gap cannot recur, and **(d)** as its bell. Explicit non-goals surfaced in
ideation: no in-place LLM rewriting of records; no binary compression (archives stay readable
markdown); no new ever-growing hygiene ledger (state lives in the files' own watermarks);
agent-zone hygiene is a sibling of `vlt-lint`, not folded into its wiki niche.

## Provenance guess (marked as a guess)

Likely origin: the governance bundle's file scaffolds were designed for correctness of *writes*
(append-only, single-writer, commit-paired) with lifecycle simply out of frame at design time —
the same posture-age pattern the boot-whale filings found (surfaces predating the module's later
lazy/JIT discipline). A guess; factory capture should re-ground it.
