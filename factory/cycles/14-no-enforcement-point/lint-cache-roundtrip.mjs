#!/usr/bin/env node
// Cycle 14 build-2 (A14-8) — the findings-cache round-trip harness.
//
// A FACTORY RECORD, never copied into a vault: it lives under factory/cycles/ and is
// durable, re-runnable by a later cycle, not a scratch script.
//
// What it grades (build-2 acceptance checks 1, 2, 3, 5, 6) and — the part b2(5) got
// wrong — WHAT IT REFUSES TO STUB: the sidecar write. Cycle 12's harness ran two runs
// inside one process with the SKILL-side write step stubbed, which is the exact seam
// that was broken, so it passed over a cache that has never once worked. Here every
// read and every write goes through the SHIPPED skills/vlt-lint/scripts/lint-cache.py
// as a subprocess, against a real temp vault dir, and the workflow is the SHIPPED
// skills/vlt-setup/assets/workflows/vlt-lint-full.js source. Only the page-scanner
// agents are stubbed — nothing else.
//
// Run: node factory/cycles/14-no-enforcement-point/lint-cache-roundtrip.mjs [tmpdir]

import { execFileSync } from 'node:child_process'
import fs from 'node:fs'
import os from 'node:os'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const REPO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..')
const WORKFLOW = path.join(REPO, 'skills/vlt-setup/assets/workflows/vlt-lint-full.js')
const SCRIPT = path.join(REPO, 'skills/vlt-lint/scripts/lint-cache.py')
const ROOT = process.argv[2] || fs.mkdtempSync(path.join(os.tmpdir(), 'lint-cache-rt-'))

const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor

// ── the corpus (synthetic by necessity — no wiki corpus ships in this repo) ──
const SLUGS = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta']
const pages = SLUGS.map((s) => ({ slug: s, path: `/vault/wiki/${s}.md` }))
const pageHashes = Object.fromEntries(SLUGS.map((s, i) => [s, `sha256-${s}-${i}`]))
const COMPONENTS = {
  module_version: '0.16.2',
  pin_vector: 'frontmatter@13,wiki-supersession@2,wiki-index@2,write-verification@3',
  convention_digests: { frontmatter: 'aaaa111122223333', 'wiki-index': 'bbbb444455556666', 'write-verification': 'cccc777788889999' },
  checks_digest: 'dddd000011112222',
}
const scanFor = (slug) => ({
  slug,
  available: true,
  title: `Page ${slug}`,
  outbound_links: [`[[${slug === 'zeta' ? 'alpha' : 'zeta'}.md|alias]]`],
  frontmatter_defect: 'none',
  frontmatter_defect_fields: [],
  frontmatter_defect_detail: '',
  category: 'Notes',
  topic_is_list: true,
  summary: `a summary for ${slug}`,
  created: '2026-01-01',
  last_updated: '2026-01-02',
  verified_by: 'owner',
  verified_at: '2026-01-02',
  review_after: '2099-01-01',
  name_callout_targets: [],
  sources_vs_prose: 'match',
  sources_vs_prose_detail: '',
  stale_unmarked: [],
  within_page_contradictions: [],
  unmarked_supersession: [],
  thin: false,
})

// ── the shipped workflow, loaded as source and run with the runtime's own shapes ──
async function runWorkflow(argsObject, { patchSource } = {}) {
  let src = fs.readFileSync(WORKFLOW, 'utf8').replace('export const meta =', 'const meta =')
  if (patchSource) src = patchSource(src)
  const dispatched = []
  const logs = []
  const agent = async (prompt, opts = {}) => {
    const label = String(opts.label || '')
    if (label.startsWith('scan:')) { const slug = label.slice(5); dispatched.push(slug); return scanFor(slug) }
    if (label === 'index-drift') return { drift: [], malformed: false, h2_headings: ['Notes'] }
    return { cross_page_contradictions: [], documented_open: [], documented_adjudicable: [], documented_undispositioned: [], entity_collisions: [] }
  }
  const parallel = async (thunks) => { const out = []; for (const t of thunks) out.push(await t()); return out }
  const fn = new AsyncFunction('args', 'agent', 'parallel', 'phase', 'log', 'budget', src)
  // THE RUNTIME CONTRACT: args arrives as a JSON-encoded STRING, never the object.
  const ret = await fn(JSON.stringify(argsObject), agent, parallel, () => {}, (m) => logs.push(String(m)), { total: 0, remaining: () => 1e9 })
  return { ret, dispatched, logs }
}

