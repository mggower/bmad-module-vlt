export const meta = {
  name: 'vlt-consult',
  description: 'Ask one partner a question in another partner\'s domain and get an attributed answer back synchronously',
  whenToUse: "Invoked by vlt-dispatch's `consult` mode when a partner needs another's domain to finish its current move. Returns a typed union: answer / insufficient-context / wrong-partner / needs-human / needs-work.",
  phases: [
    { title: 'Consult', detail: 'spawn the summoned partner; it answers as itself or names what it cannot answer' },
  ],
}

// ─────────────────────────────────────────────────────────────────────────────
// vlt-consult — the synchronous partner→partner consult engine.
//
// Depth-1 is STRUCTURAL, not an honor system: this workflow spawns exactly ONE
// agent, and a spawned agent cannot re-enter a workflow. The summoned partner
// therefore cannot chain a consult of its own — the boundary-erosion risk is
// closed by the shape of the engine, not by a prose rule it could talk past.
//
// The typed return union is FORCED by the schema below, so `insufficient-context`
// is a first-class return the model cannot prose its way around. A thin payload
// producing an invented opinion is strictly worse than no mechanism at all:
// read-and-cite cannot impersonate, and a confabulated partner voice is exactly
// what the operating contract's authority boundary forbids.
//
// args (passed by vlt-dispatch's `consult` mode):
//   {
//     fromSlug:     string    // the calling partner's routing slug
//     toSlug:       string    // the summoned partner's routing slug
//     question:     string    // the question, in the caller's own framing
//     why:          string    // what the caller is trying to finish, and which part
//                             //   of it is outside its authority. The anti-confabulation
//                             //   field: it is what lets the summoned partner return
//                             //   wrong-partner / insufficient-context ACCURATELY rather
//                             //   than producing a plausible opinion about a question it
//                             //   was never really asked.
//     groundIn:     string[]  // LIVE absolute paths the summoned partner must read.
//                             //   Never a plugin-cache copy — the council learned this
//                             //   the hard way; pass the real project-tree paths.
//     skillsPath:   string    // absolute path to the installed skills dir (holds vlt-agent-*)
//     partnersPath: string    // absolute path to {partners} (holds <slug>/identity.md, thread.md)
//     today:        string    // 'YYYY-MM-DD' — the script has no clock and must not invent one
//   }
// returns the CONSULT_RETURN object (plus `degraded: true` + a note when the
// summoned partner could not be read).
// ─────────────────────────────────────────────────────────────────────────────

// The Workflow runtime delivers `args` as a JSON-encoded STRING, not the object the
// caller passed (true for name-, scriptPath-, and inline-script invocation alike).
// Parse defensively so the consult runs on the first try — without this, `a` is the raw
// string, `a.toSlug` is undefined, and the guard below wrongly reports "args missing".
let a = args || {}
if (typeof a === 'string') { try { a = JSON.parse(a) } catch { a = {} } }

const fromSlug = a.fromSlug
const toSlug = a.toSlug
const question = a.question
const why = a.why || ''
const groundIn = Array.isArray(a.groundIn) ? a.groundIn : []
const skillsPath = a.skillsPath
const partnersPath = a.partnersPath
const today = a.today || ''

if (!fromSlug || !toSlug || !question || !skillsPath) {
  return {
    error: 'vlt-consult requires { fromSlug, toSlug, question, skillsPath }. vlt-dispatch\'s `consult` mode names them.',
    received: {
      fromSlug: fromSlug || null,
      toSlug: toSlug || null,
      hasQuestion: !!question,
      hasSkillsPath: !!skillsPath,
    },
  }
}

if (fromSlug === toSlug) {
  return {
    error: `a partner does not consult itself (fromSlug === toSlug === "${fromSlug}")`,
    received: { fromSlug, toSlug },
  }
}

