#!/usr/bin/env node
// Cycle 16 build-3 — the at-rest instrument for acceptance check (2) Delegate (brief F10;
// §Verification 10 and 11). Loads the SHIPPED `vlt-delegate.js` through Cycle 15's shared shim,
// which delivers `args` as a JSON STRING exactly as the runtime does (§Verification 11: every leg
// below is also a parse-on-intake assertion — a script that skipped the parse would report
// "args missing" on the first leg).
//
// The stub is a COUNTER: the spawn count is asserted PER LEG, because `too-big` being the ENGINE's
// ruling (not a spawned agent's opinion) is only observable as ZERO invocations.
//
// Leg 4 (`incomplete`) is driven by a FORCED NULL return — the shape a killed runner produces —
// never by a cooperative "stop after writing your WIP" prompt, which would test the fix's shape
// rather than the failure's (A12 i). The harness then performs the CALLER's mechanical probe
// (newest *.WIP.md under the probe dir, modified after the spawn stamp) over a PRE-PLANTED file,
// and asserts its first two body lines carry the attribution.
//
// Run: node factory/cycles/16-closed-loops/fixtures/build-3-delegate-harness.mjs

import fs from 'node:fs'
import os from 'node:os'
import path from 'node:path'
import { REPO, run, readSrc } from '../../15-nothing-reads-it-back/fixtures/vlt-lint-full-shim.mjs'

const ENGINE = path.join(REPO, 'skills', 'vlt-setup', 'assets', 'workflows', 'vlt-delegate.js')
const src = readSrc(ENGINE)

let failures = 0
const check = (label, ok, detail = '') => {
  if (!ok) failures++
  console.log(`${ok ? 'PASS' : 'FAIL'}  ${label}${detail ? ` — ${detail}` : ''}`)
}

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'build-3-delegate-'))
const RESEARCH = path.join(tmp, 'research')
fs.mkdirSync(RESEARCH, { recursive: true })

const base = {
  op: 'research',
  fromSlug: 'creative',
  question: 'what is the retention window for the vendor API?',
  why: 'finishing a PARA brief; the number must be findable later',
  groundIn: [path.join(tmp, 'ground.md')],
  skillsPath: path.join(REPO, 'skills'),
  researchPath: RESEARCH,
  logPath: path.join(tmp, 'log.md'),
  today: '2026-09-17',
  spawnedAt: '2026-09-17 10:00:00',
}

console.log('leg 1 — a thin payload → insufficient-context, ONE runner spawned')
let r = await run(src, { ...base, groundIn: [] }, async () => ({
  available: true, returnType: 'insufficient-context', notePath: '', headline: '', verification: '',
  wikiCandidate: false, missing: ['no grounding paths were passed'],
}))
check('returnType insufficient-context', r.result.returnType === 'insufficient-context', JSON.stringify(r.result.returnType))
check('exactly 1 agent spawned', r.invocations === 1, `invocations=${r.invocations}`)
check('the missing list survives to the caller', Array.isArray(r.result.missing) && r.result.missing.length === 1, JSON.stringify(r.result.missing))

console.log('\nleg 2 — depth: deep → too-big, ZERO runners spawned (the engine rules, not an agent)')
r = await run(src, { ...base, depth: 'deep' }, async () => { throw new Error('must not spawn') })
check('returnType too-big', r.result.returnType === 'too-big', JSON.stringify(r.result.returnType))
check('ZERO agents spawned', r.invocations === 0, `invocations=${r.invocations}`)
check('the refusal is logged, not silent', r.logs.some((l) => /refused before spawning/.test(l)), JSON.stringify(r.logs))

