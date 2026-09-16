#!/usr/bin/env node
// Cycle 16 build-1 — the at-rest instrument for acceptance check (2) Census (brief F4 / F5 / F6;
// §Verification 2 and 7). The build-4-return-harness.mjs shape, importing Cycle 15's shared shim.
//
// Phase 1 runs `skills/vlt-lint/scripts/lint-page-facts.py --census` FOR REAL over `build-1-wiki/`
// (real files on disk; `uv run --quiet`, falling back to `python3`) and deep-compares its JSON and its
// `--census-line` to the HAND-WRITTEN oracle `build-1-expected-census.json` (written before the script
// ran). It then runs `--pages` over the same 29 pages and asserts the per-page `bareSources` /
// `sourcesUnparsed` are the same values — ONE function, both callers (disposition 5).
//
// Phase 2 loads the shipped workflow through the shim with a COUNTING agent stub whose `scan:` returns
// are PLANTED frontmatter verdicts, and asserts `malformed_frontmatter` per the brief's case table:
// the bare-path complaint (the filing's own fragment, on dutch-oven-braising) is REFUSED only where the
// page's byte fact says the form is there; every other shape REPORTS; an absent `bareSources` reports
// and names itself on `coverage_caps`; a wrong-typed map/entry is refused pre-dispatch by name.
// `--workflow <path>` runs the same table over another copy — the failability proof against v0.18.0,
// where the planted complaints reach the slot and no wrong type is refused.
//
// Phase 3 runs the persist gate over a full-mode report carrying the oracle line: `ok`; the same line
// off by one → `failed`, reason `bare_path_sources: rendered line does not match the recount`; scoped
// mode with the key absent → `ok`; full mode without `--wiki-dir` → exit 2 (§Verification 7).
//
// Usage:
//   node build-1-census-harness.mjs                    # all three phases on the shipped workflow
//   node build-1-census-harness.mjs --workflow <path>  # phase 2 over another workflow copy
// Exit 0 when every expectation holds, 1 otherwise.

import fs from 'node:fs'
import os from 'node:os'
import path from 'node:path'
import { spawnSync } from 'node:child_process'
import { HERE as C15, REPO, SHIPPED, run } from '../../15-nothing-reads-it-back/fixtures/vlt-lint-full-shim.mjs'

const HERE = path.dirname(new URL(import.meta.url).pathname)
const WIKI = path.join(HERE, 'build-1-wiki')
const INDEX = path.join(WIKI, 'index.md')
const ORACLE = path.join(HERE, 'build-1-expected-census.json')
const SCRIPT = path.join(REPO, 'skills', 'vlt-lint', 'scripts', 'lint-page-facts.py')
const GATE = path.join(REPO, 'skills', 'vlt-lint', 'scripts', 'lint-report-check.py')
const PARA = path.join(C15, 'build-5-para')
const OK_REPORT = path.join(C15, 'build-5-report-ok.yaml')

const argv = process.argv.slice(2)
const opt = (name) => { const i = argv.indexOf(name); return i >= 0 ? argv[i + 1] : undefined }
const workflowPath = opt('--workflow') || SHIPPED
const src = fs.readFileSync(workflowPath, 'utf8')

let failures = 0
const check = (label, ok, detail) => { if (!ok) failures++; console.log(`${ok ? 'PASS' : 'FAIL'}  ${label}${detail ? ` — ${detail}` : ''}`) }
const canon = (v) => Array.isArray(v) ? v.map(canon) : (v && typeof v === 'object') ? Object.fromEntries(Object.keys(v).sort().map((k) => [k, canon(v[k])])) : v
const same = (a, b) => JSON.stringify(canon(a)) === JSON.stringify(canon(b))

function py(args, input) {
  const attempts = [['uv', ['run', '--quiet', ...args]], ['python3', args]]
  for (const [cmd, a] of attempts) {
    const r = spawnSync(cmd, a, { input, encoding: 'utf8' })
    if (r.error) continue
    return { via: cmd, status: r.status, stdout: r.stdout, stderr: r.stderr }
  }
  throw new Error(`could not run ${args[0]} via uv or python3`)
}

