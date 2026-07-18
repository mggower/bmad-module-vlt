export const meta = {
  name: 'vlt-review-council',
  description: 'Run a persona-lens panel over a mint or a contested question and synthesize a structured verdict',
  whenToUse: 'Invoked by vlt-mint to gate a mint by blast-radius, or by a partner to debate a contested question. Returns Consensus / Disputed-resolved / Disputed-open / Recommended-actions (pass/revise/reject for a mint).',
  phases: [
    { title: 'Lenses', detail: 'spawn each selected persona lens in parallel, independently' },
    { title: 'Synthesis', detail: 'the moderator maps the positions into one structured verdict' },
  ],
}

// ─────────────────────────────────────────────────────────────────────────────
// vlt-review-council — the panel engine (Gap A: invoke-and-return + mandatory
// capture come free; both modes route through here).
//
// args (passed by the caller — vlt-mint via workflow('vlt-review-council', {...}),
// or the vlt-review-council SKILL for a debate):
//   {
//     mode:        'mint' | 'debate'          // required
//     kind:        string                     // mint mode only — drives panel selection
//     subject:     string                     // the proposal (mint) or question+context (debate).
//                                             //   MUST carry the LIVE project-tree path(s) of what is
//                                             //   under review — the lenses read those paths directly,
//                                             //   never a plugin-cache copy (Gap A sub-issue 3).
//     personasPath: string                    // absolute, {project-root}-anchored path to the live
//                                             //   personas dir (e.g. "/abs/vault/_meta/personas").
//                                             //   Resolving live is the cache fix — pass the real path.
//     lenses:      string[]  (optional)       // debate mode: caller may narrow the lens set.
//   }
// returns the structured verdict object (see SYNTHESIS schema).
// ─────────────────────────────────────────────────────────────────────────────

// The Workflow runtime delivers `args` as a JSON-encoded STRING, not the object the
// caller passed (true for name-, scriptPath-, and inline-script invocation alike).
// Parse defensively so the panel runs on the first try — without this, `a` is the raw
// string, `a.mode` is undefined, and the guard below wrongly reports "args missing".
let a = args || {}
if (typeof a === 'string') { try { a = JSON.parse(a) } catch { a = {} } }
const mode = a.mode
const kind = a.kind
const subject = a.subject
const personasPath = a.personasPath

if (!mode || !subject || !personasPath) {
  return {
    error: 'vlt-review-council requires { mode, subject, personasPath }. The caller (vlt-mint or the SKILL) names them.',
    received: { mode: mode || null, hasSubject: !!subject, hasPersonasPath: !!personasPath },
  }
}

// The fixed kind → council map — the SINGLE SOURCE OF TRUTH for panel composition.
// Callers (vlt-mint, the council SKILL) name a kind and let this select the lenses; they do
// NOT restate the composition (Theme 6 single-home fix). vlt-mint keeps only a cheap none-set
// predicate to skip the workflow for additive/reversible kinds.
const KIND_PANEL = {
  // Capability kinds (build-7). vlt-mint only invokes the workflow for the GATED case;
  // the additive ones below are [] and are normally skipped by vlt-mint's none-predicate.
  'add a capability': ['architect', 'skeptic', 'pragmatist'], // only reached when gated: a heavy cap writing a lane it doesn't rightfully own / a second writer — lane-discipline review
  'migrate a capability': [],          // re-owning an existing ability — additive/reversible
  'retire a capability': [],           // removing an ability the vault already had
  'create/extend a family': [],        // gathering existing invariants — additive
  'change family invariants': ['architect', 'skeptic', 'pragmatist', 'historian'], // cross-partner blast radius — every instance must re-conform (propagation, like a convention edit)
  // Back-compat aliases (pre-build-7 callers / mid-upgrade vlt-mint):
  'operation skill': [],
  'capability migration': [],
  // Partner / governance kinds:
  'new partner': ['architect', 'skeptic', 'pragmatist', 'historian'], // roster creation — highest blast radius; full panel so build-16's bell question reaches every lens and the historian reads the record (build-22: filled a composition stub)
  'persona self-edit': ['architect', 'skeptic', 'pragmatist', 'historian'],
  'convention edit': ['architect', 'skeptic', 'pragmatist', 'historian'],
  'retire a partner': ['architect', 'skeptic', 'pragmatist', 'historian'], // roster removal — full panel, same rationale as 'new partner' (build-22)
}

