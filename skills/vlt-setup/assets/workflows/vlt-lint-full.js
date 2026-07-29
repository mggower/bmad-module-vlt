export const meta = {
  name: 'vlt-lint-full',
  description: 'Fan-out health-check of the whole wiki — one agent per page, findings reduced into the structured lint report',
  whenToUse: 'Invoked by vlt-lint for a --full sweep once the wiki is large enough that single-context linting is expensive. Read-only: it FINDS and returns structured findings; the vlt-lint SKILL applies the safe fixes serially (single-writer).',
  phases: [
    { title: 'Scan pages', detail: 'one agent per wiki page returns its self-contained findings + graph data', model: 'haiku' },
    { title: 'Reduce + cross-page', detail: 'JS reduces the graph (orphans/missing/near-dup); index + contradiction-cluster passes', model: 'sonnet' },
  ],
}

// ─────────────────────────────────────────────────────────────────────────────
// vlt-lint-full — the fan-out finder (owner-prioritized op-layer workflow).
//
// The script has NO filesystem access, so the vlt-lint SKILL discovers the page
// list (cheap: a glob over {wiki}) and passes it in, with LIVE absolute paths
// (the cache fix — agents read the live project tree, never a plugin copy).
//
// args:
//   {
//     pages:           [{ slug, path }]   // every wiki page to scan (LIVE abs paths). required.
//     indexPath:       string             // LIVE abs path to {index}. required.
//     conventionsPath: string             // LIVE abs path to {conventions} dir. required.
//     crossLayerSlugs: [string] (optional)// normalized basenames of valid NON-wiki link targets (research /
//                                          //   agent-zone notes the SKILL globbed) — a [[link]] to one of these
//                                          //   is NOT a missing target. default []. (filing #3 §4)
//     stubSlugs:       [string] (optional)// slugs cataloged under {index}'s "## Stubs" section (the SKILL parses
//                                          //   them) — a [[link]] to a registered stub is a RECORDED gap, not a
//                                          //   missing target. default []. (B5-3)
//     today:           string  (optional) // 'YYYY-MM-DD' — the SKILL passes it (scripts have no Date.now());
//                                          //   needed to compute review_due; absent → review_due not computed
//                                          //   (reported as a coverage cap).
//     budgetFloor:     number  (optional) // stop fanning out when budget.remaining() < this (default 40_000)
//     clusterCap:      number  (optional) // max cross-page contradiction clusters to check (default scales with page count)
//     pairCap:         number  (optional) // max callout-seeded entity pairs to compare in the second pass (default 24);
//                                          //   excess seeded pairs are reported in coverage_caps, never silently dropped
//     scanModel:       string  (optional) // model for the per-page scanners (pure extraction). default 'haiku' — the ~10x cost win.
//     indexModel:      string  (optional) // model for the index-drift pass (light reasoning). default 'sonnet'.
//     clusterModel:    string  (optional) // model for the cross-page contradiction pass (light judgement). default 'sonnet'.
//   }
// returns the structured findings (the vlt-lint Step 5 report shape, pre-fix, + Gap B slots).
// The SKILL applies fix_now, files backlog_candidates, emits the report, and logs.
// ─────────────────────────────────────────────────────────────────────────────

// The Workflow runtime delivers `args` as a JSON-encoded STRING, not the object the
// caller passed (true for name-, scriptPath-, and inline-script invocation alike).
// Parse defensively so the sweep runs on the first try — without this, `a` is the raw
// string, `a.pages` is undefined, and the guard below wrongly bails "args missing".
let a = args || {}
if (typeof a === 'string') { try { a = JSON.parse(a) } catch { a = {} } }

// Deterministic slug normalization — the seam fix (B5-3): scanners EXTRACT link targets
// verbatim; every comparison below runs on THIS normal form, computed here, never by a model.
const normalizeTarget = (t) => String(t || '')
  .replace(/^\s*\[\[/, '').replace(/\]\]\s*$/, '') // tolerate [[ ]] a scanner left on "inner text"
  .split('|')[0].split('#')[0]           // strip |alias, #anchor
  .trim().replace(/\.md$/i, '')          // strip extension
  .split('/').pop()                      // basename (path prefix off)
  .trim().toLowerCase()

