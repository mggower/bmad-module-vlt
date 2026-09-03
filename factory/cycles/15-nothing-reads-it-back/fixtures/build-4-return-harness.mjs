#!/usr/bin/env node
// Cycle 15 build-4 — the at-rest instrument for acceptance checks (1), (2) and (3).
//
// Phase 1 runs `skills/vlt-lint/scripts/lint-page-facts.py` FOR REAL over `build-4-wiki/`
// (real files on disk — the script must read bytes; `uv run --quiet`, falling back to
// `python3`) and deep-compares its output to the HAND-WRITTEN oracle
// `build-4-expected-facts.json`. A script defect fails here before any reduce case runs — the
// oracle is what makes the script's check failable (check (1)'s adversary: a shared extraction
// bug in script and planted return would otherwise agree).
//
// Phase 2 loads the workflow through the shared shim with a COUNTING agent stub whose `scan:`
// returns are PLANTED RECORDS AT ODDS WITH THE BYTES (a dropped link, a stripped `#`, a
// substituted noun, a paraphrased summary, a fabricated callout target) and asserts the report
// follows the bytes. `--workflow <path>` runs the same table over another copy — the
// failability proof against `7222cd2`, where the planted returns are consumed.
//
// Usage:
//   node build-4-return-harness.mjs                    # phase 1 + the case table on the shipped workflow
//   node build-4-return-harness.mjs --workflow <path>  # the same table over another workflow copy
//   node build-4-return-harness.mjs --fingerprint      # print scanFingerprint only (Verification 2)
// Exit 0 when every expectation holds, 1 otherwise.

import fs from 'node:fs'
import path from 'node:path'
import { spawnSync } from 'node:child_process'
import { HERE, REPO, SHIPPED, run } from './vlt-lint-full-shim.mjs'

const WIKI = path.join(HERE, 'build-4-wiki')
const ORACLE = path.join(HERE, 'build-4-expected-facts.json')
const SCRIPT = path.join(REPO, 'skills', 'vlt-lint', 'scripts', 'lint-page-facts.py')

const argv = process.argv.slice(2)
const flag = (name) => argv.includes(name)
const opt = (name) => { const i = argv.indexOf(name); return i >= 0 ? argv[i + 1] : undefined }
const workflowPath = opt('--workflow') || SHIPPED
const src = fs.readFileSync(workflowPath, 'utf8')

let failures = 0
const check = (label, ok, detail) => { if (!ok) failures++; console.log(`${ok ? 'PASS' : 'FAIL'}  ${label}${detail ? ` — ${detail}` : ''}`) }

// The page list in the brief's table order (the SKILL-supplied slugs the maps are keyed by).
const ORDER = ['fantasy-football-evaluation', 'fantasy-platform-read-access', 'chicken-soup', 'katsuo-dashi', 'calf-strain',
  'seattle-seahawks', 'l-theanine', 'barbacoa', 'parallel-walk-introduction', 'lonely-page', 'code-fence-page']
const pages = ORDER.map((slug) => ({ slug, path: path.join(WIKI, `${slug}.md`) }))

// ── phase 1: the script, for real, against the oracle ────────────────────────
function runScript() {
  const input = JSON.stringify(pages)
  const attempts = [['uv', ['run', '--quiet', SCRIPT, '--pages', '-']], ['python3', [SCRIPT, '--pages', '-']]]
  for (const [cmd, args] of attempts) {
    const r = spawnSync(cmd, args, { input, encoding: 'utf8' })
    if (r.error || r.status !== 0) continue
    return { via: cmd, out: JSON.parse(r.stdout) }
  }
  throw new Error('lint-page-facts.py could not be run via uv or python3')
}
const canon = (v) => Array.isArray(v) ? v.map(canon) : (v && typeof v === 'object') ? Object.fromEntries(Object.keys(v).sort().map((k) => [k, canon(v[k])])) : v
const oracle = JSON.parse(fs.readFileSync(ORACLE, 'utf8'))
delete oracle._comment
const { via, out: facts } = runScript()
const phase1 = JSON.stringify(canon(facts)) === JSON.stringify(canon(oracle))
console.log(`phase 1 — lint-page-facts.py (via ${via}) over ${path.relative(REPO, WIKI)} vs the hand-written oracle`)
check('script output deep-equals build-4-expected-facts.json', phase1, phase1 ? '' : `diff:\n got ${JSON.stringify(canon(facts))}\n exp ${JSON.stringify(canon(oracle))}`)
if (!phase1) { console.log('\nphase 1 FAILED — the reduce cases are not run over a script that disagrees with the bytes'); process.exit(1) }