// ── phase 1: the census, for real, against the oracle ────────────────────────
const oracle = JSON.parse(fs.readFileSync(ORACLE, 'utf8'))
delete oracle._comment
const censusRun = py([SCRIPT, '--census', WIKI, '--census-exclude', INDEX])
const censusJson = JSON.parse(censusRun.stdout)
const lineRun = py([SCRIPT, '--census', WIKI, '--census-exclude', INDEX, '--census-line'])
console.log(`phase 1 — lint-page-facts.py --census (via ${censusRun.via}) over ${path.relative(REPO, WIKI)} vs the hand-written oracle`)
const { line: oracleLine, ...oracleJson } = oracle
check('census JSON deep-equals the oracle (bareSources, sourcesUnparsed, counts)', same(censusJson, oracleJson), same(censusJson, oracleJson) ? '' : `\n got ${JSON.stringify(canon(censusJson))}\n exp ${JSON.stringify(canon(oracleJson))}`)
check('--census-line equals the oracle line', lineRun.stdout.trim() === oracleLine, lineRun.stdout.trim())
const pages = Object.keys(oracle.bareSources).concat(oracle.sourcesUnparsed).sort().map((slug) => ({ slug, path: path.join(WIKI, `${slug}.md`) }))
check('the page list is the 29 walked pages (index excluded)', pages.length === 29 && !pages.some((p) => p.slug === 'index'), String(pages.length))
const facts = JSON.parse(py([SCRIPT, '--pages', '-'], JSON.stringify(pages)).stdout)
check('--pages bareSources / sourcesUnparsed equal the census per page — one function, both callers', same(facts.bareSources, oracle.bareSources) && same(facts.sourcesUnparsed, oracle.sourcesUnparsed), JSON.stringify(facts.sourcesUnparsed))
check('--pages keeps pageLinks / summaryLengths / unreadable / pages', ['pageLinks', 'summaryLengths', 'unreadable', 'pages'].every((k) => k in facts) && facts.pages === 29 && facts.unreadable.length === 0)
const bad = py([SCRIPT, '--census', path.join(WIKI, 'no-such-dir')])
check('--census over a missing directory exits 2 (never reads as zero)', bad.status === 2, `exit ${bad.status}`)
if (failures) { console.log('\nphase 1 FAILED — the reduce cases are not run over a script that disagrees with the oracle'); process.exit(1) }

// ── phase 2: the workflow with planted verdicts ───────────────────────────────
const hashOf = (slug) => `sha256-${slug}-fixture-bytes`.padEnd(64, '0')
const DIGEST = { frontmatter: '1111111111111111', 'wiki-supersession': '2222222222222222', 'write-verification': '3333333333333333' }
const baseArgs = (over = {}) => ({
  pages,
  indexPath: '/vault/resources/wiki/index.md',
  conventionsPath: '/vault/_agent/conventions',
  overlaysPath: '/vault/_agent/conventions/overlays',
  overlayNames: [],
  crossLayerSlugs: [],
  stubSlugs: [],
  today: '2026-09-16',
  pageHashes: Object.fromEntries(pages.map((p) => [p.slug, hashOf(p.slug)])),
  cachedScans: [],
  rulesetComponents: { convention_digests: { ...DIGEST } },
  pageLinks: structuredClone(facts.pageLinks),
  summaryLengths: structuredClone(facts.summaryLengths),
  bareSources: structuredClone(facts.bareSources),
  ...over,
})
const record = (slug, over = {}) => ({
  slug, available: true, title: slug, created: '2026-08-01', last_updated: '2026-08-26', verified_by: 'vlt-lint', verified_at: '2026-08-26',
  review_after: '', frontmatter_defect: 'none', category: 'Fixture', topic_is_list: true, summary: 'a short summary', frontmatter_defect_fields: [],
  frontmatter_defect_detail: '', sources_vs_prose: 'match', sources_vs_prose_detail: '', stale_unmarked: [], within_page_contradictions: [],
  unmarked_supersession: [], thin: false, name_callout_targets: [], ...over,
})
// The preserved specimen: the filing's report fragment, verbatim (A16-2, bytes preserved for 1).
const FRAGMENT = 'YAML rule 1 & rule 4 violation: sources entry `_agent/research/2026-05-11-193624-dutch-oven-barbacoa-chuck-roast.md` must be double-quoted wikilink without .md: `"[[_agent/research/2026-05-11-193624-dutch-oven-barbacoa-chuck-roast]]"`'
const plant = (over) => { const m = new Map(pages.map((p) => [p.slug, record(p.slug)])); for (const [slug, o] of Object.entries(over)) m.set(slug, record(slug, o)); return m }
const stubFor = (bySlug) => async (_prompt, o) => (o && typeof o.label === 'string' && o.label.startsWith('scan:')) ? structuredClone(bySlug.get(o.label.slice(5))) : null
const CASES = {
  'dutch-oven-braising': { frontmatter_defect: 'unclassified', frontmatter_defect_fields: ['sources'], frontmatter_defect_detail: FRAGMENT },   // bare form on a manifest page → REFUSED
  'scalar-sources': { frontmatter_defect: 'unclassified', frontmatter_defect_fields: ['sources'], frontmatter_defect_detail: 'sources: is a scalar, not a list' },   // no map entry → REPORTS
  'barbacoa': { frontmatter_defect: 'missing_required', frontmatter_defect_fields: ['sources'], frontmatter_defect_detail: 'sources: absent' },   // wrong kind → REPORTS
  'seattle-seahawks': { frontmatter_defect: 'unclassified', frontmatter_defect_fields: ['sources', 'title'], frontmatter_defect_detail: 'two fields' },   // not exactly [sources] → REPORTS
  'myles-garrett': { frontmatter_defect: 'malformed_block', frontmatter_defect_fields: [], frontmatter_defect_detail: 'block unparseable' },   // never refused → REPORTS
  'protein-intake': { frontmatter_defect: 'unclassified', frontmatter_defect_fields: [], frontmatter_defect_detail: 'sources entry must be a quoted wikilink' },   // wording never enters → REPORTS
  'creatine-monohydrate': { frontmatter_defect: 'missing_required', frontmatter_defect_fields: ['verified_by', 'verified_at'], frontmatter_defect_detail: '' },   // disposition 1 still refuses → control
}
const slotOf = (r) => ((r.flag_for_human || {}).malformed_frontmatter || [])
const has = (list, slug) => list.some((m) => m.startsWith(`${slug}:`))

