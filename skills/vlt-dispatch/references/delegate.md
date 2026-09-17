# vlt-dispatch — reference: Mode `delegate`

Read on entering `delegate` mode (router: `SKILL.md`, Mode dispatch).

## Mode: `delegate` — hand bounded work to a partnerless runner and get its result now

**A delegate moves the work, not the wheel.** A partner hands a **bounded** piece of work to a **partnerless runner** — an agent that is nobody, running one operation — and gets a **typed result back inside its own sitting**. No sitting boundary is crossed, the caller keeps the wheel, and the runner writes **no session note**. What comes back is an artifact someone can find later, plus a headline the caller can use in its own voice.

The two axes and every cell they make are single-homed at `vault-operating-contract.md`, *Sessions, sittings, and hand-offs* — read the 2×2 there. This section owns the **mechanics**.

**The population rule** is the contract's: **an operation may be delegated only where its write target is not a shared lane.** The **v1 tenant is `op: research`** (`vlt-research` writes `{research}`, which the contract's *Capabilities* names as not a shared lane). A second tenant is an **enum change in this mode**, never a second engine.

### Who fires it

A partner **mid-turn**, when it needs a **bounded, findable-later** artifact to finish its current move — the test is *findable later* (should this produce an artifact someone can find?), which is disjoint from the consult's test of *memory*. A consult reaches for a partner; a delegate reaches for a runner.

A human may **invoke `delegate` directly** for debugging, exactly as `relay` and `consult` allow. **Never unprompted** — the standing rule holds for this mode too: there is no background delegate.

