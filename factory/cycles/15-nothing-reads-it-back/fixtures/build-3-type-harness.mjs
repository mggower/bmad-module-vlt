#!/usr/bin/env node
// Cycle 15 build-3 — the at-rest instrument for acceptance checks (1), (2) and (3).
//
// Loads `vlt-lint-full.js` through the shared shim (`vlt-lint-full-shim.mjs` — factored out by
// build-4, the third harness, per this header's original ruling). `args` is delivered as a JSON
// STRING, exactly as the runtime does. The agent stub COUNTS invocations: a refusal case must
// show 0, not merely `files_checked: 0` — the property under test is "a wrong type never
// reaches dispatch and is never rendered as an absence".
//
// Usage:
//   node build-3-type-harness.mjs                      # check (1): the eight-case type table + the not-refused four
//   node build-3-type-harness.mjs --workflow <path>    # the same table over another workflow copy (failability: 450c886)
//   node build-3-type-harness.mjs --stubs              # check (2): link-target cases over a two-page fixture
//   node build-3-type-harness.mjs --tail               # check (3): the two decision-log instruments over the fixture + its mutated twin
// Exit 0 when every expectation in the selected mode holds, 1 otherwise.

import fs from 'node:fs'
import path from 'node:path'
import { HERE, REPO, SHIPPED, run } from './vlt-lint-full-shim.mjs'

const SIDECAR_FIXTURE = path.join(HERE, 'build-2-sidecar.json')
const TAIL_FIXTURE = path.join(HERE, 'build-3-decision-log-tail.md')

const argv = process.argv.slice(2)
const flag = (name) => argv.includes(name)
const opt = (name) => { const i = argv.indexOf(name); return i >= 0 ? argv[i + 1] : undefined }
const workflowPath = opt('--workflow') || SHIPPED

let failures = 0
const check = (label, ok, detail) => { if (!ok) failures++; console.log(`${ok ? 'PASS' : 'FAIL'}  ${label}${detail ? ` — ${detail}` : ''}`) }

// The runtime shim (compile / counting run) lives in vlt-lint-full-shim.mjs since build-4.

