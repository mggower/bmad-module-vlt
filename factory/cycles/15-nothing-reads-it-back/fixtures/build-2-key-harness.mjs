#!/usr/bin/env node
// Cycle 15 build-2 — the at-rest instrument for acceptance checks (1) and (2).
//
// Loads `vlt-lint-full.js` the way package-lint's E6 does (node over the file), rewrites
// `export const meta` to `const meta`, wraps the body in an AsyncFunction with the runtime
// globals stubbed, and runs the case table from the brief's §Acceptance (1). `args` is
// delivered as a JSON STRING, exactly as the runtime does. The agent stub returns null, so
// a page the workflow decides to re-scan surfaces as `agent_failed` — the honest observable
// that exactly those slugs were dispatched — and a fully-reused run dispatches nothing.
//
// The sidecar fixture's keys are RE-COMPOSED in memory by the code under test before the
// cases run (a `gen` pass whose agent stub hands back each record's own scan), so the
// harness stays valid after a later build moves the scan surface; `--regen` rewrites the
// committed fixture's keys from that pass. The committed keys are checked against it and
// reported (informational — a stale committed key is fixture drift, not a key-logic fault).
//
// Usage:
//   node build-2-key-harness.mjs                       # case table over the shipped workflow
//   node build-2-key-harness.mjs --workflow <path> --legacy   # the pre-build workflow (0e01381)
//   node build-2-key-harness.mjs --sidecar <path>      # "unchanged inputs" over a sidecar on disk (check 2)
//   node build-2-key-harness.mjs --regen               # rewrite build-2-sidecar.json's keys
//   node build-2-key-harness.mjs --fingerprint         # print scanFingerprint only (Verification 2)
// Exit 0 when every expectation in the selected mode holds, 1 otherwise.

import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const HERE = path.dirname(fileURLToPath(import.meta.url))
const REPO = path.resolve(HERE, '..', '..', '..', '..')
const SHIPPED = path.join(REPO, 'skills', 'vlt-setup', 'assets', 'workflows', 'vlt-lint-full.js')
const SIDECAR_FIXTURE = path.join(HERE, 'build-2-sidecar.json')

const argv = process.argv.slice(2)
const flag = (name) => argv.includes(name)
const opt = (name) => { const i = argv.indexOf(name); return i >= 0 ? argv[i + 1] : undefined }
const workflowPath = opt('--workflow') || SHIPPED
const legacy = flag('--legacy')

// ── runtime shim ─────────────────────────────────────────────────────────────
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor
const compile = (src) => new AsyncFunction('args', 'agent', 'parallel', 'phase', 'log', 'budget', 'workflow',
  src.replace(/^export const meta =/m, 'const meta ='))

async function run(src, args, agentStub = async () => null) {
  const logs = []
  const fn = compile(src)
  const result = await fn(
    JSON.stringify(args),                       // the runtime delivers args as a JSON string
    agentStub,
    (thunks) => Promise.all(thunks.map((t) => t())),
    () => {},
    (m) => logs.push(String(m)),
    { total: 0, remaining: () => 0 },
    async () => null,
  )
  return { result, logs }
}

// ── fixture + baseline inputs ────────────────────────────────────────────────
const fixture = JSON.parse(fs.readFileSync(SIDECAR_FIXTURE, 'utf8'))
const allRecords = fixture.records
const hashOf = (slug) => `sha256-${slug}-baseline-bytes`.padEnd(64, '0')
const DIGEST = {
  frontmatter: '1111111111111111',
  'wiki-supersession': '2222222222222222',
  'write-verification': '3333333333333333',
}
const baselineArgs = (records, cachedScans) => ({
  pages: records.map((r) => ({ slug: r.slug, path: `/vault/wiki/${r.slug}.md` })),
  indexPath: '/vault/wiki/index.md',
  conventionsPath: '/vault/_agent/conventions',
  today: '2026-09-02',
  pageHashes: Object.fromEntries(records.map((r) => [r.slug, hashOf(r.slug)])),
  cachedScans,
  rulesetComponents: {
    convention_digests: { ...DIGEST },
    // The pre-build workflow requires these three slots; the post-build one ignores them
    // (case (b) is exactly that difference).
    ...(legacy ? { module_version: '0.17.1', pin_vector: 'frontmatter@14 wiki-index@2', checks_digest: '4444444444444444' } : {}),
  },
})