// ── phase 2: the workflow with planted returns at odds with the bytes ────────
const hashOf = (slug) => `sha256-${slug}-baseline-bytes`.padEnd(64, '0')
const DIGEST = { frontmatter: '1111111111111111', 'wiki-supersession': '2222222222222222', 'write-verification': '3333333333333333' }
const baseArgs = (over = {}) => ({
  pages,
  indexPath: '/vault/wiki/index.md',
  conventionsPath: '/vault/_agent/conventions',
  overlaysPath: '/vault/_agent/conventions/overlays',
  overlayNames: [],
  // Both basenames of seattle-seahawks's cross-layer targets (the frontmatter wikilink and the body link).
  crossLayerSlugs: ['2026-07-07-espn-top-10-cornerbacks-2026-execs-coaches-scouts', '2026-07-26-112444-espn-top-10-cornerbacks-2026'],
  stubSlugs: [],
  today: '2026-09-02',
  pageHashes: Object.fromEntries(pages.map((p) => [p.slug, hashOf(p.slug)])),
  cachedScans: [],
  rulesetComponents: { convention_digests: { ...DIGEST } },
  pageLinks: structuredClone(facts.pageLinks),
  summaryLengths: structuredClone(facts.summaryLengths),
  ...over,
})

const record = (slug, over = {}) => ({
  slug, available: true, title: slug, created: '2026-08-01', last_updated: '2026-08-01', verified_by: 'vlt-lint', verified_at: '2026-08-01',
  review_after: '', frontmatter_defect: 'none', category: 'Misc', topic_is_list: true, summary: 'a short summary', frontmatter_defect_fields: [],
  frontmatter_defect_detail: '', sources_vs_prose: 'match', sources_vs_prose_detail: '', stale_unmarked: [], within_page_contradictions: [],
  unmarked_supersession: [], thin: false, name_callout_targets: [], outbound_links: facts.pageLinks[slug], ...over,
})
const LT_PARAPHRASE = 'L-theanine is an amino acid found in green tea that promotes calm alertness without sedation and, when paired with caffeine, smooths the stimulant edge; a staple.'
const BB_VERBATIM = 'Barbacoa is a slow braise of beef cheek or chuck in dried-chile adobo — cooked low until it shreds, then served on warm tortillas with onion, cilantro and limes'
if (LT_PARAPHRASE.length !== 162 || BB_VERBATIM.length !== 160) throw new Error('planted summary lengths drifted — fix the harness')
// The planted returns: every mutation the four filings observed, at odds with the bytes on disk.
const planted = new Map(pages.map((p) => [p.slug, record(p.slug)]))
planted.set('fantasy-football-evaluation', record('fantasy-football-evaluation', { outbound_links: ['calf-strain', 'chicken-soup'] }))               // A15-1: [[fantasy-platform-read-access]] dropped
planted.set('chicken-soup', record('chicken-soup', { outbound_links: [], name_callout_targets: [{ target: 'katsuo-dashi', name: 'Katsuo' }] }))       // A15-1: [[katsuo-dashi]] dropped; a genuine callout
planted.set('seattle-seahawks', record('seattle-seahawks', {
  outbound_links: ['sources/articles/2026-07-07-espn-top-10-cornerbacks-2026-execs-coaches-scouts', '_agent/research/2026-07-26-112444-espn-top-10-cornerboxes-2026'], // A15-4: the substituted noun
  name_callout_targets: [{ target: 'new-england-patriots', name: 'Patriots' }],                                                                    // check (3): a fabricated seed
}))
planted.set('calf-strain', record('calf-strain', { outbound_links: ['early loading phase (≈ days 3–7)', 'Red Flags'] }))                             // A15-3: the stripped `#`
planted.set('l-theanine', record('l-theanine', { summary: LT_PARAPHRASE, frontmatter_defect: 'unclassified', frontmatter_defect_detail: 'summary exceeds 160 characters (161)' })) // A15-5 refuted #2, both routes
planted.set('barbacoa', record('barbacoa', { summary: BB_VERBATIM }))                                                                                // A15-5 refuted #1: verbatim, at the cap
const stubFor = (bySlug) => async (_prompt, o) => (o && typeof o.label === 'string' && o.label.startsWith('scan:')) ? structuredClone(bySlug.get(o.label.slice(5))) : null