const pages = Array.isArray(a.pages) ? a.pages : []
const indexPath = a.indexPath
const conventionsPath = a.conventionsPath
const crossLayerSlugs = (Array.isArray(a.crossLayerSlugs) ? a.crossLayerSlugs : []).map(normalizeTarget).filter(Boolean)
const stubSlugs = (Array.isArray(a.stubSlugs) ? a.stubSlugs : []).map(normalizeTarget).filter(Boolean)
const today = typeof a.today === 'string' ? a.today : ''
const budgetFloor = a.budgetFloor || 40_000
// Cluster cap scales with the wiki size — a fixed 12 sat one below the 13 natural clusters on the
// live wiki and falsely tripped the coverage cap every run. Floor of 12 holds for small wikis. (#3 §6)
const clusterCap = a.clusterCap || Math.max(12, Math.ceil(pages.length / 4))
// Model tiering — the page scanners are pure structured extraction (the bulk of the spend); a cheap
// model is sufficient and is where the ~10x cost win lives. Index + cluster passes do light reasoning. (#3 §2)
const pairCap = Number.isInteger(a.pairCap) ? a.pairCap : 24 // 0 is a valid (test) value — no || fallback
const scanModel = a.scanModel || 'haiku'
const indexModel = a.indexModel || 'sonnet'
const clusterModel = a.clusterModel || 'sonnet'

if (!pages.length || !indexPath || !conventionsPath) {
  return { error: 'vlt-lint-full requires { pages:[{slug,path}], indexPath, conventionsPath }. The vlt-lint SKILL discovers pages and passes live paths.' }
}

const PAGE_SCAN = {
  type: 'object',
  additionalProperties: false,
  required: ['slug', 'available', 'title', 'outbound_links', 'frontmatter_valid', 'category', 'topic_is_list', 'summary', 'last_updated', 'verified_by', 'verified_at', 'review_after', 'name_callout_targets'],
  properties: {
    slug: { type: 'string' },
    available: { type: 'boolean', description: 'false if the page file could not be read — then it is dropped from the reduce' },
    title: { type: 'string', description: "the page's frontmatter title value verbatim (empty if absent — an omitted title would silently fall back to slug tokens in the near-dup title signal)" },
    created: { type: 'string', description: "the page's frontmatter created date (or empty) — the SKILL uses it to gate unattested_write as informational for pre-convention files" },
    last_updated: { type: 'string', description: "the page's frontmatter last_updated (or empty)" },
    verified_by: { type: 'string', description: "the frontmatter verified_by value verbatim (empty if absent)" },
    verified_at: { type: 'string', description: "the frontmatter verified_at value verbatim (empty if absent)" },
    review_after: { type: 'string', description: "the frontmatter review_after date verbatim (empty if absent — absence = evergreen)" },
    outbound_links: { type: 'array', items: { type: 'string' }, description: 'the raw [[wikilink]] inner text of every outbound link on this page, verbatim — including any |alias, #anchor, or path prefix; do not normalize' },
    frontmatter_valid: { type: 'boolean', description: 'frontmatter present and well-formed per frontmatter.md (no key:, sources: parseable)' },
    category: { type: 'string', description: "the page's frontmatter category: value verbatim (empty string if the field is missing) — validated against the index H2 set in the index pass" },
    topic_is_list: { type: 'boolean', description: 'true if topic: is a YAML list; false if it is still a delimited string (a / b or a, b) or missing — a frontmatter-drift finding' },
    summary: { type: 'string', description: 'the frontmatter summary: value verbatim (empty string if the field is absent)' },
    frontmatter_issue: { type: 'string', description: 'what is wrong if frontmatter_valid is false' },
    sources_vs_prose_mismatch: { type: 'boolean', description: 'GAP B — true if the frontmatter sources: list and the prose Sources section diverge (a URL in one not the other)' },
    sources_vs_prose_detail: { type: 'string' },
    stale_unmarked: { type: 'array', items: { type: 'string' }, description: 'time-bound claims past their shelf life that LACK a [!stale] marker' },
    within_page_contradictions: { type: 'array', items: { type: 'string' }, description: 'incompatible claims inside this one page' },
    unmarked_supersession: { type: 'array', items: { type: 'string' }, description: 'silently-updated/conflicting claims lacking a [!superseded]/[!stale] callout, or consensus claims lacking citations' },
    thin: { type: 'boolean', description: 'few claims, no connections, single source — a merge/stub candidate' },
    key_claims: { type: 'array', items: { type: 'string' }, description: 'up to ~5 short claim summaries, for the cross-page contradiction pass' },
    name_callout_targets: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['target', 'name'], properties: {
      target: { type: 'string', description: 'the [[wikilinked]] page the callout names — the raw wikilink inner text, verbatim; do not normalize' },
      name: { type: 'string', description: 'the proper noun the callout questions' },
    } }, description: 'one entry per callout on THIS page that questions a proper noun against another named wiki page (a name-verification / [!stale] callout whose body says this page and that page disagree about a name) — the vault marking a suspect pair. Empty when the page carries none.' },
  },
}