// The gen pass: under baseline inputs and an EMPTY cache, an agent stub that returns each
// record's own scan makes the workflow compose and return one cache_record per page — the
// keys the code under test would have written. Those are the "written under baseline" keys.
async function rekey(src, records) {
  const bySlug = new Map(records.map((r) => [r.slug, r.scan]))
  const stub = async (_prompt, o) => (o && typeof o.label === 'string' && o.label.startsWith('scan:')) ? structuredClone(bySlug.get(o.label.slice(5))) : null
  const { result } = await run(src, baselineArgs(records, []), stub)
  if (!Array.isArray(result.cache_records) || result.cache_records.length !== records.length) {
    throw new Error(`gen pass did not return ${records.length} cache_records: ${JSON.stringify(result).slice(0, 300)}`)
  }
  const keyOf = new Map(result.cache_records.map((c) => [c.slug, c.key]))
  return {
    records: records.map((r) => ({ slug: r.slug, key: keyOf.get(r.slug), scan: r.scan })),
    scanFingerprint: String(result.cache_fingerprint || '').split('|')[0],
  }
}

const src = fs.readFileSync(workflowPath, 'utf8')
const observe = (r) => ({
  files_cached: r.result.files_cached,
  agent_failed: r.result.agent_failed || [],
  cache_miss_terms: r.result.cache_miss_terms,
  caps: r.result.coverage_caps || [],
  logs: r.logs,
  error: r.result.error,
})

let failures = 0
const check = (label, ok, detail) => { if (!ok) failures++; console.log(`${ok ? 'PASS' : 'FAIL'}  ${label}${detail ? ` — ${detail}` : ''}`) }

// ── --fingerprint: Verification 2 (prompt-text invariance) ──────────────────
if (flag('--fingerprint')) {
  const { scanFingerprint } = await rekey(src, allRecords.slice(0, 2))
  console.log(scanFingerprint)
  process.exit(0)
}

// ── --regen: rewrite the committed fixture's keys ────────────────────────────
if (flag('--regen')) {
  const { records } = await rekey(src, allRecords)
  fs.writeFileSync(SIDECAR_FIXTURE, JSON.stringify({ ...fixture, records }, null, 2) + '\n')
  console.log(`rewrote ${records.length} keys into ${path.relative(REPO, SIDECAR_FIXTURE)}`)
  process.exit(0)
}

// ── --sidecar <path>: check (2) — "unchanged inputs" over a sidecar on disk ──
if (opt('--sidecar')) {
  const onDisk = JSON.parse(fs.readFileSync(opt('--sidecar'), 'utf8'))
  const { records: keyed } = await rekey(src, allRecords)
  const keyOf = new Map(keyed.map((r) => [r.slug, r.key]))
  // The page list is the FULL fixture (all pages still exist); the cache is what the evict left.
  const cached = (onDisk.records || []).map((r) => ({ ...r, key: keyOf.get(r.slug) ?? r.key }))
  const o = observe(await run(src, baselineArgs(allRecords, cached)))
  const expectFailed = allRecords.map((r) => r.slug).filter((s) => !cached.some((c) => c.slug === s))
  console.log(JSON.stringify({ files_cached: o.files_cached, agent_failed: o.agent_failed, cache_miss_terms: o.cache_miss_terms }))
  check('exactly the evicted page(s) re-dispatched', JSON.stringify(o.agent_failed) === JSON.stringify(expectFailed), `agent_failed=${JSON.stringify(o.agent_failed)} expected=${JSON.stringify(expectFailed)}`)
  check('the rest reused', o.files_cached === cached.length, `files_cached=${o.files_cached}`)
  process.exit(failures ? 1 : 0)
}

// ── the case table (check 1) ─────────────────────────────────────────────────
const two = allRecords.slice(0, 2)
const { records: keyed, scanFingerprint } = await rekey(src, two)
const committedCurrent = two.every((r) => keyed.find((k) => k.slug === r.slug).key === r.key)
console.log(`workflow: ${path.relative(REPO, workflowPath)}${legacy ? ' (legacy slots supplied)' : ''}`)
console.log(`scanFingerprint: ${scanFingerprint}`)
console.log(`committed fixture keys current: ${committedCurrent ? 'yes' : 'NO (run --regen)'}`)