if (flag('--fingerprint')) {
  const { result } = await run(src, baseArgs(), stubFor(planted))
  console.log(String(result.cache_fingerprint || '').split('|')[0])
  process.exit(0)
}

console.log(`\nphase 2 — workflow: ${path.relative(REPO, workflowPath)}`)
const main = await run(src, baseArgs(), stubFor(planted))
const r = main.result
if (r.error || r.status === 'failed') { console.log(`run did not complete: ${r.error || r.reason}`); }
const fixNow = r.fix_now || {}
const flagH = r.flag_for_human || {}
const missing = fixNow.missing_targets || []
console.log(`orphans=${JSON.stringify(fixNow.orphans)}\nmissing_targets=${JSON.stringify(missing)}\nfrontmatter_drift=${JSON.stringify(fixNow.frontmatter_drift)}\nmalformed_frontmatter=${JSON.stringify(flagH.malformed_frontmatter)}\nscanner_return_rejected=${JSON.stringify(r.scanner_return_rejected)}\ncaps=${JSON.stringify(r.coverage_caps)}\nagent labels=${JSON.stringify(main.labels)}`)

// check (1)
check('(a) orphans === [lonely-page] exactly — the planted dropped links manufacture no orphan', JSON.stringify(fixNow.orphans) === JSON.stringify(['lonely-page']), JSON.stringify(fixNow.orphans))
check("(b) missing_targets names no 'cornerboxes' (bare-path twin not a link; [[ ]] twin resolves via crossLayerSlugs)", !missing.some((m) => /cornerboxes|seattle-seahawks/.test(m)), JSON.stringify(missing))
check('(c) no missing target for calf-strain (the same-page anchors)', !missing.some((m) => m.startsWith('calf-strain')), JSON.stringify(missing))
check('(d) control: code-fence-page → missing-target-page IS reported; ghost-page / ghost-two are not', missing.includes('code-fence-page → missing-target-page') && !missing.some((m) => /ghost/.test(m)), JSON.stringify(missing))
check('(e) control: katsuo-dashi#Simmer resolves to katsuo-dashi (no missing target for chicken-soup)', !missing.some((m) => m.startsWith('chicken-soup')), JSON.stringify(missing))
{
  // (f) the post-build scanner: the same returns with NO outbound_links at all → identical report.
  const bare = new Map([...planted].map(([slug, rec]) => { const c = structuredClone(rec); delete c.outbound_links; return [slug, c] }))
  const f = await run(src, baseArgs(), stubFor(bare))
  const view = (x) => JSON.stringify({ fix_now: x.fix_now, flag_for_human: x.flag_for_human, opportunities: x.opportunities, rejected: x.scanner_return_rejected })
  check('(f) a return with no outbound_links at all → identical fix_now / flag_for_human / opportunities', view(f.result) === view(r), f.result.error || f.result.reason || '')
}
{
  // (g) D4: the same cached records reused (key unchanged) while pageLinks drops the link → the verdict follows pageLinks.
  const cached = structuredClone(r.cache_records || [])
  const edited = structuredClone(facts.pageLinks)
  edited['fantasy-football-evaluation'] = edited['fantasy-football-evaluation'].filter((l) => l !== 'fantasy-platform-read-access')
  const g = await run(src, baseArgs({ cachedScans: cached, pageLinks: edited }), stubFor(planted))
  const go = (g.result.fix_now || {}).orphans
  console.log(`(g) files_cached=${g.result.files_cached} orphans=${JSON.stringify(go)} scan labels=${JSON.stringify(g.labels.filter((l) => String(l).startsWith('scan:')))}`)
  check('(g) the fantasy-football-evaluation record is REUSED (not re-dispatched) — pageLinks is not a key term', g.result.files_cached >= 10 && !g.labels.includes('scan:fantasy-football-evaluation'), `files_cached=${g.result.files_cached}`)
  check('(g) …and fantasy-platform-read-access IS an orphan — the verdict follows pageLinks, never the cache', Array.isArray(go) && go.includes('fantasy-platform-read-access') && go.includes('lonely-page'), JSON.stringify(go))
}