// ── the shipped writer/reader, as a subprocess. Never stubbed. ──
const cacheRead = (vaultRoot) =>
  JSON.parse(execFileSync('uv', ['run', '--quiet', SCRIPT, 'read', '--vault-root', vaultRoot], { encoding: 'utf8' }))
const cacheWrite = (vaultRoot, fingerprint, records) => {
  const p = path.join(vaultRoot, 'records.json')
  fs.writeFileSync(p, JSON.stringify(records))
  return JSON.parse(execFileSync('uv', ['run', '--quiet', SCRIPT, 'write', '--vault-root', vaultRoot, '--fingerprint', String(fingerprint || ''), '--records', p, '--today', '2026-08-27'], { encoding: 'utf8' }))
}
const sidecarPath = (vaultRoot) => path.join(vaultRoot, '_agent', 'lint-cache.json')

// ── assertions ──
let failures = 0
const check = (name, cond, detail) => {
  if (cond) console.log(`  PASS  ${name}`)
  else { failures++; console.log(`  FAIL  ${name}${detail ? ' — ' + detail : ''}`) }
}
const freshVault = (name) => { const v = path.join(ROOT, name); fs.mkdirSync(path.join(v, '_agent'), { recursive: true }); return v }

// One full SKILL-side turn: read the sidecar through the script, run the workflow,
// write the returned cache_records back through the script.
async function turn(vaultRoot, { components = COMPONENTS, patchSource, hashes = pageHashes } = {}) {
  const read = cacheRead(vaultRoot)
  const { ret, dispatched, logs } = await runWorkflow(
    { pages, indexPath: '/vault/wiki/index.md', conventionsPath: '/vault/conventions', today: '2026-08-27', pageHashes: hashes, cachedScans: read.records, rulesetComponents: components },
    { patchSource },
  )
  const write = ret.cache_records ? cacheWrite(vaultRoot, ret.cache_fingerprint, ret.cache_records) : null
  return { read, ret, write, dispatched, logs, sidecar: fs.existsSync(sidecarPath(vaultRoot)) ? fs.readFileSync(sidecarPath(vaultRoot), 'utf8') : null }
}

console.log(`temp root: ${ROOT}\n`)

// ══ V1 / check (1) + (3): cold → warm → warm, with a real writer ══
console.log('V1 — three runs: cold → warm → warm (shipped workflow + shipped lint-cache.py)')
const v1 = freshVault('v1')
const r1 = await turn(v1)
const r2 = await turn(v1)
const r3 = await turn(v1)
for (const [n, r] of [[1, r1], [2, r2], [3, r3]]) {
  console.log(`  run ${n}: status=${r.read.status} read=${r.read.count} | files_checked=${r.ret.files_checked} files_cached=${r.ret.files_cached} files_listed=${r.ret.files_listed} cache_records=${r.ret.cache_records.length} cache_records_read=${r.ret.cache_records_read} cache_rejected=${r.ret.cache_rejected} | written=${r.write.written} legacy_removed=${r.write.legacy_removed}`)
}
check('(1a) run 1 is cold: no sidecar, files_cached 0, every page dispatched', r1.read.status === 'missing' && r1.ret.files_cached === 0 && r1.dispatched.length === SLUGS.length && r1.write.written === SLUGS.length)
check('(1b) run 2 is warm: files_checked 0, files_cached N, cache_rejected 0, N rewritten', r2.ret.files_checked === 0 && r2.ret.files_cached === SLUGS.length && r2.ret.cache_rejected === 0 && r2.write.written === SLUGS.length, JSON.stringify({ checked: r2.ret.files_checked, cached: r2.ret.files_cached }))
check('(1c) run 3 ≡ run 2: same N, same keys, same scan payloads byte-for-byte (normalizeTarget idempotence)', JSON.stringify(r3.ret.cache_records) === JSON.stringify(r2.ret.cache_records) && r3.sidecar === r2.sidecar, 'sidecars differ')
check('(3a) cache_records.length === files_checked + files_cached === files_listed (run 2)', r2.ret.cache_records.length === r2.ret.files_checked + r2.ret.files_cached && r2.ret.cache_records.length === r2.ret.files_listed)
check('(3b) every record carries non-empty slug, key and scan', r2.ret.cache_records.every((c) => c && c.slug && c.key && c.scan))
check('(3c) fresh_scans is ABSENT from the return (retirement 1)', !('fresh_scans' in r2.ret))
check('(3d) run 2 records are reused-derived (0 dispatched, N records)', r2.dispatched.length === 0 && r2.ret.cache_records.length === SLUGS.length)
console.log('  one reused record, verbatim:\n    ' + JSON.stringify(r2.ret.cache_records[0]))
console.log('  sidecar after run 2 (verbatim):\n    ' + r2.sidecar.trim().slice(0, 400) + (r2.sidecar.trim().length > 400 ? '…' : ''))