const INDEX_SCAN = {
  type: 'object',
  additionalProperties: false,
  required: ['drift', 'malformed', 'h2_headings'],
  properties: {
    malformed: { type: 'boolean', description: "true if the index's own structure is broken per wiki-index.md" },
    drift: { type: 'array', items: { type: 'string' }, description: 'index problems: a page missing from the index, a listed page that does not exist, a miscategorized row, or a malformed ## Stubs entry. The index is a structural map — it carries NO descriptions, source counts, or dates, so do not check those.' },
    h2_headings: { type: 'array', items: { type: 'string' }, description: "every H2 heading in the index, verbatim and in order — the heading text exactly as written, with only the leading '## ' marker removed. Do not judge categories against it; the category↔H2 comparison is computed downstream." },
  },
}

const CLUSTER_FINDINGS = {
  type: 'object',
  additionalProperties: false,
  required: ['cross_page_contradictions', 'documented_open', 'documented_adjudicable', 'documented_undispositioned', 'entity_collisions'],
  properties: {
    cross_page_contradictions: { type: 'array', items: { type: 'string' }, description: 'incompatible claims ACROSS pages in this cluster, as "page-a vs page-b: claim" — unhandled (no callout)' },
    documented_open: { type: 'array', items: { type: 'string' }, description: 'disagreements ALREADY documented whose callout literally records "**Disposition:** open" — classify by reading that line, never by judging the disagreement yourself' },
    documented_adjudicable: { type: 'array', items: { type: 'string' }, description: 'disagreements ALREADY documented whose callout literally records "**Disposition:** adjudicable" — classify by reading that line, never by judging the disagreement yourself. Carry the callout\'s "Closes when" / "Filed" detail where present.' },
    documented_undispositioned: { type: 'array', items: { type: 'string' }, description: 'disagreements ALREADY documented whose callout carries NO **Disposition:** line (it predates the convention, or the writer omitted it). This is not an error and NOT a guess-bucket — a callout with no disposition goes here and is never guessed into open or adjudicable.' },
    entity_collisions: { type: 'array', items: { type: 'string' }, description: 'the SAME proper noun recorded with INCOMPATIBLE attributes across two pages in this cluster (two mutually exclusive affiliations, two incompatible roles in one period), as "page-a vs page-b: <name> — <attribute A> vs <attribute B>"' },
  },
}

// ── Phase 1: per-page fan-out, chunked with a budget guard ───────────────────
phase('Scan pages')

const pageScanPrompt = (p) =>
  `You are a wiki-lint page scanner. Read the wiki page at the LIVE path ${p.path} (slug "${p.slug}"). Read the conventions you judge against from ${conventionsPath}/frontmatter.md, ${conventionsPath}/wiki-supersession.md, and ${conventionsPath}/wiki-index.md (read once, apply per page). ` +
  `Return ONLY findings about THIS page: the raw [[wikilink]] inner text of every outbound link, verbatim — including any |alias, #anchor, or path prefix; do not normalize — whether frontmatter is valid, its frontmatter category: value verbatim (empty if missing), whether topic: is a YAML list (false if a delimited string or missing), the frontmatter summary: value verbatim (empty if absent), whether the frontmatter sources: and the prose Sources section diverge (Gap B), its created and last_updated dates verbatim, its verified_by and verified_at values verbatim (empty if absent), its review_after date verbatim (empty if absent), time-bound claims past shelf life lacking a [!stale] marker, within-page contradictions, unmarked supersessions, whether the page is thin, up to 5 short key-claim summaries, and name_callout_targets — for each callout on this page that questions a proper noun against another named wiki page, the raw [[wikilink]] target text verbatim and the name in question (an ordinary [!stale] marker with no cross-page name question yields nothing). Do not assess other pages — cross-page checks happen later.`

