export const meta = {
  name: 'vlt-delegate',
  description: 'Hand a bounded piece of work to a partnerless runner and return a typed result inside the caller\'s own sitting',
  whenToUse: "Invoked by vlt-dispatch's `delegate` mode when a partner needs a bounded, findable-later artifact to finish its current move. Returns a typed union: done / incomplete / insufficient-context / needs-human / too-big.",
  phases: [
    { title: 'Delegate', detail: 'spawn one partnerless runner; it runs the bounded operation and returns its artifact' },
  ],
}

// depends_on: []
// ^ the asset ack (B7-6): this workflow reads NO convention files today — the empty
//   list is the explicit, checkable "reads no conventions" state the release gate
//   (package-lint E5) requires on every shipped workflow, so a future convention
//   read cannot arrive unacked and structurally unnoticed.
//   NOTE: the runner below attests its note exactly as its operation skill already
//   requires, and writes two attribution lines into its .WIP.md — both are the
//   operation's own rules, read by the runner from the LIVE skill at run time. This
//   file pins NO convention; the ack lives on `vlt-dispatch`, which owns the mode.

// ─────────────────────────────────────────────────────────────────────────────
// vlt-delegate — the partnerless bounded-work runner.
//
// The work moves; the wheel does not. The caller stays at the wheel for its whole
// sitting and gets a typed result back inside it. The runner is NOBODY: it has no
// slug, no memory, no identity read, and it writes NO session note — which is what
// keeps this a delegate and not a hand-off.
//
// Depth-1 is STRUCTURAL, not an honor system: this workflow spawns exactly ONE
// agent, and a spawned agent cannot re-enter a workflow. The runner therefore
// cannot chain a delegate, a consult, or a relay of its own — the boundary is
// closed by the shape of the engine, not by a prose rule it could talk past.
//
// It carries NO rule-card or vault-rung text: those arrive with the session
// through the vault's CLAUDE.md imports, for this session kind like every other.
// A copy here would be a second carrier of the same rules.
//
// The typed return union is FORCED by the schema below. `too-big` is the ENGINE's
// ruling, returned before any agent is spawned — never a spawned agent's opinion
// about its own scope. `incomplete` is likewise engine-derived from a null return:
// a runner that was killed cannot report that it was killed, so it is never asked to.
//
// args (passed by vlt-dispatch's `delegate` mode):
//   {
//     op:           string    // the delegated operation. v1 enum: 'research' ONLY.
//                             //   A second tenant is an enum change here, never a
//                             //   second engine.
//     fromSlug:     string    // the CALLER's routing slug — or 'none' in a partnerless
//                             //   sitting. The runner has no slug of its own; every
//                             //   tag it writes carries this one.
//     question:     string    // the question, in the caller's own framing
//     depth:        string    // 'quick' | 'moderate'. 'deep' is refused before spawning.
//     why:          string    // what the caller is trying to finish, and why the answer
//                             //   must be findable later. The anti-confabulation field:
//                             //   it is what lets the runner return insufficient-context
//                             //   ACCURATELY rather than diving on a question it was
//                             //   never really asked.
//     groundIn:     string[]  // LIVE absolute paths the runner must read. Never a
//                             //   plugin-cache copy — pass the real vault paths.
//     skillsPath:   string    // absolute path to the installed skills dir (holds vlt-research)
//     researchPath: string    // absolute path to {research} — where the note and any
//                             //   .WIP.md land
//     logPath:      string    // absolute path to {log} — the runner appends the
//                             //   operation's own line there, tagged with the CALLER
//     today:        string    // 'YYYY-MM-DD' — the script has no clock and must not invent one
//     spawnedAt:    string    // optional stamp the caller passes for the incomplete probe
//                             //   (the script has no clock; see the incomplete path below)
//   }
// returns the DELEGATE_RETURN object (plus `degraded: true` + a note where the
// operation skill could not be read or the runner did not return).
// ─────────────────────────────────────────────────────────────────────────────

// The Workflow runtime delivers `args` as a JSON-encoded STRING, not the object the
// caller passed (true for name-, scriptPath-, and inline-script invocation alike).
// Parse defensively so the delegate runs on the first try — without this, `a` is the raw
// string, `a.question` is undefined, and the guard below wrongly reports "args missing".
let a = args || {}
if (typeof a === 'string') { try { a = JSON.parse(a) } catch { a = {} } }

const OPS = ['research']

const op = a.op || 'research'
const fromSlug = a.fromSlug
const question = a.question
const depth = a.depth || 'quick'
const why = a.why || ''
const groundIn = Array.isArray(a.groundIn) ? a.groundIn : []
const skillsPath = a.skillsPath
const researchPath = a.researchPath || ''
const logPath = a.logPath || ''
const today = a.today || ''
const spawnedAt = a.spawnedAt || today