console.log('\nleg 3 — a quick dive → done{notePath, headline, verification, wikiCandidate}')
const NOTE = path.join(RESEARCH, '2026-09-17-101500-vendor-api-retention-window.md')
r = await run(src, { ...base, depth: 'quick' }, async (prompt, o) => {
  // prompt assertions, on the leg that actually dives
  check('the runner is told it is PARTNERLESS and nobody', /PARTNERLESS RUNNER/.test(prompt) && /You are nobody/.test(prompt))
  check('every tag it writes carries the CALLER', new RegExp(`carries the CALLER's slug, "creative"`).test(prompt))
  check('it is forbidden a session note', /You write \*\*NO session note\*\*|write \*\*NO session note\*\*|NO session note/.test(prompt))
  check('it is forbidden the wiki and the Librarian hand-off', /NOTHING under the wiki/.test(prompt) && /never offer or perform the Librarian hand-off/.test(prompt))
  check('it carries NO card/rung text — only that they arrive with the session',
    !/Act-blocking rules|Write boundaries\./.test(prompt) && /arrive with this session through the vault's CLAUDE\.md/.test(prompt))
  check('the .WIP.md attribution lines are required, in the body', /delegated_by: creative/.test(prompt) && /FIRST TWO BODY LINES/.test(prompt))
  check('the label names the op', o && o.label === 'delegate:research', String(o && o.label))
  return { available: true, returnType: 'done', notePath: NOTE, headline: 'the vendor keeps 30 days', verification: 'passed', wikiCandidate: true }
})
check('returnType done', r.result.returnType === 'done', JSON.stringify(r.result.returnType))
check('exactly 1 agent spawned', r.invocations === 1, `invocations=${r.invocations}`)
check('notePath, headline, verification and wikiCandidate all reach the caller',
  r.result.notePath === NOTE && r.result.headline && r.result.verification === 'passed' && r.result.wikiCandidate === true,
  JSON.stringify(r.result))
check('fromSlug is echoed for the caller-tagged record', r.result.fromSlug === 'creative', String(r.result.fromSlug))

console.log('\nleg 4 — a killed runner (forced null) → incomplete, with the probe the caller resolves')
const WIP = path.join(RESEARCH, '2026-09-17-101500-vendor-api-retention-window.WIP.md')
fs.writeFileSync(WIP, `---\ntype: research\n---\n\ndelegated_by: creative\nquestion: ${base.question}\n\n## Progress\n\n- one sub-question done\n`)
r = await run(src, base, async () => null)
check('returnType incomplete', r.result.returnType === 'incomplete', JSON.stringify(r.result.returnType))
check('exactly 1 agent spawned', r.invocations === 1, `invocations=${r.invocations}`)
check('degraded is labelled, nothing invented', r.result.degraded === true && /did not return/.test(r.result.note || ''), JSON.stringify(r.result.note))
check('the probe names the dir, the stamp and the pattern',
  r.result.wipProbe && r.result.wipProbe.dir === RESEARCH && r.result.wipProbe.newerThan === base.spawnedAt && r.result.wipProbe.pattern === '*.WIP.md',
  JSON.stringify(r.result.wipProbe))
// the CALLER's mechanical step (references/delegate.md, Route the return): newest *.WIP.md, by mtime
const since = Date.parse('2026-09-17T10:00:00Z')
const found = fs.readdirSync(r.result.wipProbe.dir)
  .filter((n) => n.endsWith('.WIP.md'))
  .map((n) => path.join(r.result.wipProbe.dir, n))
  .filter((p) => fs.statSync(p).mtimeMs > since)
  .sort((a, b) => fs.statSync(b).mtimeMs - fs.statSync(a).mtimeMs)[0]
check('the mechanical probe resolves the pre-planted WIP', found === WIP, String(found))
const body = fs.readFileSync(WIP, 'utf8').split('---')[2].trim().split('\n').slice(0, 2)
check('its first two body lines attribute caller and question',
  body[0] === 'delegated_by: creative' && body[1] === `question: ${base.question}`, JSON.stringify(body))

console.log('\nleg 5 — an unreadable op skill → a labelled degraded return, never an invented result')
r = await run(src, { ...base, skillsPath: path.join(tmp, 'no-such-skills') }, async () => ({
  available: false, returnType: 'done', notePath: '', headline: '', verification: '', wikiCandidate: false,
}))
check('returnType needs-human, degraded', r.result.returnType === 'needs-human' && r.result.degraded === true, JSON.stringify(r.result.returnType))
check('exactly 1 agent spawned', r.invocations === 1, `invocations=${r.invocations}`)
check('the note names the unreadable skill and invents nothing',
  /could not be read/.test(r.result.note || '') && r.result.headline === '' && r.result.notePath === '', JSON.stringify(r.result.note))

console.log('\nguards — the enum and the required args, before any spawn')
r = await run(src, { ...base, op: 'ingest' }, async () => { throw new Error('must not spawn') })
check('an op outside the v1 enum is refused', /not a delegable operation/.test(r.result.error || ''), JSON.stringify(r.result.error))
check('ZERO agents spawned on the enum refusal', r.invocations === 0, `invocations=${r.invocations}`)
r = await run(src, { op: 'research' }, async () => { throw new Error('must not spawn') })
check('missing required args are named, not guessed', /requires \{ fromSlug, question, skillsPath \}/.test(r.result.error || ''), JSON.stringify(r.result.error))
check('ZERO agents spawned on the args refusal', r.invocations === 0, `invocations=${r.invocations}`)

fs.rmSync(tmp, { recursive: true, force: true })
console.log(`\n${failures ? `${failures} expectation(s) FAILED` : 'all expectations hold'}`)
process.exit(failures ? 1 : 0)