// check (2)
const drift = fixNow.frontmatter_drift || []
check('(2) frontmatter_drift carries parallel-walk-introduction: over-length (162 chars)', drift.includes('parallel-walk-introduction: over-length (162 chars)'), JSON.stringify(drift))
check('(2) frontmatter_drift carries lonely-page: summary missing', drift.includes('lonely-page: summary missing'), JSON.stringify(drift))
check('(2) NOTHING for l-theanine (159 on disk, 162 returned) or barbacoa (160, at the cap)', !drift.some((d) => /^(l-theanine|barbacoa)/.test(d)), JSON.stringify(drift))
check("(2) the prompt carries the length-exclusion sentence, once, outside every schema literal", (src.match(/LENGTH is never a frontmatter defect/g) || []).length === 1 && !/description:[^\n]*LENGTH is never a frontmatter defect/.test(src))
console.log(`(2) recorded, not asserted — the planted 'unclassified' length complaint for l-theanine ${(flagH.malformed_frontmatter || []).some((m) => m.startsWith('l-theanine')) ? 'STILL REACHES' : 'does not reach'} malformed_frontmatter (leg 3 of Cycle 14 build-1 (6) grades this live; the prompt is the only elimination for that key)`)

// check (3)
const pairLabels = main.labels.filter((l) => String(l).startsWith('entity-pair:'))
check('(3) exactly one entity-pair dispatched: chicken-soup+katsuo-dashi', JSON.stringify(pairLabels) === JSON.stringify(['entity-pair:chicken-soup+katsuo-dashi']), JSON.stringify(pairLabels))
check('(3) scanner_return_rejected === {count: 1, of: 11, slugs: [seattle-seahawks]}', JSON.stringify(r.scanner_return_rejected) === JSON.stringify({ count: 1, of: 11, slugs: ['seattle-seahawks'] }), JSON.stringify(r.scanner_return_rejected))
check('(3) the cap names the slug and the target', (r.coverage_caps || []).some((c) => c.includes('scanner_return_rejected') && c.includes('seattle-seahawks') && c.includes('new-england-patriots')), JSON.stringify(r.coverage_caps))
const recs = r.cache_records || []
check('(3) cache_records has 10 entries (scans − count) and seattle-seahawks is absent — rejection and non-persistence are one act', recs.length === 10 && !recs.some((c) => c.slug === 'seattle-seahawks'), `cache_records=${recs.length} slugs=${JSON.stringify(recs.map((c) => c.slug))}`)

console.log(`\n${failures ? `${failures} expectation(s) FAILED` : 'all expectations hold'}`)
process.exit(failures ? 1 : 0)