// (3e) a page with no pageHashes entry yields NO record rather than one keyed on an empty digest
const v1b = freshVault('v1b')
const partialHashes = { ...pageHashes }
delete partialHashes.zeta
const rb = await turn(v1b, { hashes: partialHashes })
check('(3e) a page with no pageHashes entry produces no record', rb.ret.cache_records.length === SLUGS.length - 1 && !rb.ret.cache_records.some((c) => c.slug === 'zeta'), `got ${rb.ret.cache_records.length}`)

// ══ V2 / check (2): a record keyed under a different PAGE_SCAN is NOT reusable ══
console.log('\nV2 — negative controls')
const patchScan = (src) => {
  const before = "available: { type: 'boolean', description: 'false if the page file could not be read' },"
  const after = "available: { type: 'boolean', description: 'false if the page file could not be readX' },"
  if (!src.includes(before)) throw new Error('PAGE_SCAN patch anchor not found')
  return src.replace(before, after)
}
const v2 = freshVault('v2')
await turn(v2)                                   // seed a warm sidecar
const cScan = await turn(v2, { patchSource: patchScan })
console.log(`  different PAGE_SCAN: files_cached=${cScan.ret.files_cached} files_checked=${cScan.ret.files_checked} cache_rejected=${cScan.ret.cache_rejected} cache_records_read=${cScan.ret.cache_records_read}`)
check('(2a) a record keyed under a different PAGE_SCAN is not reusable', cScan.ret.files_cached === 0 && cScan.ret.files_checked === SLUGS.length && cScan.ret.cache_rejected === 0)
const v2b = freshVault('v2b')
await turn(v2b)
const cRule = await turn(v2b, { components: { ...COMPONENTS, checks_digest: 'eeee333344445555' } })
console.log(`  changed ruleset component: files_cached=${cRule.ret.files_cached} files_checked=${cRule.ret.files_checked}`)
check('(2b) changing only a ruleset component also yields files_cached 0', cRule.ret.files_cached === 0 && cRule.ret.files_checked === SLUGS.length)
const v2c = freshVault('v2c')
await turn(v2c)
const cNone = await turn(v2c)
console.log(`  neither changed: files_cached=${cNone.ret.files_cached}`)
check('(2c) changing neither yields full reuse', cNone.ret.files_cached === SLUGS.length)
console.log('  composed keys — warm: ' + cNone.ret.cache_records[0].key + '\n                 patched PAGE_SCAN: ' + cScan.ret.cache_records[0].key + '\n                 changed component: ' + cRule.ret.cache_records[0].key)