if (!fromSlug || !question || !skillsPath) {
  return {
    error: 'vlt-delegate requires { fromSlug, question, skillsPath }. vlt-dispatch\'s `delegate` mode names them (fromSlug is "none" in a partnerless sitting).',
    received: {
      fromSlug: fromSlug || null,
      hasQuestion: !!question,
      hasSkillsPath: !!skillsPath,
    },
  }
}

if (!OPS.includes(op)) {
  return {
    error: `vlt-delegate's op enum is [${OPS.join(', ')}] — "${op}" is not a delegable operation. A second tenant is an enum change in this engine and its mode reference, never a second engine.`,
    received: { op },
  }
}

// `too-big` is the ENGINE's ruling, made BEFORE any spawn: a deep dive is not bounded
// work, so it is not delegable at all. Zero agents are spawned on this path — the
// caller routes it through relay instead. (A partner may still run the operation deep
// in its own sitting; that is not a delegate.)
if (depth !== 'quick' && depth !== 'moderate') {
  log(`delegate refused before spawning: depth "${depth}" is not bounded work (quick | moderate only)`)
  return {
    op,
    fromSlug,
    returnType: 'too-big',
    notePath: '',
    headline: '',
    verification: '',
    wikiCandidate: false,
    missing: [],
    note: `depth "${depth}" is not bounded work — nothing was spawned. Route it through relay, or run the operation deep in your own sitting.`,
  }
}

const DELEGATE_RETURN = {
  type: 'object',
  additionalProperties: false,
  required: ['available', 'returnType', 'notePath', 'headline', 'verification', 'wikiCandidate'],
  properties: {
    available: {
      type: 'boolean',
      description: 'false if the operation SKILL could not be read — then the rest is empty and the caller gets a degraded, clearly-labelled return rather than an invented result',
    },
    returnType: {
      type: 'string',
      enum: ['done', 'insufficient-context', 'needs-human'],
      description: 'the runner\'s own typed return. `insufficient-context` is a FIRST-CLASS, praised return — never a failure to apologize for. `incomplete` and `too-big` are NOT in this list: they are the engine\'s rulings, never the runner\'s',
    },
    notePath: {
      type: 'string',
      description: 'returnType=done ONLY — the absolute path of the research note actually written. Empty on every other return: a `done` with no note is a contradiction the caller checks',
    },
    headline: {
      type: 'string',
      description: 'returnType=done ONLY — the single headline finding, in plain prose, for the caller to use in its own voice. Not a summary of the note; the one thing the dive found',
    },
    verification: {
      type: 'string',
      description: 'returnType=done ONLY — the tier-1 verification result on the note: "passed", or the specific gaps flagged. Fail-open: gaps are flagged, never a reason to withhold the note',
    },
    wikiCandidate: {
      type: 'boolean',
      description: 'whether these findings belong in the wiki. The runner NEVER offers or performs the hand-off — it raises this flag and the CALLER relays to the Librarian',
    },
    missing: {
      type: 'array',
      items: { type: 'string' },
      description: 'returnType=insufficient-context ONLY — precisely what the payload lacked (a path not passed, a question too broad to bound, context only the caller holds)',
    },
    needsHuman: {
      type: 'string',
      description: 'returnType=needs-human ONLY — the decision that is the human\'s to make, in one line',
    },
  },
}

phase('Delegate')
log(`delegate: ${fromSlug} → ${op} (${depth}; grounding in ${groundIn.length} path(s))`)