const scans = []
const coverageCaps = []
const CHUNK = 16
for (let i = 0; i < pages.length; i += CHUNK) {
  if (budget.total && budget.remaining() < budgetFloor) {
    const msg = `budget guard: scanned ${scans.length}/${pages.length} pages before the remaining budget fell below ${budgetFloor} — the rest were NOT checked`
    coverageCaps.push(msg)
    log(msg)
    break
  }
  const chunk = pages.slice(i, i + CHUNK)
  const part = await parallel(chunk.map((p) => () => agent(pageScanPrompt(p), { label: `scan:${p.slug}`, phase: 'Scan pages', schema: PAGE_SCAN, model: scanModel })))
  scans.push(...part.filter(Boolean).filter((s) => s.available !== false))
  log(`scanned ${scans.length}/${pages.length} pages`)
}

// ── JS reduce: the link graph (free — no agents) ─────────────────────────────
phase('Reduce + cross-page')

// Normalize once at intake (B5-3): scanners returned raw wikilink text; every graph
// comparison below runs on the normal form. Empty-after-normalization targets (e.g. a
// bare [[#anchor]]) are dropped, not compared.
for (const s of scans) s.outbound_links = (s.outbound_links || []).map(normalizeTarget).filter(Boolean)
const nslug = (s) => normalizeTarget(s.slug)

const slugSet = new Set(scans.map(nslug))
const inbound = new Map()
for (const s of scans) for (const l of s.outbound_links) inbound.set(l, (inbound.get(l) || 0) + 1)

const orphans = scans.filter((s) => !(inbound.get(nslug(s)) > 0)).map((s) => s.slug)
// A [[link]] target that resolves to a wiki slug OR a known cross-layer note (research / agent-zone,
// supplied by the SKILL which has filesystem access) is valid; only a target resolving to NOTHING
// anywhere is a missing target. Without crossLayer, valid cross-layer links false-positive en masse. (#3 §4)
// A target registered under the index's ## Stubs section is a RECORDED gap, not a missing target (B5-3).
const crossLayer = new Set(crossLayerSlugs)
const stubs = new Set(stubSlugs)
const missing_targets = []
for (const s of scans) for (const l of s.outbound_links) if (!slugSet.has(l) && !crossLayer.has(l) && !stubs.has(l)) missing_targets.push(`${s.slug} → ${l}`)

// near-duplicates (#3 §5): a pair is a near-duplicate ONLY when a shared-link signal COINCIDES with a
// secondary signal (shared slug stem OR title similarity) — never shared links alone. Shared links
// alone fire constantly from hub/entity co-citation (70 false pairs on the live wiki), so we
//   (a) exclude cluster-hub links (targets cited by many pages) before counting shared, and
//   (b) require BOTH a shared-link signal AND a structural secondary signal.
// O(n^2) on link sets — fine for hundreds; cap the comparison budget for very large wikis and log if hit.
const near_duplicates = []
const NEAR_SHARED_MIN = 3
const hubThreshold = Math.max(5, Math.ceil(scans.length * 0.25))
const hubs = new Set([...inbound.entries()].filter(([, n]) => n > hubThreshold).map(([l]) => l))
const linkSets = scans.map((s) => new Set(s.outbound_links.filter((l) => !hubs.has(l))))
const stem = (slug) => slug.split('-').slice(0, 2).join('-')
// A stem shared by 4+ pages is a topical family (nfl-2026-*), not a duplicate signal — within a
// family the stem always matches and the two-signal design would degenerate to shared-links-only.
// A true near-duplicate is a pair; 2–3 shared stems are still legitimate drift suspects. (B5-3)
const stemCounts = new Map()
for (const s of scans) { const k = stem(s.slug); stemCounts.set(k, (stemCounts.get(k) || 0) + 1) }
const familyStem = (k) => (stemCounts.get(k) || 0) >= 4
const titleTokens = scans.map((s) => new Set((s.title || s.slug).toLowerCase().split(/[^a-z0-9]+/).filter((t) => t.length > 2)))
const titleSimilar = (i, j) => {
  const A = titleTokens[i], B = titleTokens[j]
  if (!A.size || !B.size) return false
  let inter = 0
  for (const t of A) if (B.has(t)) inter++
  return inter / (A.size + B.size - inter) >= 0.5 // Jaccard ≥ 0.5 on title tokens
}
if (!today) { const m = `no 'today' arg provided — review_due was NOT computed (pass today: 'YYYY-MM-DD')`; coverageCaps.push(m); log(m) }