// ── check (3): the two decision-log instruments (--tail) ─────────────────────
// Instrument 1 — the form-agnostic heading count (`grep -c '^## '`, re-implemented).
// Instrument 2 — the matcher: S = keyed entries (`## [YYYY-MM-DD] …` + `kind:` + `ref:`);
// X = the convention's two-tier tail, which is a DATED ENTRY heading (`## YYYY-MM-DD —` or
// `## [YYYY-MM-DD]`) with kind: but no ref:, or with no kind: at all; N = E − S − X.
const tailInstruments = (text) => {
  const lines = text.split('\n')
  const E = lines.filter((l) => /^## /.test(l)).length
  let S = 0, X = 0
  for (let i = 0; i < lines.length; i++) {
    if (!/^## /.test(lines[i])) continue
    let j = i + 1
    const body = []
    while (j < lines.length && !/^## /.test(lines[j])) body.push(lines[j++])
    const dated = /^## (\[\d{4}-\d{2}-\d{2}\]|\d{4}-\d{2}-\d{2} —)/.test(lines[i])
    if (!dated) continue // a section heading, a form nobody anticipated → the remainder
    const hasKind = body.some((l) => /^- kind:/.test(l))
    const hasRef = body.some((l) => /^- ref:/.test(l))
    if (/^## \[/.test(lines[i]) && hasKind && hasRef) S++
    else X++
  }
  return { E, S, X, N: E - S - X }
}

if (flag('--tail')) {
  const text = fs.readFileSync(TAIL_FIXTURE, 'utf8')
  const base = tailInstruments(text)
  const twin = tailInstruments(text + '\n## Notes\n\n(a section heading nobody anticipated)\n')
  console.log(`fixture:      ${JSON.stringify(base)}`)
  console.log(`mutated twin: ${JSON.stringify(twin)}`)
  check('fixture E 16 (heading count) / S 3 / X 13 / N 0', base.E === 16 && base.S === 3 && base.X === 13 && base.N === 0)
  check('mutated twin E 17 / S 3 / X 13 / N 1 — the remainder rendered, not absorbed', twin.E === 17 && twin.S === 3 && twin.X === 13 && twin.N === 1)
  check('a same-matcher total (S + X) reads back nothing on the twin', twin.S + twin.X === 16 && twin.E !== twin.S + twin.X)
  console.log(`\n${failures ? `${failures} expectation(s) FAILED` : 'all expectations hold'}`)
  process.exit(failures ? 1 : 0)
}

// ── fixture + baseline inputs (from build-2's harness) ───────────────────────
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
  overlaysPath: '/vault/_agent/conventions/overlays',
  overlayNames: [],
  today: '2026-09-02',
  pageHashes: Object.fromEntries(records.map((r) => [r.slug, hashOf(r.slug)])),
  // Build-4's two REQUIRED byte-fact args, composed from the fixture records (a record's
  // `links` where the case supplies one — the --stubs mode — else the sidecar's pre-build-4
  // `scan.outbound_links`, equal to what the scanner returned, so prior expectations hold).
  pageLinks: Object.fromEntries(records.map((r) => [r.slug, r.links || r.scan.outbound_links || []])),
  summaryLengths: Object.fromEntries(records.map((r) => [r.slug, (r.scan.summary || '').length])),
  cachedScans,
  rulesetComponents: { convention_digests: { ...DIGEST } },
})
const src = fs.readFileSync(workflowPath, 'utf8')

// The gen pass (build-2's): under baseline inputs and an empty cache, an agent stub returning
// each record's own scan makes the workflow compose the keys it would have written.
async function rekey(records) {
  const bySlug = new Map(records.map((r) => [r.slug, r.scan]))
  const stub = async (_prompt, o) => (o && typeof o.label === 'string' && o.label.startsWith('scan:')) ? structuredClone(bySlug.get(o.label.slice(5))) : null
  const { result } = await run(src, baselineArgs(records, []), stub)
  if (!Array.isArray(result.cache_records) || result.cache_records.length !== records.length) {
    throw new Error(`gen pass did not return ${records.length} cache_records: ${JSON.stringify(result).slice(0, 300)}`)
  }
  const keyOf = new Map(result.cache_records.map((c) => [c.slug, c.key]))
  return records.map((r) => ({ slug: r.slug, key: keyOf.get(r.slug), scan: r.scan }))
}

// ── check (2): the link-target cases (--stubs) ───────────────────────────────
if (flag('--stubs')) {
  const template = allRecords[0].scan
  // Since build-4 the link set is passed as `pageLinks` (the SKILL's byte-fact), not returned by
  // the scanner — the planted scans carry no outbound_links at all.
  const scanFor = (slug) => { const s = { ...structuredClone(template), slug, title: slug, name_callout_targets: [] }; delete s.outbound_links; return s }
  const pages = [{ slug: 'a', links: ['birria'], scan: scanFor('a') }, { slug: 'b', links: [], scan: scanFor('b') }]
  const bySlug = new Map(pages.map((p) => [p.slug, p.scan]))
  const stub = async (_prompt, o) => (o && typeof o.label === 'string' && o.label.startsWith('scan:')) ? structuredClone(bySlug.get(o.label.slice(5))) : null
  const withStubs = (stubSlugs) => ({ ...baselineArgs(pages, []), stubSlugs })
  const cases = [
    { name: 'the three registered slugs passed → no missing target', stubSlugs: ['birria', 'jesse-minter', 'nfl-draft-safety-archetypes'], expectMissing: [] },
    { name: '[] passed (the A15-2 observable) → a registered stub reported missing', stubSlugs: [], expectMissing: ['a → birria'] },
    { name: "'birria' (a string) passed → refused pre-dispatch", stubSlugs: 'birria', refused: true },
  ]
  for (const c of cases) {
    const o = await run(src, withStubs(c.stubSlugs), stub)
    const r = o.result
    if (c.refused) {
      console.log(`status=${r.status} agents=${o.invocations} reason=${JSON.stringify(r.reason)}`)
      check(c.name, r.status === 'failed' && /stubSlugs/.test(r.reason) && /got string/.test(r.reason) && o.invocations === 0, `status=${r.status} agents=${o.invocations}`)
    } else {
      const missing = r.fix_now ? r.fix_now.missing_targets : undefined
      console.log(`missing_targets=${JSON.stringify(missing)} agents=${o.invocations}`)
      check(c.name, JSON.stringify(missing) === JSON.stringify(c.expectMissing), `missing_targets=${JSON.stringify(missing)}`)
    }
  }
  console.log(`\n${failures ? `${failures} expectation(s) FAILED` : 'all expectations hold'}`)
  process.exit(failures ? 1 : 0)
}

// ── check (1): the type table ────────────────────────────────────────────────
const two = allRecords.slice(0, 2)
const keyed = await rekey(two)
console.log(`workflow: ${path.relative(REPO, workflowPath)}`)

// The case-table stub returns each page's own scan for a `scan:` dispatch (build-2's gen-pass
// stub) — so a COLD case runs to a findings report with `files_cached: 0` rather than tripping
// the near-total-shortfall guard, and the count of invocations is the honest dispatch measure.
const scanBySlug = new Map(two.map((r) => [r.slug, r.scan]))
const scanStub = async (_prompt, o) => (o && typeof o.label === 'string' && o.label.startsWith('scan:')) ? structuredClone(scanBySlug.get(o.label.slice(5))) : null
const base = () => baselineArgs(two, structuredClone(keyed))
const patchCD = (fn) => { const a = base(); fn(a.rulesetComponents.convention_digests, a); return a }
const cases = [
  { id: 'a', name: 'convention_digests: [] (an array where a map is required)', args: patchCD((_, a) => { a.rulesetComponents.convention_digests = [] }), refused: { slot: 'convention_digests', got: 'array' } },
  { id: 'b', name: 'convention_digests.frontmatter: 42', args: patchCD((cd) => { cd.frontmatter = 42 }), refused: { slot: 'convention_digests[frontmatter]', got: 'number' } },
  { id: 'c', name: 'convention_digests: {}', args: patchCD((_, a) => { a.rulesetComponents.convention_digests = {} }), cap: 'empty [convention_digests]' },
  { id: 'd', name: 'write-verification key absent', args: patchCD((cd) => { delete cd['write-verification'] }), cap: 'absent [convention_digests[write-verification]]' },
  { id: 'e', name: "convention_digests.frontmatter: ''", args: patchCD((cd) => { cd.frontmatter = '' }), cap: 'empty [convention_digests[frontmatter]]' },
  { id: 'f', name: "stubSlugs: 'birria'", args: (() => { const a = base(); a.stubSlugs = 'birria'; return a })(), refused: { slot: 'stubSlugs', got: 'string' } },
  { id: 'g', name: 'rulesetComponents: []', args: (() => { const a = base(); a.rulesetComponents = []; return a })(), refused: { slot: 'rulesetComponents', got: 'array' } },
  { id: 'h', name: 'baseline', args: base(), warm: true },
]

console.log('\ncase  status    files_cached  agents  scan-row-dispatched  reason / cap')
for (const c of cases) {
  const o = await run(src, c.args, scanStub)
  const r = o.result
  const scanRow = r.cost_accounting && r.cost_accounting.phases.find((p) => p.phase === 'Scan pages')
  const dispatched = scanRow ? scanRow.agents_dispatched : '(no row)'
  const caps = r.coverage_caps || []
  const coldCaps = caps.filter((m) => m.includes('findings cache cold'))
  const detail = r.status === 'failed' ? r.reason : (coldCaps.join(' | ') || '(no cold cap)')
  console.log(`(${c.id})   ${String(r.status || 'report').padEnd(9)} ${String(r.files_cached).padEnd(13)} ${String(o.invocations).padEnd(7)} ${String(dispatched).padEnd(20)} ${detail}   [${c.name}]`)
  if (c.refused) {
    check(`(${c.id}) refused: status 'failed', reason names ${c.refused.slot} + ${c.refused.got}`, r.status === 'failed' && typeof r.reason === 'string' && r.reason.includes(`slot rendered with the wrong type: ${c.refused.slot} (got ${c.refused.got}`), `status=${r.status} reason=${JSON.stringify(r.reason)}`)
    check(`(${c.id}) 0 agent invocations (never reached dispatch)`, o.invocations === 0, `agents=${o.invocations}`)
    check(`(${c.id}) cost_accounting scan row 0 dispatched`, dispatched === 0, `dispatched=${dispatched}`)
    check(`(${c.id}) never rendered as an absence (no 'absent'/'empty' cap naming the slot)`, !coldCaps.some((m) => m.includes(c.refused.slot)), JSON.stringify(coldCaps))
    check(`(${c.id}) next: is directed (names step 2 / Missing targets)`, typeof r.next === 'string' && r.next.includes('step 2') && r.next.includes('Missing targets'), JSON.stringify(r.next))
    check(`(${c.id}) failed-run shape carries the cache reader's counts`, r.cache_records_read === 2 && r.cache_rejected === 0 && r.files_checked === 0 && r.files_cached === 0, JSON.stringify({ read: r.cache_records_read, rejected: r.cache_rejected }))
  } else if (c.cap) {
    check(`(${c.id}) findings report, files_cached 0`, r.status === undefined && r.files_cached === 0, `status=${r.status} files_cached=${r.files_cached}`)
    check(`(${c.id}) cap reads '${c.cap}'`, coldCaps.some((m) => m.includes(c.cap)), JSON.stringify(coldCaps))
  } else {
    check(`(${c.id}) baseline: 2 cached, no cold cap`, r.files_cached === 2 && coldCaps.length === 0, `files_cached=${r.files_cached} caps=${JSON.stringify(coldCaps)}`)
  }
}

// Verification 6 — the not-refused four (informational, the on-record gap for the candidate filing):
// a wrong-typed `pageHashes` still coerces to {} and runs a stated cold sweep, no refusal.
{
  const a = base(); a.pageHashes = []
  const o = await run(src, a, scanStub)
  console.log(`\ninformational — pageHashes: [] (not a D2 slot, NOT refused): status=${o.result.status || 'report'} files_cached=${o.result.files_cached} agents=${o.invocations}`)
}

console.log(`\n${failures ? `${failures} expectation(s) FAILED` : 'all expectations hold'}`)
process.exit(failures ? 1 : 0)