console.log(`\nphase 2 — workflow: ${path.relative(REPO, workflowPath)}`)
const A = await run(src, baseArgs(), stubFor(plant(CASES)))
const rA = A.result
if (rA.error || rA.status === 'failed') console.log(`run A did not complete: ${rA.error || rA.reason}`)
const mfA = slotOf(rA)
console.log(`A: malformed_frontmatter=${JSON.stringify(mfA)}\n   caps=${JSON.stringify(rA.coverage_caps)}`)
check('A (a) dutch-oven-braising unclassified/[sources] with the filing fragment → REFUSED (bareSources[slug] = 1)', !has(mfA, 'dutch-oven-braising'))
check('A (b) scalar-sources unclassified/[sources] → REPORTS (no byte fact — absent from the map)', has(mfA, 'scalar-sources'))
check('A (c) barbacoa missing_required/[sources] → REPORTS (disposition 3 keys on unclassified only)', has(mfA, 'barbacoa'))
check('A (d) seattle-seahawks unclassified/[sources, title] → REPORTS (field list not exactly [sources])', has(mfA, 'seattle-seahawks'))
check('A (e) myles-garrett malformed_block → REPORTS (never refused)', has(mfA, 'myles-garrett'))
check('A (f) protein-intake unclassified/[] with sources-naming prose → REPORTS (wording never enters)', has(mfA, 'protein-intake'))
check('A (g) control: creatine-monohydrate missing_required/[verified_by, verified_at] → REFUSED by disposition 1 (unchanged)', !has(mfA, 'creatine-monohydrate'))
check('A (h) exactly the five reporting pages, nothing else', mfA.length === 5, String(mfA.length))
check('A (i) no bareSources cap when the map is present', !(rA.coverage_caps || []).some((c) => c.includes('bareSources absent')))
check('A (j) the refused page is still cached — refusal drops a duplicate, not the record', (rA.cache_records || []).some((c) => c.slug === 'dutch-oven-braising'))

const B = await run(src, baseArgs({ bareSources: undefined }), stubFor(plant(CASES)))
const rB = B.result
const mfB = slotOf(rB)
console.log(`B: malformed_frontmatter=${JSON.stringify(mfB)}\n   caps=${JSON.stringify(rB.coverage_caps)}`)
check('B (a) bareSources ABSENT → dutch-oven-braising REPORTS (the refusal is inert)', has(mfB, 'dutch-oven-braising'))
check('B (b) …and coverage_caps names it: "bareSources absent — bare-path sources: complaints report unrefused"', (rB.coverage_caps || []).some((c) => c.startsWith('bareSources absent — bare-path sources: complaints report unrefused')), JSON.stringify(rB.coverage_caps))
check('B (c) the run still completed (absent is degraded, never refused)', B.invocations > 0 && !rB.error && rB.status !== 'failed', `invocations=${B.invocations}`)

const E = await run(src, baseArgs({ bareSources: {} }), stubFor(plant(CASES)))
const mfE = slotOf(E.result)
check('E (a) bareSources PRESENT but empty {} → dutch-oven-braising REPORTS (no entry for the page), and no absent-cap', has(mfE, 'dutch-oven-braising') && !(E.result.coverage_caps || []).some((c) => c.includes('bareSources absent')), JSON.stringify(E.result.coverage_caps))