// Select the panel. Mint → by kind; debate → full panel (caller may narrow). Moderator is always added.
let lenses
if (mode === 'mint') {
  if (!(kind in KIND_PANEL)) {
    return { error: `unknown mint kind "${kind}" — expected one of ${Object.keys(KIND_PANEL).join(', ')}` }
  }
  lenses = KIND_PANEL[kind].slice()
  // A 'none' kind is gated nowhere — return immediately so vlt-mint proceeds frictionlessly.
  if (lenses.length === 0) {
    log(`kind "${kind}" → no review required; returning pass.`)
    return { mode, kind, reviewRequired: false, verdict: 'pass', note: 'no review required (additive/reversible)' }
  }
} else {
  // debate: default to the full deliberative panel unless the caller named a narrower set.
  lenses = Array.isArray(a.lenses) && a.lenses.length ? a.lenses.slice() : ['architect', 'skeptic', 'pragmatist', 'historian']
}

// Cap lens count so synthesis stays tractable (~5 incl. moderator → ~4 lenses).
if (lenses.length > 4) lenses = lenses.slice(0, 4)

const VERDICT = {
  type: 'object',
  additionalProperties: false,
  required: ['lens', 'available', 'position', 'concerns', 'recommendation'],
  properties: {
    lens: { type: 'string', description: 'the lens name (e.g. architect)' },
    available: { type: 'boolean', description: 'false if the persona file could not be read — then the rest is empty and this lens is dropped from synthesis' },
    position: { type: 'string', description: "this lens's position from its single axis, grounded in what it actually read" },
    concerns: { type: 'array', items: { type: 'string' }, description: 'concrete risks or objections this lens raises (may be empty)' },
    recommendation: { type: 'string', enum: ['pass', 'revise', 'reject', 'n/a'], description: "this lens's leaning (n/a for a debate with no pass/revise/reject frame)" },
  },
}

const SYNTHESIS = {
  type: 'object',
  additionalProperties: false,
  required: ['consensus', 'disputedResolved', 'disputedOpen', 'recommendedActions'],
  properties: {
    consensus: { type: 'array', items: { type: 'string' }, description: 'what every fielded lens actually agreed on' },
    disputedResolved: { type: 'array', items: { type: 'string' }, description: 'disagreements resolved WITH checkable reasoning — never by fiat' },
    disputedOpen: { type: 'array', items: { type: 'string' }, description: 'genuinely unresolved disagreements, named plainly' },
    recommendedActions: { type: 'array', items: { type: 'string' }, description: 'concrete next steps, attributable to the positions that produced them' },
    verdict: { type: 'string', enum: ['pass', 'revise', 'reject'], description: 'MINT MODE ONLY — the gate decision' },
    changes: { type: 'array', items: { type: 'string' }, description: "MINT MODE, verdict=revise — the specific changes required before the mint may proceed" },
    reason: { type: 'string', description: 'MINT MODE, verdict=reject — why the mint is rejected' },
  },
}

phase('Lenses')
log(`${mode} panel: ${lenses.join(', ')} + moderator (reading live personas at ${personasPath})`)

