# vlt-review-council: `args` not threaded on name-invoked workflows — every council-gated mint fails first try

**Filed:** 2026-06-13 · **Origin:** Chef (cooking partner) mint session in `vlt-core`; recurrence observed across three mints · **Target artifacts:** `vlt-review-council` workflow (primary), `vlt-mint` SKILL Step 2a + `vlt-review-council` SKILL Step 2 (documentation), plus an upstream harness defect to escalate

## Problem statement + evidence

The council panel engine is the dynamic workflow `vlt-review-council.js`. Both its callers — `vlt-mint` (Step 2a, to gate a mint) and the `vlt-review-council` SKILL (Step 2, for a debate) — are instructed to invoke it **by name** with an args object, e.g.:

```
workflow('vlt-review-council', { mode: 'mint', kind, subject, personasPath })
```

The workflow reads its inputs from the `args` global (line ~32):

```js
const a = args || {}
const mode = a.mode
const subject = a.subject
const personasPath = a.personasPath
if (!mode || !subject || !personasPath) {
  return { error: 'vlt-review-council requires { mode, subject, personasPath }. ...',
           received: { mode: mode || null, hasSubject: !!subject, hasPersonasPath: !!personasPath } }
}
```

**Observed failure (reproduced verbatim this session, Chef mint):** invoking the Workflow tool with `name: 'vlt-review-council'` and a fully-populated `args` object returned, in ~3ms with zero agents spawned:

```json
{"error":"vlt-review-council requires { mode, subject, personasPath }.",
 "received":{"mode":null,"hasSubject":false,"hasPragmasPath":false}}
```

i.e. **`args` arrived empty/undefined inside the script** even though the tool call supplied it. The guard correctly refused to run a meaningless panel — good defensive design — but the gate could not execute as documented.

**This is not a one-off.** It has now occurred on **all three council-gated mints**:
- Dog Trainer (2026-06-09) — decision-log notes the same.
- Health Coach (2026-06-13) — decision-log: *"the harness did not thread `args` into the named-workflow invocation; the council had to be run by inlining the inputs into the persisted script."*
- Chef (2026-06-13) — same, third occurrence.

**The recovery used each time** (proven, but undocumented in the skills): every Workflow invocation persists its script to `…/workflows/scripts/<name>-<runId>.js` and returns the path. The operator edits that persisted script to **inline the inputs** — replacing `const a = args || {}` with a literal object carrying `mode`/`kind`/`subject`/`personasPath` — then re-invokes via `Workflow({ scriptPath })`. That runs the panel correctly. So the panel logic is sound; only the **args delivery path for name-invoked workflows is broken**.

## Root cause (best diagnosis)

The defect is in the **harness's name-invocation path**, not in the module's panel logic: when a workflow is launched by `name` from the main agent loop, the supplied `args` are not threaded into the script's `args` global. (Launching by `scriptPath` with the inputs baked in works — which is exactly why the inline-and-rerun workaround succeeds.) The module cannot fully fix a harness bug, but it can (a) harden the workflow so a stringified-args variant doesn't also silently fail, and (b) stop making every operator rediscover the recovery.

## Decision + rationale — what to ship in the module

### 1. Harden `vlt-review-council.js` args intake (defensive, low-risk)
Replace the bare `const a = args || {}` with intake that tolerates both an object and a JSON string, and surfaces a clearer diagnostic:

```js
let a = args || {}
if (typeof a === 'string') { try { a = JSON.parse(a) } catch { a = {} } }
```

Rationale: the Workflow tool contract warns that args passed as a JSON-encoded string breaks `args.x` access; some invocation paths may deliver a string rather than dropping args entirely. Parsing defends against that variant at zero cost. (It does **not** rescue the total-drop case — that needs the harness fix or the workaround — but it removes one failure mode and makes the guard's `received` report trustworthy.)

### 2. Document the recovery in both callers (the real fix until the harness is fixed)
The skills currently present the name-invocation as if it just works. Add an explicit fallback note so the gate is never blocked and the workaround isn't re-derived each mint:

- **`vlt-mint` Step 2a** and **`vlt-review-council` SKILL Step 2:** after the `workflow('vlt-review-council', {...})` instruction, add:
  > If the call returns `{ error: "vlt-review-council requires { mode, subject, personasPath }", received: { mode: null, … } }`, the harness did not thread `args` into the name-invoked workflow (a known harness defect). Recover: take the persisted script path from the tool result, edit it to inline the inputs (replace `const a = args || {}` with a literal `{ mode, kind, subject, personasPath }`), and re-invoke `Workflow({ scriptPath, … })`. Capture remains mandatory regardless of invocation path.

### 3. (Optional, stronger) Have the workflow self-report the delivery failure
Augment the guard's error so it names the likely cause and the fix inline, so the operator doesn't need to remember it:
```js
note: 'args did not reach the workflow — if invoked by name, the harness may not have threaded them; re-invoke by scriptPath with inputs inlined.'
```

## Exact module-side changes

| Artifact | Change |
|---|---|
| `vlt-review-council.js` (workflow) | line ~32: string-or-object args intake (#1); optionally extend the guard's error `note` (#3) |
| `vlt-mint/SKILL.md` | Step 2a: add the args-not-threaded recovery note (#2) |
| `vlt-review-council/SKILL.md` | Step 2: add the same recovery note (#2) — debate mode invokes the identical workflow and has the identical latent failure |

## Upgrade / migration path for existing installs

- All three changes are **additive and backward-compatible** — no data migration, no config change. A reinstall/upgrade simply ships the hardened workflow + the two skill notes.
- No effect on already-completed mints; their decision-log captures stand.
- Verify post-upgrade by running any council-gated kind and confirming either (a) name-invocation now threads args, or (b) the operator is guided straight to the scriptPath recovery.

## Latent bugs / related surface

- **The `vlt-review-council` SKILL (debate path) shares the defect.** It is documented only for the mint path here because that's where it was observed, but the debate entry calls the same workflow the same way — fix/doc both.
- **`new partner` KIND_PANEL = `['architect']`** (single lens). Not a bug, but note for the maintainer: every new-partner mint fields only the architect lens + moderator. The Health Coach and Chef decision-logs both flag this as "thinner than ideal." If richer new-partner review is wanted, that's a separate KIND_PANEL decision — out of scope for this filing, surfaced for visibility.

## Open questions for the maintainer

1. **Escalate upstream?** The core defect is in the harness's name-invocation args threading. Is there a channel to file it against the Claude Code / Workflow tool runtime? The module-side hardening is a mitigation, not a cure.
2. **Prefer scriptPath invocation by default?** An alternative to documenting the recovery is to have the callers invoke the council **by scriptPath from the start** (resolving the installed `…/.claude/workflows/vlt-review-council.js` and passing inputs in a way scriptPath honors). If scriptPath threads args reliably where name does not, making it the documented default would remove the failure entirely rather than recovering from it. Worth a maintainer test.