let pairBudget = 2_000_000
let nearCapped = false
outer: for (let i = 0; i < scans.length; i++) {
  for (let j = i + 1; j < scans.length; j++) {
    if (pairBudget-- <= 0) { nearCapped = true; break outer }
    let shared = 0
    for (const l of linkSets[i]) if (linkSets[j].has(l)) shared++
    if (shared < NEAR_SHARED_MIN) continue // shared-link signal is the necessary first gate
    const sameStem = stem(scans[i].slug) === stem(scans[j].slug) && !familyStem(stem(scans[i].slug))
    const titSim = titleSimilar(i, j)
    if (sameStem || titSim) {
      const secondary = sameStem ? 'shared slug stem' : 'title overlap'
      near_duplicates.push(`${scans[i].slug} + ${scans[j].slug} (${shared} shared non-hub links + ${secondary})`)
    }
  }
}
if (nearCapped) { const m = `near-duplicate comparison capped — not all page pairs were compared`; coverageCaps.push(m); log(m) }

// ── Index pass (one agent, reads the live index + the computed page set) ─────
const indexScan = await agent(
  `You are a wiki-index linter. Read the live index at ${indexPath} and judge it against ${conventionsPath}/wiki-index.md. The wiki currently contains exactly these page slugs: ${[...slugSet].join(', ')}. ` +
    `The index is a STRUCTURAL MAP — it carries no descriptions, source counts, or dates; do not check those. Report (1) index drift: pages missing from the index, listed pages that don't exist, miscategorized rows, malformed ## Stubs entries; and (2) h2_headings: every H2 heading in the index, verbatim and in order — the heading text exactly as written, with only the leading '## ' marker removed. Do not judge page categories against the headings; that comparison is computed downstream.`,
  { label: 'index-drift', phase: 'Reduce + cross-page', schema: INDEX_SCAN, model: indexModel },
)

// ── Cross-page contradiction clusters (bounded; clusters by shared links) ────
// Build clusters greedily from link adjacency, cap the number of clusters checked.
const clustered = new Set()
const clusters = []
for (const s of scans) {
  if (clustered.has(s.slug)) continue
  const group = [s]
  clustered.add(s.slug)
  for (const t of scans) {
    if (clustered.has(t.slug)) continue
    const sLinks = new Set(s.outbound_links)
    let shared = 0
    for (const l of t.outbound_links) if (sLinks.has(l) || l === nslug(s)) shared++
    if (shared >= 2 || t.outbound_links.includes(nslug(s))) { group.push(t); clustered.add(t.slug) }
  }
  if (group.length >= 2) clusters.push(group)
}
let clustersToCheck = clusters
if (clusters.length > clusterCap) {
  clustersToCheck = clusters.slice(0, clusterCap)
  const m = `cross-page contradiction check capped at ${clusterCap}/${clusters.length} clusters — the rest were not checked for cross-page contradictions`
  coverageCaps.push(m)
  log(m)
}

const clusterResults = (
  await parallel(
    clustersToCheck.map((group) => () =>
      agent(
        `You are a cross-page contradiction checker. These wiki pages share topic/links and may conflict. For each, read its LIVE path. Pages: ${group.map((g) => `${g.slug} (${pages.find((p) => p.slug === g.slug)?.path || '?'})`).join('; ')}. ` +
          `Key claims already extracted: ${JSON.stringify(group.map((g) => ({ slug: g.slug, claims: g.key_claims || [] })))}. ` +
          `Find incompatible claims ACROSS these pages that lack a supersession/contradiction callout (unhandled). SEPARATELY, for disagreements that ARE already documented with a Contradictions section or callout, split them by the callout's recorded "**Disposition:**" line: open -> documented_open, adjudicable -> documented_adjudicable. A documented disagreement whose callout carries NO Disposition line goes to documented_undispositioned — do NOT infer a disposition for it, and never guess it into open or adjudicable. ` +
          `ALSO report entity_collisions: the same proper noun recorded with incompatible attributes across two of these pages. PRECEDENCE — a conflict that is one name carrying incompatible attributes goes to entity_collisions and NOT to cross_page_contradictions; report it once, in one slot.`,
        { label: 'contradict-cluster', phase: 'Reduce + cross-page', schema: CLUSTER_FINDINGS, model: clusterModel },
      ),
    )
  )
).filter(Boolean)