const C = await run(src, baseArgs({ bareSources: 'nope' }), stubFor(plant(CASES)))
check('C (a) bareSources a string → refused pre-dispatch: status failed, reason names bareSources, 0 agent invocations', C.result.status === 'failed' && /slot rendered with the wrong type: bareSources \(got string, expected plain object\)/.test(C.result.reason || '') && C.invocations === 0, `${C.result.status} ${C.result.reason || ''} invocations=${C.invocations}`)
const D = await run(src, baseArgs({ bareSources: { ...facts.bareSources, barbacoa: 'one' } }), stubFor(plant(CASES)))
check('D (a) bareSources[barbacoa] a string → refused pre-dispatch BY NAME (bareSources[barbacoa]), 0 invocations', D.result.status === 'failed' && /bareSources\[barbacoa\] \(got string, expected integer\)/.test(D.result.reason || '') && D.invocations === 0, `${D.result.status} ${D.result.reason || ''} invocations=${D.invocations}`)
const F = await run(src, baseArgs({ bareSources: { ...facts.bareSources, 'not-a-listed-page': 'x' } }), stubFor(plant(CASES)))
check('F (a) a wrong-typed entry for an UNLISTED slug is not refused (the guard walks pages, not the map)', F.result.status !== 'failed' && !F.result.error, F.result.reason || '')

// ── phase 3: the persist gate recounts the line (§Verification 7) ─────────────
if (workflowPath === SHIPPED) {
  console.log('\nphase 3 — lint-report-check.py over a report carrying the oracle line')
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'build-1-census-'))
  const ok = fs.readFileSync(OK_REPORT, 'utf8')
  const CENSUS_ANCHOR = '  attestation_census: {pages_total: 1, fresh: 0, stale: 0, unattested_pre_adoption: 1}\n'
  if (!ok.includes(CENSUS_ANCHOR)) throw new Error('build-5-report-ok.yaml anchor moved — fix the harness')
  // build-5-report-ok.yaml already carries its own bare_path_sources: line (F11) — replace it with the oracle's
  const stripped = ok.split('\n').filter((l) => !l.startsWith('  bare_path_sources:')).join('\n')
  const withLine = (line) => stripped.replace(CENSUS_ANCHOR, CENSUS_ANCHOR + `  bare_path_sources: "${line}"\n`)
  const DIRS = ['--dir', path.join(PARA, 'projects'), '--dir', path.join(PARA, 'areas'), '--dir', path.join(PARA, 'resources'), '--exclude', path.join(PARA, 'resources', 'wiki'), '--root', PARA]
  const gate = (text, mode, extra) => {
    const p = path.join(tmp, `${mode}-${Math.random().toString(16).slice(2)}.yaml`)
    fs.writeFileSync(p, text)
    const r = py([GATE, 'check', '--report', p, '--mode', mode, ...DIRS, ...extra])
    let out = {}
    try { out = JSON.parse(r.stdout) } catch { out = { stderr: r.stderr.trim() } }
    return { code: r.status, out }
  }
  const WD = ['--wiki-dir', WIKI, '--wiki-exclude', INDEX]
  let g = gate(withLine(oracleLine), 'full', WD)
  check('3 (a) full mode, oracle line, --wiki-dir build-1-wiki → ok, census {N 57, P 23, M 29}', g.code === 0 && g.out.status === 'ok' && same(g.out.census, { N: 57, P: 23, M: 29 }), JSON.stringify(g.out))
  g = gate(withLine(oracleLine.replace('57 entries', '56 entries')), 'full', WD)
  check('3 (b) 57 → 56 → failed, reason exactly "bare_path_sources: rendered line does not match the recount"', g.code === 1 && g.out.reason === 'bare_path_sources: rendered line does not match the recount', JSON.stringify(g.out.reason))
  g = gate(stripped.replace('mode: "full"', 'mode: "scoped"'), 'scoped', [])
  check('3 (c) scoped mode, key absent, no --wiki-dir → ok', g.code === 0 && g.out.status === 'ok' && g.out.census === null, JSON.stringify(g.out))
  g = gate(withLine('anything — scoped composes no census').replace('mode: "full"', 'mode: "scoped"'), 'scoped', [])
  check('3 (d) scoped mode, key present, no --wiki-dir → ok (ignored)', g.code === 0 && g.out.status === 'ok', JSON.stringify(g.out))
  g = gate(withLine(oracleLine), 'full', [])
  check('3 (e) full mode without --wiki-dir → usage error, exit 2', g.code === 2, `exit ${g.code} ${g.out.stderr || ''}`)
  g = gate(stripped, 'full', WD)
  check('3 (f) full mode, key absent → key missing: flag_for_human.bare_path_sources', g.code === 1 && /key missing: flag_for_human\.bare_path_sources/.test(g.out.reason || ''), JSON.stringify(g.out.reason))
  fs.rmSync(tmp, { recursive: true, force: true })
}

console.log(`\n${failures ? `${failures} expectation(s) FAILED` : 'all expectations hold'}`)
process.exit(failures ? 1 : 0)