const CONSULT_RETURN = {
  type: 'object',
  additionalProperties: false,
  required: ['available', 'returnType', 'answer', 'stanceChanged', 'groundedIn'],
  properties: {
    available: {
      type: 'boolean',
      description: 'false if the summoned partner\'s SKILL could not be read — then the rest is empty and the caller gets a degraded, clearly-labelled note rather than an invented answer',
    },
    returnType: {
      type: 'string',
      enum: ['answer', 'insufficient-context', 'wrong-partner', 'needs-human', 'needs-work'],
      description: 'the typed return. `insufficient-context` is a FIRST-CLASS, praised return — never a failure to apologize for',
    },
    answer: {
      type: 'string',
      description: 'the raw answer in the summoned partner\'s OWN voice, verbatim — the caller surfaces this attributed, before using it. Empty for wrong-partner/needs-human where there is nothing to say from this domain',
    },
    wrongPartner: {
      type: 'string',
      description: 'returnType=wrong-partner ONLY — the slug of the partner whose domain this question actually falls in, or empty if none is apparent',
    },
    missing: {
      type: 'array',
      items: { type: 'string' },
      description: 'returnType=insufficient-context ONLY — precisely what the payload lacked (a path not passed, a decision not stated, context only the caller holds)',
    },
    stanceChanged: {
      type: 'boolean',
      description: 'whether this consult MOVED the summoned partner\'s position (a new stance, a revised one, a genuinely new open question). Gates its thread.md write — false means the consult merely confirmed what it already held, and the prunable file stays untouched',
    },
    groundedIn: {
      type: 'array',
      items: { type: 'string' },
      description: 'the paths actually read, so the caller can see whether the answer rests on the payload or on nothing',
    },
  },
}

phase('Consult')
log(`consult: ${fromSlug} → ${toSlug} (grounding in ${groundIn.length} path(s))`)

const consultPrompt =
  `You are the vault partner whose routing slug is "${toSlug}". ` +
  `Read your SKILL at the LIVE path ${skillsPath}/vlt-agent-${toSlug}/SKILL.md and BECOME that partner — answer in its own voice, from its own expertise, with its own manner. ` +
  (partnersPath
    ? `Also read ${partnersPath}/${toSlug}/identity.md and ${partnersPath}/${toSlug}/thread.md if they exist — your accumulated identity in this vault and what you are currently on. `
    : '') +
  `If your SKILL file cannot be read, return { available: false } with empty fields and stop — do NOT answer as a generic assistant. ` +
  `\n\nYou have been CONSULTED by the partner "${fromSlug}". A consult is synchronous and depth-1: you answer, and you are done. ` +
  `HARD RULES:\n` +
  `- You may READ anything you are entitled to read, and you must read every path listed under GROUND IN below from those exact LIVE paths.\n` +
  `- You write NOTHING, with exactly one exception: if this consult genuinely moved your position, you may append to your OWN ${partnersPath ? `${partnersPath}/${toSlug}/thread.md` : 'thread.md'}${today ? ` (dated ${today})` : ''} — your own memory, never anyone else's. Set stanceChanged accordingly. If the consult merely confirmed what you already held, write nothing and set stanceChanged false.\n` +
  `- You NEVER summon another partner. You do not consult, relay, hand off, or spawn. If the answer needs someone else, say so through the return type.\n` +
  `- You answer ONLY from your own domain. If this question is not yours, return wrong-partner and name whose it is.\n` +
  `- If the payload does not carry enough for you to answer honestly, return insufficient-context and name precisely what is missing. This is a PRAISED return, not a failure: an invented opinion in your voice manufactures authority the answer does not have, which is strictly worse than declining. Never guess to be helpful.\n` +
  `- If the honest answer is that work must be done rather than a question answered, return needs-work — the caller will route it through the asynchronous relay path. You do not do the work.\n` +
  `- If this needs a human decision rather than a partner's judgment, return needs-human.\n` +
  `\nYour \`answer\` is surfaced to the human VERBATIM and attributed to you, before the caller uses it. Write it as you would say it.\n` +
  `\n--- CONSULTED BY ---\n${fromSlug}\n` +
  `\n--- QUESTION ---\n${question}\n` +
  (why ? `\n--- WHY THEY ARE ASKING (what they are trying to finish, and which part is outside their authority) ---\n${why}\n` : '') +
  `\n--- GROUND IN (read every one of these live paths) ---\n${groundIn.length ? groundIn.join('\n') : '(nothing passed — if you cannot answer without grounding, that is insufficient-context)'}\n`

const result = await agent(consultPrompt, { label: `consult:${toSlug}`, phase: 'Consult', schema: CONSULT_RETURN })

if (!result) {
  return {
    fromSlug,
    toSlug,
    degraded: true,
    returnType: 'needs-human',
    answer: '',
    note: `the consult of "${toSlug}" did not return — no answer was produced; nothing was invented in its place`,
  }
}

if (result.available === false) {
  log(`the summoned partner "${toSlug}" could not be read — returning a degraded note, not an answer.`)
  return {
    fromSlug,
    toSlug,
    degraded: true,
    returnType: 'needs-human',
    answer: '',
    note: `could not read ${skillsPath}/vlt-agent-${toSlug}/SKILL.md — no partner was fielded, so no attributed answer exists. Check the slug and the installed roster.`,
    groundedIn: [],
    stanceChanged: false,
  }
}

return {
  fromSlug,
  toSlug,
  degraded: false,
  ...result,
}