// ── Callout-seeded entity-pair pass (B5-2) ───────────────────────────────────
// Greedy cluster consumption can split even directly-linked pages, and entity_collisions
// is only ever asked within a cluster — so pairs the vault itself has marked suspicious
// (a name-verification callout on one page questioning a proper noun against another)
// are compared here, wherever clustering put them. Seeds are callouts ONLY, never all
// cross-cluster direct links — the unmarked-split-pair residual is stated in the SKILL's
// entity_scan: denominator, not chased here.
const PAIR_FINDINGS = {
  type: 'object',
  additionalProperties: false,
  required: ['entity_collisions'],
  properties: {
    entity_collisions: { type: 'array', items: { type: 'string' }, description: 'the SAME proper noun recorded with INCOMPATIBLE attributes across these two pages, as "page-a vs page-b: <name> — <attribute A> vs <attribute B>". Empty when the marked pair does not actually collide.' },
  },
}

const pairKey = (x, y) => [x, y].sort().join('|')
const comparedPairs = new Set()
for (const group of clustersToCheck)
  for (let i = 0; i < group.length; i++)
    for (let j = i + 1; j < group.length; j++) comparedPairs.add(pairKey(group[i].slug, group[j].slug))

const seedMap = new Map() // pairKey -> { a, b, name }
for (const s of scans)
  for (const t of s.name_callout_targets || []) {
    const target = t && normalizeTarget(t.target) // raw wikilink text in, normal form compared (B5-3)
    if (!target || !slugSet.has(target) || target === nslug(s)) continue
    const k = pairKey(s.slug, target)
    if (comparedPairs.has(k) || seedMap.has(k)) continue
    seedMap.set(k, { a: s.slug, b: target, name: t.name })
  }
const seededPairsTotal = seedMap.size
let seededPairs = [...seedMap.values()]
if (seededPairs.length > pairCap) {
  seededPairs = seededPairs.slice(0, pairCap)
  const m = `callout-seeded entity-pair check capped at ${pairCap}/${seededPairsTotal} pairs — ${seededPairsTotal - pairCap} vault-marked pairs were NOT compared`
  coverageCaps.push(m)
  log(m)
}

const seededResults = (
  await parallel(
    seededPairs.map((pr) => () =>
      agent(
        `You are a cross-page entity-collision checker. A name-verification callout marked these two wiki pages as a suspect pair over the proper noun "${pr.name}". Read BOTH at their LIVE paths: ${pr.a} (${pages.find((p) => p.slug === pr.a)?.path || '?'}); ${pr.b} (${pages.find((p) => p.slug === pr.b)?.path || '?'}). ` +
          `Judge the PAGES, not the callout: report entity_collisions — the same proper noun recorded with incompatible attributes across these two pages, as "page-a vs page-b: <name> — <attribute A> vs <attribute B>". PRECEDENCE — a conflict that is one name carrying incompatible attributes is an entity collision, never also a contradiction. Report nothing else; a marked pair whose pages do not actually collide returns empty (that is the pass working, not failing).`,
        { label: `entity-pair:${pr.a}+${pr.b}`, phase: 'Reduce + cross-page', schema: PAIR_FINDINGS, model: clusterModel },
      ),
    )
  )
).filter(Boolean)
// Duplication with cluster findings is impossible by construction — only never-compared pairs run.
const seededCollisions = seededResults.flatMap((r) => (r.entity_collisions || []).map((f) => `${f} (callout-seeded)`))

// ── Assemble the structured report (vlt-lint Step 5 shape + Gap B slots) ─────
const flat = (key) => clusterResults.flatMap((c) => c[key] || [])
const collect = (key) => scans.flatMap((s) => (s[key] || []).map((v) => `${s.slug}: ${v}`))

