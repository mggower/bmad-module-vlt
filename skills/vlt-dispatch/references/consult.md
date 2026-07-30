# vlt-dispatch — reference: Mode `consult`

Read on entering `consult` mode (router: `SKILL.md`, Mode dispatch).

## Mode: `consult` — ask another partner and get an attributed answer now

**A consult is a `relay` whose drain happens immediately, in-process, with the answer returned to the caller instead of left on the board.** Synchronous, **depth-1 hard** — the summoned partner answers, or refuses and names why; **it never summons**. It is read-only except its own memory. *Consult answers; relay assigns.*

Governed by `{conventions}/consult.md` — what a consult is, when it is earned, and the precondition it places on specs live there. This section owns the **mechanics**. The summoned partner **boots lite** — the engine prompt exempts it from its SKILL's activation ritual (no rule-card/contract read, no Beat 2 orient); entry is lite, and exit was already exempt (the contract: a consult crosses no sitting boundary, so no session note).

### Who fires it

A partner **mid-turn**, when it needs another partner's domain **to finish its current move** and the consult passes the **trigger rule** — single-homed at `vault-operating-contract.md`, *Read-and-cite is the documented default*; read the test there, don't work from memory. Read-and-cite stays the default; a consult is the exception that earns itself against that test.

A human may **invoke `consult` directly** for debugging, exactly as `relay` allows. **Never unprompted** — the standing rule holds for this mode too: there is no background consult.

### Inputs and validation