// If a convention read ever enters this prompt, it must be merged-on-read per
// vault-operating-contract.md (Convention overlays) and must add its flat
// "name@version" pin to the depends_on header line at the top of this file.
const delegatePrompt =
  `You are a PARTNERLESS RUNNER. You are nobody: you have no partner identity, no slug, no memory in this vault, and no voice of your own. ` +
  `You have been DELEGATED one bounded piece of work by the partner whose routing slug is "${fromSlug}". You do that work, you return, and you are done. ` +
  `\n\nRun the operation at the LIVE path ${skillsPath}/vlt-${op}/SKILL.md — read it and follow it, at depth "${depth}". ` +
  `If that SKILL file cannot be read, return { available: false } with empty fields and stop — do NOT improvise the operation.\n` +
  `\nYou do NOT run any partner's activation ritual: you are not a partner and you do not become one. ` +
  `(The rule-card and the vault rung arrive with this session through the vault's CLAUDE.md — you do not go looking for them, and you do not need to.)\n` +
  `\nHARD RULES:\n` +
  `- You may READ anything the operation entitles you to read, and you must read every path listed under GROUND IN below from those exact LIVE paths.\n` +
  `- You write EXACTLY what the operation writes and nothing else: the note at ${researchPath || '{research}'}, its .WIP.md while the dive is open, and the operation's own {log} line at ${logPath || '{log}'}.\n` +
  `- **Every tag you write carries the CALLER's slug, "${fromSlug}", never yours** — you have none. The operation's {log} line takes "${fromSlug}" as its partner tag.\n` +
  `- You write **NO session note**. The caller keeps the wheel and owns the single session note for this sitting. This is not optional and it is not a style choice: a runner that writes a session note has turned a delegate into a hand-off.\n` +
  `- You write **NOTHING under the wiki**, and you **never offer or perform the Librarian hand-off** (the operation's final wiki-pass offer does NOT apply to you — you are depth-1 traffic). If the findings belong in the wiki, set wikiCandidate true and let the caller relay it.\n` +
  `- You NEVER summon a partner, consult, relay, hand off, or spawn anything. If the work needs someone else, say so through the return type.\n` +
  `- Attest the note exactly as the operation requires (its verify-and-attest phase: the tier-1 checklist, then verified_by / verified_at) and report the result in \`verification\`. Fail-open: fix what you can, flag what you can't, always complete the write.\n` +
  `- Your .WIP.md, whenever you write one, carries as its FIRST TWO BODY LINES, immediately beneath its frontmatter and above Progress:\n` +
  `    delegated_by: ${fromSlug}\n` +
  `    question: ${question}\n` +
  `  Write them there every time you write or refresh the file. If you are interrupted, that file is the only attribution anyone has.\n` +
  `- If the payload does not carry enough for you to work honestly, return insufficient-context and name precisely what is missing. This is a PRAISED return, not a failure: an invented finding is strictly worse than declining. Never guess to be helpful.\n` +
  `- If this needs a human decision rather than the operation's work, return needs-human.\n` +
  `- Never carry a secret into the note, the log line, or your return.\n` +
  `\nYour \`headline\` is surfaced to the human by the caller. Write the one thing the dive found, plainly.\n` +
  `\n--- DELEGATED BY ---\n${fromSlug}\n` +
  `\n--- QUESTION ---\n${question}\n` +
  (why ? `\n--- WHY THEY ARE ASKING (what they are trying to finish, and why the answer must be findable later) ---\n${why}\n` : '') +
  (today ? `\n--- TODAY ---\n${today}\n` : '') +
  `\n--- GROUND IN (read every one of these live paths) ---\n${groundIn.length ? groundIn.join('\n') : '(nothing passed — if you cannot work without grounding, that is insufficient-context)'}\n`

const result = await agent(delegatePrompt, { label: `delegate:${op}`, phase: 'Delegate', schema: DELEGATE_RETURN })

// A null return is a killed or dead runner. `incomplete` is derived HERE, from that
// null — the runner is never asked to report its own interruption, because a runner
// that was killed cannot report anything. The engine has no filesystem access, so it
// hands back the probe rather than the resolved path: the caller resolves wipPath
// MECHANICALLY (newest *.WIP.md in {research} modified after the spawn stamp) and
// never by asking any agent. The mode reference owns that step.
if (!result) {
  return {
    op,
    fromSlug,
    degraded: true,
    returnType: 'incomplete',
    notePath: '',
    headline: '',
    verification: '',
    wikiCandidate: false,
    missing: [],
    wipProbe: { dir: researchPath, newerThan: spawnedAt, pattern: '*.WIP.md' },
    note: `the delegated ${op} run did not return — the dive was interrupted; nothing was invented in its place. Resolve the work-in-progress file mechanically from wipProbe (its first body lines name who asked and what for).`,
  }
}

if (result.available === false) {
  log(`the operation "vlt-${op}" could not be read — returning a degraded note, not a result.`)
  return {
    op,
    fromSlug,
    degraded: true,
    returnType: 'needs-human',
    notePath: '',
    headline: '',
    verification: '',
    wikiCandidate: false,
    missing: [],
    note: `the operation skill vlt-${op} could not be read at ${skillsPath}/vlt-${op}/SKILL.md — no work was done and nothing was invented in its place`,
  }
}

return {
  op,
  fromSlug,
  returnType: result.returnType,
  notePath: result.notePath || '',
  headline: result.headline || '',
  verification: result.verification || '',
  wikiCandidate: !!result.wikiCandidate,
  missing: Array.isArray(result.missing) ? result.missing : [],
  needsHuman: result.needsHuman || '',
}