**The caller's tag** is the firing partner's own slug — or **`none`** in a partnerless sitting (the contract's `(none)` tag; there is no `(user)` value in this module). A human running the mode by hand is doing so inside some sitting: the tag is that sitting's active partner, or `none` if it has none.

### Inputs and validation

Required: **`op`** (v1: `research`), **`question`** (in the caller's own framing), **`depth`** (`quick` | `moderate`), **`groundIn`** (the **live absolute paths** the runner must read — never a plugin-cache copy), and **`why`** — one line naming *what the caller is trying to finish* and *why the answer must be findable later*. Optional: **`from-slug`** (infer from the calling partner; `none` when partnerless).

- **`depth: deep` is refused before spawning** and returns `too-big`. A deep dive is not bounded work; it routes to `relay`. (A partner may still run `vlt-research` deep **in its own sitting** — that is not a delegate.)
- **`op` liveness (light).** Confirm `op` names a live operation skill (`vlt-research` in `{project-root}/.claude/skills/`). If it can't be read, say so and stop — **never spawn**.
- **`op` is in the enum.** Anything but `research` is refused here, not passed to the engine.
- **Secret hygiene.** Same as every other mode — never put a credential in the question, the gist, or the `{log}` line.

**`why` is the anti-confabulation field**, exactly as it is on a consult: it is what lets the runner return `insufficient-context` accurately instead of diving on a question it was never really asked.

### Invoke the engine

Call the delegate engine via the Workflow tool — **do not hand-spawn the runner**:

```
workflow('vlt-delegate', {
  op:           'research',
  fromSlug:     <the calling partner's slug, or 'none'>,
  question:     <the question, in the caller's framing>,
  depth:        'quick' | 'moderate',
  why:          <what the caller is finishing, and why it must be findable later>,
  groundIn:     [<live absolute paths the runner must read>],
  skillsPath:   <resolved LIVE absolute path to the installed skills dir>,
  researchPath: <resolved LIVE absolute path to {research}>,
  logPath:      <resolved LIVE absolute path to {log}>,
  today:        'YYYY-MM-DD',
  spawnedAt:    '<a stamp taken immediately before this call>',
})
```

Take `spawnedAt` **before** invoking (e.g. `date '+%Y-%m-%d %H:%M:%S'`) — the engine has no clock, and the stamp is what bounds the interrupted-dive probe below.

The workflow spawns **exactly one** agent (**zero** on `deep`) and forces its return through a typed schema. **Depth-1 is structural, not an honor system**: a spawned agent cannot re-enter the workflow, so the runner *cannot* chain a delegate, a consult or a hand-off of its own. The engine is the single home for the delegate protocol — this SKILL invokes it, it does not re-implement it in prose.

### The typed return union

`done{notePath, headline, verification, wikiCandidate}` | `incomplete{wipPath}` | `insufficient-context` | `needs-human` | `too-big`.

`too-big` and `incomplete` are the **engine's** rulings — `too-big` returned before any agent is spawned, `incomplete` derived from a null return. The runner's own schema offers it only `done` / `insufficient-context` / `needs-human`: it cannot rule on its own scope, and it cannot report its own death.

**`insufficient-context` is a first-class, praised return.** A thin payload producing an invented finding is strictly worse than no mechanism at all. Never treat a refusal as a failed delegate; treat a suspiciously confident one as the thing to inspect.


### Route the return

- **`done`** → surface the `headline` in the caller's own voice and **cite the note** (`notePath`). If `wikiCandidate` is true, **the caller relays** to the Librarian (`vlt-dispatch relay`) — the runner never offers or performs the wiki hand-off, because depth-1 forbids it.
- **`incomplete`** → the runner was killed mid-dive. The engine derives this from a null return — **the runner is never asked to report its own interruption** — and hands back a `wipProbe` rather than a path, because a workflow script has no filesystem access. **Resolve `wipPath` mechanically, never by asking any agent**: the newest `*.WIP.md` under `wipProbe.dir` modified after `wipProbe.newerThan` (`find "<dir>" -name '*.WIP.md' -newermt "<stamp>"`, newest by mtime). Surface that path **and its attribution** — the file's first body lines carry `delegated_by:` and the question. The caller decides: re-fire, finish it itself, or leave it for the human. If the probe finds nothing, say exactly that: the dive died before it checkpointed.
- **`insufficient-context`** → re-fire with a fuller payload, or fall back to read-and-cite.
- **`too-big`** → the **relay** path: the work is not bounded, so it is assigned, not delegated. *Consult answers; delegate runs bounded work; relay assigns.*
- **`needs-human`** → surface it and stop.

### Write the delegate block

Append to `_agent/dispatch.md`. The header shape **is the mode signal** (as `daily/…`, `relay:` and `consult:` are — a `delegate:` header is its own kind, never a `consult:` block carrying an extra field):

```
## [YYYY-MM-DD HH:MM] delegate: <from-slug> → research — <return-type>
- [x] `from-slug` Partner Name — <question gist> → [[<note-or-wip-path>]] ✓ returned YYYY-MM-DD
```

**The pointer is written pre-checked (`- [x]`).** A delegate never waited, so it is **traffic, not a queue item**: a `delegate:` block **never** appears on the `ledger` board and never in a partner's open slice, **by construction** — the ledger's greps count `- [ ]` only. Nothing here can rot open.

**Unlike a `consult:` block, a `delegate:` block is drain-eligible the moment it is written** (`vlt-decay`, its drain reference). The difference is the evidentiary window: a consult's is unbounded (the consult-precondition check compares blocks against specs of any age), a delegate's is not — it is bounded work with an artifact of its own, exactly like a relay.

### The trail, and its bound

Three sites, and **only** three:

1. The pre-checked block above.
2. **Two `{log}` lines, both tagged with the caller** — the `research` line the operation writes (`vlt-research`, Phase 6, with `<partner>` = the **caller**, not the runner) and this mode's own `dispatch` line (see Log line, below).
3. **The note itself** (`notePath`), or the `.WIP.md` on an interrupted dive.

**No session note from the runner.** A delegate crosses **no sitting boundary** — the caller keeps the wheel and owns the single session note for the sitting (operating contract, *Sessions, sittings, and hand-offs*). **Nothing under `{wiki}`** is written by the runner, and the runner fires **no relay**: a wiki candidate comes back as a flag for the caller to relay.

### Report

Brief — what was delegated, the return type, and what came back:

> Delegated a `quick` dive on the retention question → `done`. Filed at `{research}/2026-09-17-101500-retention-window-evidence.md` (verification passed); headline below. It flagged a wiki candidate, so I've relayed the note to the Librarian.

Or: "Delegated a dive → `too-big`: a `deep` dive isn't bounded work. Nothing was spawned. I've written the handoff doc and relayed it instead."

### Log line

The mode's `{log}` entry (router: Log):

```
## [YYYY-MM-DD HH:MM] dispatch (<from-slug>) | delegate: <from> → research — <question gist> → <return-type>
```

**Both lines carry ONE partner tag — the caller.** The tag is *the active partner for the operation* (operating contract, *the `{log}` format*), and a runner is nobody: it is not at the wheel and has no slug to carry. That is why the operation's own `research` line is tagged with the caller too, not with the runner.

### Verify

After writing, re-read what you produced and confirm:

- `op` was in the enum and **live**; `depth` was `quick` or `moderate` — a `deep` request returned `too-big` with **nothing spawned**.
- Exactly **one** `delegate: <from> → research` block was appended, and its pointer is written **checked** (`- [x]`) — not open.
- At most **one** research note exists from this run, it carries `verified_by: vlt-research`, and the `headline` surfaced matches it.
- **Zero bytes written under `{wiki}`**; **no relay fired by the runner**; no second agent spawned (depth-1 held).
- The runner wrote **no session note** — the sitting's single session note is the **caller's**, tagged with the caller.
- **Two `{log}` entries**, both tagged with the caller. No secret in the question or the gist.
- On `incomplete`: the `.WIP.md` exists and its first body lines carry `delegated_by:` and the question.

Report the result; fix any gap before closing.