Required: **`to-slug`** (the partner being consulted), **`question`** (in the caller's own framing), **`groundIn`** (the **live absolute paths** the summoned partner must read — never a plugin-cache copy), and **`why`** — one line naming *what the caller is trying to finish* and *which part of it is outside its own authority*. Optional: **`from-slug`** (infer from the calling partner). Then:

- **Liveness (light).** Confirm `to-slug` matches a live `vlt-agent-{to-slug}` in `{project-root}/.claude/skills/`. If it doesn't, say so and stop — **never spawn**.
- **`from-slug ≠ to-slug`** — a partner does not consult itself.
- **Secret hygiene.** Same as every other mode — never put a credential in the question, the gist, or the `{log}` line.

**`why` is the anti-confabulation field.** It is what lets the summoned partner return `wrong-partner` or `insufficient-context` *accurately* instead of producing a plausible opinion about a question it was never really asked. A consult fired without it is a consult that cannot refuse well.

### Invoke the engine

Call the consult engine via the Workflow tool — **do not hand-spawn the partner**:

```
workflow('vlt-consult', {
  fromSlug:     <the calling partner's slug>,
  toSlug:       <the consulted partner's slug>,
  question:     <the question, in the caller's framing>,
  why:          <what the caller is finishing, and which part is outside its authority>,
  groundIn:     [<live absolute paths the summoned partner must read>],
  skillsPath:   <resolved LIVE absolute path to the installed skills dir>,
  partnersPath: <resolved LIVE absolute path to {partners}>,
  today:        'YYYY-MM-DD',
})
```

The workflow spawns **exactly one** agent and forces its return through a typed schema. That is why **depth-1 is structural, not an honor system**: a spawned agent cannot re-enter the workflow, so the summoned partner *cannot* chain a consult of its own. The engine is the single home for the consult protocol — this SKILL invokes it, it does not re-implement it in prose.

### The typed return union

`answer` | `insufficient-context` | `wrong-partner` (with a slug) | `needs-human` | `needs-work`.

**`insufficient-context` is a first-class, praised return.** A thin payload producing an invented opinion is strictly worse than no mechanism at all — read-and-cite cannot impersonate, but a confabulated partner voice can, and that is precisely what the operating contract's authority boundary forbids. Never treat a refusal as a failed consult; treat a suspiciously confident one as the thing to inspect.

### Surface the answer raw, attributed, before you use it

Put the summoned partner's `answer` in **its own block, verbatim, attributed** — then, *after* that block, the caller's use of it in the caller's own voice:

> **Consulted — Partner Name (`to-slug`):**
> <the answer, exactly as returned>

A digested partner voice is an unattributed claim. Two agents converging is only visible to the human if the human sees what the second one actually said, not a summary of it.

### Route the return

- **`needs-work`** → the caller writes the handoff doc and fires the existing **`relay`** path. *Consult answers; relay assigns* — the summoned partner never does the work.
- **`wrong-partner`** → the caller may consult the named slug. This is a **second consult by the caller**, still depth-1 from the caller — never a chained one by the summoned partner.
- **`needs-human`** → surface it and stop.
- **`insufficient-context`** → name what was missing; re-fire with a fuller payload, or fall back to read-and-cite.

### Write the consult block

Append to `_agent/dispatch.md`. The header shape **is the mode signal** (as `daily/…` and `relay:` are):

```
## [YYYY-MM-DD HH:MM] consult: <from-slug> → <to-slug> — <return-type>
- [x] `to-slug` Partner Name — <question gist> → <artifact or path grounded in> ✓ answered YYYY-MM-DD
```

If this is the record's **first** `consult:` block (grep the record) and `{conventions}/consult.md` reads `adoption_first_instance: null`, stamp it with a dated reference to this consult (the authority rule, `vlt-mint`, Step 4 — set once; if the key already carries a date, leave it).

**The pointer is written pre-checked (`- [x]`).** A consult never waited, so it is **traffic, not a queue item**. The consequence is load-bearing and worth stating outright: a consult block **never** appears on the `ledger` board and never in a partner's open slice, **by construction** — the ledger's greps count `- [ ]` only. Nothing here can rot open.

### The trail, and its bound

Three sites, and **only** three:

1. The pre-checked block above.
2. **One `{log}` line, tagged with the caller** (see Log) — the caller is the active partner; the consulted partner is named in the summary.
3. The **summoned partner's own `thread.md`** — and **only when the consult changed its stance** (the engine returns `stanceChanged`). A consult that merely confirmed what that partner already held writes nothing: `## Thread` is prunable attention that is *supposed to fade*, and one line per consult would rot the one file the contract says must stay light. The summoned partner writes its own memory; **the caller never writes it** — single-writer holds.

**No session note from the summoned partner.** A consult is **not** a hand-off and crosses **no sitting boundary** — the caller keeps the wheel and owns the single session note for the sitting. The sitting unit is single-homed in the operating contract, *Sessions, sittings, and hand-offs*; read it there.

### Report

Brief — who was consulted, the return type, and, on `insufficient-context` / `wrong-partner` / `needs-human`, what is missing, plainly:

> Consulted **Creative** (`creative`) on the framing question → `answer`. Recorded in the dispatch record; the Creative's thread moved, so it noted the shift itself.

Or: "Consulted **Researcher** → `insufficient-context`: it needs the source note path, which wasn't passed. Nothing was answered; re-fire with the path or read-and-cite instead."

### Log line

The mode's `{log}` entry (router: Log):

```
## [YYYY-MM-DD HH:MM] dispatch (<from-slug>) | consult: <from> → <to> — <question gist> → <return-type>
```

**The `consult` line carries ONE partner tag — the caller.** The tag is *the active partner for the operation* (operating contract, *the `{log}` format*), and in a consult that is unambiguously the caller: the consulted partner is not at the wheel. The consulted partner is named in the **summary**, which greps just as well and loses nothing — attribution of the *answer* lives in the attributed block and the consult record, both of which name both partners.

### Verify

After writing, re-read what you produced and confirm:

- The recipient slug is **live** (a real `vlt-agent-{to-slug}`), and `from-slug ≠ to-slug`. No partner was spawned if it wasn't.
- Exactly **one** `consult: <from> → <to>` block was appended, and its pointer is written **checked** (`- [x]`) — not open.
- The raw answer was surfaced **attributed, in its own block**, *before* any use of it in the caller's voice.
- **No `daily/` read, no wiki write.** The summoned partner spawned **no** second partner (depth-1 held).
- The summoned partner wrote **no** session note, and touched its `thread.md` **only** if the consult changed its stance.
- The `{log}` entry was appended, tagged with the **caller**. No secret in the question or the gist.

Report the result; fix any gap before closing.
