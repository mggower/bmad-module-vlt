#!/usr/bin/env node
// Cycle 14 build-2 (A14-8) — the documented-invocation harness (acceptance check 4).
//
// A FACTORY RECORD, never copied into a vault. It extracts the two `lint-cache.py`
// command lines VERBATIM from skills/vlt-lint/references/full-scale.md (steps 2 and 5),
// substitutes only the file's own declared placeholders ($SKILL, {project-root}, and the
// <angle-bracket> value slots), and EXECUTES them. A divergence between the prose and the
// script's argument parser is a failure here, not a transcription note: the seam A14-8
// names is exactly "a contract stated in prose with no enforcement point where it meets
// the code".
//
// Run: node factory/cycles/14-no-enforcement-point/lint-cache-documented-invocation.mjs [tmpdir]

import { execFileSync } from 'node:child_process'
import fs from 'node:fs'
import os from 'node:os'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const REPO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..')
const DOC = path.join(REPO, 'skills/vlt-lint/references/full-scale.md')
const SKILL = path.join(REPO, 'skills/vlt-lint')
const ROOT = process.argv[2] || fs.mkdtempSync(path.join(os.tmpdir(), 'lint-cache-doc-'))

const doc = fs.readFileSync(DOC, 'utf8')
const extracted = [...doc.matchAll(/`(uv run [^`]*lint-cache\.py[^`]*)`/g)].map((m) => m[1])
if (extracted.length !== 2) { console.log(`FAIL — expected 2 documented command lines, extracted ${extracted.length}`); process.exit(1) }
const [readCmd, writeCmd] = extracted
console.log('extracted verbatim from full-scale.md:')
for (const c of extracted) console.log('  ' + c)

const vault = path.join(ROOT, 'vault')
fs.mkdirSync(path.join(vault, '_agent'), { recursive: true })
const recordsPath = path.join(ROOT, 'records.json')
fs.writeFileSync(recordsPath, JSON.stringify([{ slug: 'alpha', key: 'h|s|r', scan: { slug: 'alpha', available: true } }]))

// Only the file's own placeholders are substituted; every other token runs as written.
const resolve = (cmd) => cmd
  .replaceAll('"$SKILL/scripts/lint-cache.py"', JSON.stringify(path.join(SKILL, 'scripts/lint-cache.py')))
  .replaceAll('{project-root}', vault)
  .replaceAll('<cache_fingerprint>', 'scanfp|rulesetfp')
  .replaceAll('<path|->', recordsPath)
const run = (cmd) => {
  const argv = cmd.match(/"[^"]*"|\S+/g).map((t) => (t.startsWith('"') ? JSON.parse(t) : t))
  try {
    const out = execFileSync(argv[0], argv.slice(1), { encoding: 'utf8' })
    return { code: 0, out: out.trim() }
  } catch (e) { return { code: e.status === undefined ? -1 : e.status, out: String(e.stdout || '').trim(), err: String(e.stderr || '').trim() } }
}

let failures = 0
const check = (name, cond, detail) => { if (cond) console.log(`  PASS  ${name}`); else { failures++; console.log(`  FAIL  ${name}${detail ? ' — ' + detail : ''}`) } }

console.log('\nstep 2 — read, three sidecar states (all exit 0: a cold run is never an error)')
const missing = run(resolve(readCmd))
console.log(`  missing:     exit ${missing.code}  ${missing.out}`)
check('(4a) a MISSING sidecar returns status "missing" at exit 0', missing.code === 0 && JSON.parse(missing.out).status === 'missing')

fs.writeFileSync(path.join(vault, '_agent', 'lint-cache.json'), '{ this is not json')
const corrupt = run(resolve(readCmd))
console.log(`  unparseable: exit ${corrupt.code}  ${corrupt.out}`)
check('(4b) a CORRUPT sidecar returns status "unparseable" at exit 0', corrupt.code === 0 && JSON.parse(corrupt.out).status === 'unparseable')

console.log('\nstep 5 — write, exactly as documented')
const written = run(resolve(writeCmd))
console.log(`  write:       exit ${written.code}  ${written.out}${written.err ? ' | stderr: ' + written.err : ''}`)
check('(4c) the documented WRITE command line runs as written and exits 0', written.code === 0 && JSON.parse(written.out).written === 1)

const ok = run(resolve(readCmd))
console.log(`  read back:   exit ${ok.code}  ${ok.out}`)
check('(4d) the sidecar the documented write produced reads back as status "ok"', ok.code === 0 && JSON.parse(ok.out).status === 'ok' && JSON.parse(ok.out).count === 1)

console.log(`\n${failures === 0 ? 'ALL CHECKS PASS' : failures + ' CHECK(S) FAILED'}`)
process.exit(failures === 0 ? 0 : 1)