// Spawn each lens independently and in parallel — lenses do NOT see each other's positions
// (independence is what keeps them from collapsing into one another). Each reads its persona file
// and any live files the subject references from their real project-tree paths (the cache fix).
const lensPrompt = (lens) =>
  `You are the "${lens}" lens on a vlt review-council panel. ` +
  `Read the persona file at the LIVE path ${personasPath}/${lens}.md and apply its "Activation Prompt" section VERBATIM as your operating instructions — that section defines your single axis. ` +
  `If that file cannot be read, return { available: false } with empty fields and stop. ` +
  `Apply your lens to the subject below. If the subject references file paths, read them from those exact LIVE paths (the live project tree — never a cached or plugin copy), so you judge what will actually go live. ` +
  `Stay strictly in your lane: do not optimize for axes other lenses own. ` +
  // Mint-mode rubric line (single-home: the "where's the bell?" lens lives HERE, not in a persona —
  // gated kinds only, which is every kind that reaches lensPrompt in mint mode).
  (mode === 'mint'
    ? `Standing question for every mint review, from your axis: WHERE'S THE BELL? Does this mint create a rule someone else must obey — and if so, does it declare who checks / at what moment / against which counter, or carry a complete tripwired deferral (deferral_metric + deferral_threshold + review_after, all three)? A missing or incomplete answer on a boundary-creating mint is a concern to raise. `
    : '') +
  `Return your position from your single axis.\n\n--- SUBJECT (${mode}${kind ? `, kind: ${kind}` : ''}) ---\n${subject}`

const positions = (
  await parallel(lenses.map((lens) => () => agent(lensPrompt(lens), { label: `lens:${lens}`, phase: 'Lenses', schema: VERDICT })))
)
  .filter(Boolean)
  .filter((p) => p.available !== false)

if (positions.length === 0) {
  log('every selected lens was unavailable — moderator-only synthesis is not meaningful; returning a degraded verdict.')
  return {
    mode,
    kind,
    reviewRequired: true,
    degraded: true,
    note: 'no persona lenses could be read (check the personasPath / governance install) — no panel verdict produced',
    ...(mode === 'mint' ? { verdict: 'revise', changes: ['re-run once the review-lens personas are installed (vlt-setup installs the governance bundle)'] } : {}),
  }
}

phase('Synthesis')

// The moderator holds no stance — it maps the fielded positions into the structured verdict.
// It reads the moderator persona for its synthesis discipline, then synthesizes ONLY what the
// lenses actually returned (passed inline — the moderator does not re-run the lenses).
const moderatorPrompt =
  `You are the Moderator of a vlt review-council panel. ` +
  `Read the moderator persona at the LIVE path ${personasPath}/moderator.md and follow its "Activation Prompt" — you synthesize, you do not argue or hold a stance. ` +
  `Below are the fielded lens positions. Map them faithfully into the structured verdict: Consensus (only where ALL fielded lenses truly agree), Disputed-resolved (only with checkable reasoning), Disputed-open (name genuine unresolved disagreements — do not paper over them), and Recommended actions (concrete, attributable). ` +
  (mode === 'mint'
    ? `This is a MINT review: also return a single \`verdict\` of pass / revise / reject. Use 'revise' with a concrete \`changes\` list when the lenses raise fixable concerns; 'reject' with a \`reason\` only when a lens surfaces a disqualifying structural problem; 'pass' when concerns are minor or absent. HARD RULE (no boundary without a bell): a boundary-creating mint that lacks its Enforcement section, or carries an incomplete deferral (any of deferral_metric / deferral_threshold / review_after missing), is 'revise' or 'reject' — never 'pass'.`
    : `This is a DEBATE: do NOT return a pass/revise/reject verdict — leave \`verdict\` unset; the four sections are the product.`) +
  `\n\n--- SUBJECT (${mode}${kind ? `, kind: ${kind}` : ''}) ---\n${subject}\n\n--- FIELDED LENS POSITIONS ---\n${JSON.stringify(positions, null, 2)}`

const synthesis = await agent(moderatorPrompt, { label: 'moderator', phase: 'Synthesis', schema: SYNTHESIS })

if (!synthesis) {
  return { mode, kind, reviewRequired: true, degraded: true, note: 'moderator synthesis failed', positions }
}

return {
  mode,
  kind: kind || null,
  reviewRequired: true,
  lensesFielded: positions.map((p) => p.lens),
  ...synthesis,
}