// Verdicts computed from verbatim extractions (B5-3) — the scanner reads, JS does the arithmetic.
const summaryIssue = (s) => !(s.summary || '').trim() ? 'summary missing' : s.summary.length > 160 ? `over-length (${s.summary.length} chars)` : ''
const attested = (s) => !!(s.verified_by && s.verified_at) // present = both non-empty
const h2set = new Set(indexScan ? indexScan.h2_headings || [] : [])

return {
  mode: 'full',
  // GAP B — files_checked counting rule: pages an agent actually SCANNED (not merely listed).
  files_checked: scans.length,
  files_listed: pages.length,
  fix_now: {
    orphans,
    missing_targets,
    index_drift: indexScan ? indexScan.drift : [],
    frontmatter_drift: scans
      .filter((s) => s.topic_is_list === false || summaryIssue(s))
      .map((s) => `${s.slug}: ${[s.topic_is_list === false ? 'topic not a list' : '', summaryIssue(s)].filter(Boolean).join('; ')}`),
    unmarked_supersessions: collect('unmarked_supersession'),
    sources_vs_prose_mismatches: scans.filter((s) => s.sources_vs_prose_mismatch).map((s) => `${s.slug}: ${s.sources_vs_prose_detail || 'frontmatter sources: vs prose Sources diverge'}`),
  },
  flag_for_human: {
    // Exact match against the extracted H2 set, computed here (B5-3) — the strict category↔H2
    // binding is case-sensitive by design: no trimming, no case folding.
    category_no_match: indexScan ? scans.filter((s) => !h2set.has(s.category)).map((s) => `${s.slug}: category '${s.category || '(none)'}' matches no H2`) : [],
    // Attestation findings (write-verification contract). PARA files are outside this workflow's
    // page set (it sweeps {wiki}) — para_missing_attestation is a structural slot the SKILL fills
    // from its own PARA jurisdiction scan; it is emitted here so the report shape is complete.
    para_missing_attestation: [],
    // ISO YYYY-MM-DD strings compare lexicographically — the same property review_due relies on.
    unattested_write: scans.filter((s) => !attested(s)).map((s) => `${s.slug} (created ${s.created || '?'})`),
    attestation_stale: scans.filter((s) => attested(s) && s.last_updated && s.last_updated > s.verified_at).map((s) => `${s.slug}: last_updated > verified_at`),
    review_due: today
      ? scans.filter((s) => s.review_after && s.review_after <= today).map((s) => `${s.slug} — review_after ${s.review_after}`)
      : [],
    stale: collect('stale_unmarked'),
    contradictions: flat('cross_page_contradictions').concat(collect('within_page_contradictions')),
    // Documented contradictions split by their RECORDED disposition — never by the mere existence of a callout.
    contradictions_open: flat('documented_open'),
    contradictions_deferred: flat('documented_adjudicable'),
    contradictions_undispositioned: flat('documented_undispositioned'),
    // Source-fidelity findings, kept out of the contradiction slots by the precedence rule in the
    // cluster prompt. Cluster findings first, then the callout-seeded pair pass's (each carrying a
    // " (callout-seeded)" provenance suffix — a marker, not a bucket). The SKILL composes the
    // entity_scan: denominator line itself from the top-level entity_scan_facts below — exactly as
    // it composes contradiction_scan: from its own run facts.
    entity_collisions: flat('entity_collisions').concat(seededCollisions),
    thin_pages: scans.filter((s) => s.thin).map((s) => s.slug),
    malformed_frontmatter: scans.filter((s) => s.frontmatter_valid === false).map((s) => `${s.slug}: ${s.frontmatter_issue || 'invalid'}`),
    index_malformed: indexScan ? !!indexScan.malformed : false,
  },
  opportunities: {
    near_duplicates,
  },
  // Honest facts for the SKILL's entity_scan: denominator composition (Step 5) — exact counts
  // even on an uncapped run, so the line never has to be inferred from cap messages.
  entity_scan_facts: {
    clusters_checked: clustersToCheck.length,
    clusters_total: clusters.length,
    seeded_pairs_checked: seededPairs.length,
    seeded_pairs_total: seededPairsTotal,
  },
  coverage_caps: coverageCaps,
}