const base = () => baselineArgs(two, structuredClone(keyed))
const withComponents = (patch) => { const a = base(); Object.assign(a.rulesetComponents, patch); return a }
const withDigest = (name, digest) => { const a = base(); a.rulesetComponents.convention_digests[name] = digest; return a }
const withoutDigest = (name) => { const a = base(); delete a.rulesetComponents.convention_digests[name]; return a }
const withScanModel = (m) => { const a = base(); a.scanModel = m; return a }
const mutatedSchema = () => {
  const needle = "'false if the page file could not be read'"
  if (!src.includes(needle)) throw new Error('PAGE_SCAN needle not found — update the harness')
  return src.replace(needle, "'false if the page file could not be read.'")
}

const cases = [
  { id: 'a', name: 'identical inputs', args: base(), warm: true },
  { id: 'b', name: 'extra module_version slot, different value', args: withComponents({ module_version: '0.18.0-different' }), warm: !legacy, flip: true },
  // (c) also flips: the pre-build key composed EVERY name passed, so a fourth convention went cold.
  { id: 'c', name: 'fourth convention (extraction) added', args: withDigest('extraction', '5555555555555555'), warm: !legacy, logNames: 'extraction', flip: true },
  { id: 'd', name: 'wiki-supersession digest changed', args: withDigest('wiki-supersession', 'ffffffffffffffff'), warm: false, term: 'ruleset' },
  { id: 'e', name: "scanModel: 'sonnet'", args: withScanModel('sonnet'), warm: legacy, term: 'ruleset', flip: true },
  { id: 'f', name: 'one byte of PAGE_SCAN changed', args: base(), src: mutatedSchema(), warm: false, term: 'scan_surface' },
  // (g)'s cap literal was re-keyed by build-3 (its F7): the one-word `absent or empty slots [...]`
  // cap became two caps, and an ABSENT name now renders under its own word.
  { id: 'g', name: 'convention_digests missing write-verification', args: withoutDigest('write-verification'), warm: false, capNames: 'absent [convention_digests[write-verification]]' },
]

console.log('\ncase  files_cached  agent_failed                          cache_miss_terms')
for (const c of cases) {
  const o = observe(await run(c.src || src, c.args))
  const terms = o.cache_miss_terms ? JSON.stringify(o.cache_miss_terms) : '(not returned)'
  console.log(`(${c.id})   ${String(o.files_cached).padEnd(13)} ${JSON.stringify(o.agent_failed).padEnd(37)} ${terms}   ${c.name}${c.flip ? '  [flips between builds]' : ''}`)
  const warm = o.files_cached === 2 && o.agent_failed.length === 0
  const cold = o.files_cached === 0 && o.agent_failed.length === 2
  check(`(${c.id}) ${c.warm ? 'warm' : 'cold'}`, c.warm ? warm : cold, o.error ? `error: ${o.error}` : '')
  if (!legacy && c.term) check(`(${c.id}) cache_miss_terms.${c.term} === 2`, o.cache_miss_terms && o.cache_miss_terms[c.term] === 2, terms)
  if (!legacy && c.logNames) check(`(${c.id}) one log line names the ignored name`, o.logs.filter((l) => l.includes(c.logNames)).length === 1, JSON.stringify(o.logs.filter((l) => l.includes(c.logNames))))
  if (!legacy && c.capNames) check(`(${c.id}) cap names ${c.capNames}`, o.caps.some((m) => m.includes(c.capNames)), JSON.stringify(o.caps))
}

// The scanModel type guard (brief disposition 3): a present non-string is refused up front.
if (!legacy) {
  const o = observe(await run(src, withScanModel(['haiku'])))
  check('scanModel: [array] refused with the args-guard error shape', typeof o.error === 'string' && o.error.includes('scanModel'), o.error)
}

console.log(`\n${failures ? `${failures} expectation(s) FAILED` : 'all expectations hold'}`)
process.exit(failures ? 1 : 0)