// ══ check (5): the fingerprint is deterministic, complete, single-homed ══
console.log('\nV2 — fingerprint determinism + completeness')
const reorder = { checks_digest: COMPONENTS.checks_digest, convention_digests: { 'write-verification': COMPONENTS.convention_digests['write-verification'], frontmatter: COMPONENTS.convention_digests.frontmatter, 'wiki-index': COMPONENTS.convention_digests['wiki-index'] }, pin_vector: COMPONENTS.pin_vector, module_version: COMPONENTS.module_version }
const a1 = await runWorkflow({ pages, indexPath: '/vault/wiki/index.md', conventionsPath: '/vault/conventions', pageHashes, rulesetComponents: COMPONENTS })
const a2 = await runWorkflow({ pages, indexPath: '/vault/wiki/index.md', conventionsPath: '/vault/conventions', pageHashes, rulesetComponents: reorder })
console.log(`  cache_fingerprint (declared order):  ${a1.ret.cache_fingerprint}\n  cache_fingerprint (shuffled order):  ${a2.ret.cache_fingerprint}`)
check('(5a) same components in a different key order compose the identical fingerprint', a1.ret.cache_fingerprint === a2.ret.cache_fingerprint && !!a1.ret.cache_fingerprint)
const missing = await runWorkflow({ pages, indexPath: '/vault/wiki/index.md', conventionsPath: '/vault/conventions', pageHashes, rulesetComponents: { module_version: '0.16.2', convention_digests: COMPONENTS.convention_digests } })
const cap = missing.ret.coverage_caps.find((c) => c.includes('rulesetComponents incomplete'))
console.log(`  missing-slot cap: ${cap}\n  missing-slot cache_fingerprint: ${JSON.stringify(missing.ret.cache_fingerprint)} files_cached: ${missing.ret.files_cached} cache_records: ${missing.ret.cache_records.length}`)
check('(5b) a components object missing a slot composes "", runs cold, and names the absent slots', missing.ret.cache_fingerprint === null && missing.ret.files_cached === 0 && !!cap && cap.includes('pin_vector') && cap.includes('checks_digest') && missing.ret.cache_records.length === 0)

// ══ V2 / check (6): a schema-mismatched sidecar is COUNTED and STATED ══
console.log('\nV2 — the field\'s own flat pre-repair sidecar shape')
const flat = SLUGS.map((s) => scanFor(s)) // flat PAGE_SCAN returns: no slug/key/scan wrapper
const v3 = freshVault('v3')
fs.writeFileSync(sidecarPath(v3), JSON.stringify({ fingerprint: 'stale', written: '2026-08-01', records: flat }))
const flatCold = await turn(v3)
console.log(`  flat sidecar, COLD branch: cache_records_read=${flatCold.ret.cache_records_read} cache_rejected=${flatCold.ret.cache_rejected} files_cached=${flatCold.ret.files_cached}`)
check('(6a) K flat records read ⇒ cache_records_read K, cache_rejected K, files_cached 0', flatCold.ret.cache_records_read === flat.length && flatCold.ret.cache_rejected === flat.length && flatCold.ret.files_cached === 0)
console.log(`  rendered per report.md:77 (cold branch): lint_cache: cold (schema-mismatched sidecar, rejected ${flatCold.ret.cache_rejected} of ${flatCold.ret.cache_records_read} records read)`)
// the WARM branch carries the pair too, including zero
const v4 = freshVault('v4')
await turn(v4)
const warm = await turn(v4)
console.log(`  warm branch, including zero: cache_records_read=${warm.ret.cache_records_read} cache_rejected=${warm.ret.cache_rejected}`)
check('(6b) the warm branch renders the pair including zero', warm.ret.cache_rejected === 0 && warm.ret.cache_records_read === SLUGS.length && 'cache_rejected' in warm.ret && 'cache_records_read' in warm.ret)
// half-and-half: some records well-formed, some flat
const v5 = freshVault('v5')
await turn(v5)
const good = JSON.parse(fs.readFileSync(sidecarPath(v5), 'utf8'))
good.records = good.records.slice(0, 3).concat(flat.slice(3))
fs.writeFileSync(sidecarPath(v5), JSON.stringify(good))
const mixed = await turn(v5)
console.log(`  mixed sidecar: cache_records_read=${mixed.ret.cache_records_read} cache_rejected=${mixed.ret.cache_rejected} files_cached=${mixed.ret.files_cached}`)
check('(6c) a partly-flat sidecar counts exactly the discarded records', mixed.ret.cache_records_read === 6 && mixed.ret.cache_rejected === 3 && mixed.ret.files_cached === 3)

// ══ the legacy .yaml is deleted by the writer, and reported ══
console.log('\nlegacy sidecar removal')
const v6 = freshVault('v6')
fs.writeFileSync(path.join(v6, '_agent', 'lint-cache.yaml'), 'fingerprint: old\nrecords: []\n')
const leg = await turn(v6)
check('(legacy) the writer deletes _agent/lint-cache.yaml and reports legacy_removed: true', leg.write.legacy_removed === true && !fs.existsSync(path.join(v6, '_agent', 'lint-cache.yaml')))

console.log(`\n${failures === 0 ? 'ALL CHECKS PASS' : failures + ' CHECK(S) FAILED'}`)
process.exit(failures === 0 ? 0 : 1)
