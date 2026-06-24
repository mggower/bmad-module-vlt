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
//     budgetFloor:     number  (optional) // stop fanning out when budget.remaining() < this (default 40_000)
//     clusterCap:      number  (optional) // max cross-page contradiction clusters to check (default scales with page count)
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
const pages = Array.isArray(a.pages) ? a.pages : []
const indexPath = a.indexPath
const conventionsPath = a.conventionsPath
const crossLayerSlugs = Array.isArray(a.crossLayerSlugs) ? a.crossLayerSlugs : []
const budgetFloor = a.budgetFloor || 40_000
// Cluster cap scales with the wiki size — a fixed 12 sat one below the 13 natural clusters on the
// live wiki and falsely tripped the coverage cap every run. Floor of 12 holds for small wikis. (#3 §6)
const clusterCap = a.clusterCap || Math.max(12, Math.ceil(pages.length / 4))
// Model tiering — the page scanners are pure structured extraction (the bulk of the spend); a cheap
// model is sufficient and is where the ~10x cost win lives. Index + cluster passes do light reasoning. (#3 §2)
const scanModel = a.scanModel || 'haiku'
const indexModel = a.indexModel || 'sonnet'
const clusterModel = a.clusterModel || 'sonnet'

if (!pages.length || !indexPath || !conventionsPath) {
  return { error: 'vlt-lint-full requires { pages:[{slug,path}], indexPath, conventionsPath }. The vlt-lint SKILL discovers pages and passes live paths.' }
}

const PAGE_SCAN = {
  type: 'object',
  additionalProperties: false,
  required: ['slug', 'available', 'outbound_links', 'sources_count', 'frontmatter_valid', 'category', 'topic_is_list'],
  properties: {
    slug: { type: 'string' },
    available: { type: 'boolean', description: 'false if the page file could not be read — then it is dropped from the reduce' },
    title: { type: 'string' },
    last_updated: { type: 'string', description: "the page's frontmatter last_updated (or empty)" },
    outbound_links: { type: 'array', items: { type: 'string' }, description: 'wiki page slugs this page links to ([[...]] targets), normalized to slugs' },
    sources_count: { type: 'integer', description: 'number of entries in the frontmatter sources: list' },
    frontmatter_valid: { type: 'boolean', description: 'frontmatter present and well-formed per frontmatter.md (no key:, sources: parseable)' },
    category: { type: 'string', description: "the page's frontmatter category: value verbatim (empty string if the field is missing) — validated against the index H2 set in the index pass" },
    topic_is_list: { type: 'boolean', description: 'true if topic: is a YAML list; false if it is still a delimited string (a / b or a, b) or missing — a frontmatter-drift finding' },
    summary_issue: { type: 'string', description: "empty if summary: is present and ≤160 chars; else 'missing' or 'over-length (N chars)'" },
    frontmatter_issue: { type: 'string', description: 'what is wrong if frontmatter_valid is false' },
    sources_vs_prose_mismatch: { type: 'boolean', description: 'GAP B — true if the frontmatter sources: list and the prose Sources section diverge (a URL in one not the other)' },
    sources_vs_prose_detail: { type: 'string' },
    stale_unmarked: { type: 'array', items: { type: 'string' }, description: 'time-bound claims past their shelf life that LACK a [!stale] marker' },
    within_page_contradictions: { type: 'array', items: { type: 'string' }, description: 'incompatible claims inside this one page' },
    unmarked_supersession: { type: 'array', items: { type: 'string' }, description: 'silently-updated/conflicting claims lacking a [!superseded]/[!stale] callout, or consensus claims lacking citations' },
    thin: { type: 'boolean', description: 'few claims, no connections, single source — a merge/stub candidate' },
    key_claims: { type: 'array', items: { type: 'string' }, description: 'up to ~5 short claim summaries, for the cross-page contradiction pass' },
  },
}

const INDEX_SCAN = {
  type: 'object',
  additionalProperties: false,
  required: ['drift', 'malformed', 'category_violations'],
  properties: {
    malformed: { type: 'boolean', description: "true if the index's own structure is broken per wiki-index.md" },
    drift: { type: 'array', items: { type: 'string' }, description: 'index problems: a page missing from the index, a listed page that does not exist, a miscategorized row, or a malformed ## Stubs entry. The index is a structural map — it carries NO descriptions, source counts, or dates, so do not check those.' },
    category_violations: { type: 'array', items: { type: 'string' }, description: 'pages whose frontmatter category: does not exactly match any index H2 heading, as "slug: category \'X\' matches no H2" — the strict category↔H2 binding in wiki-index.md' },
  },
}

const CLUSTER_FINDINGS = {
  type: 'object',
  additionalProperties: false,
  required: ['cross_page_contradictions', 'handled_contradictions'],
  properties: {
    cross_page_contradictions: { type: 'array', items: { type: 'string' }, description: 'incompatible claims ACROSS pages in this cluster, as "page-a vs page-b: claim" — unhandled (no callout)' },
    handled_contradictions: { type: 'array', items: { type: 'string' }, description: 'GAP B — disagreements in this cluster that ARE already documented (a Contradictions section / callout) — surfaced so a well-managed disagreement is visible, not vanished' },
  },
}

// ── Phase 1: per-page fan-out, chunked with a budget guard ───────────────────
phase('Scan pages')

const pageScanPrompt = (p) =>
  `You are a wiki-lint page scanner. Read the wiki page at the LIVE path ${p.path} (slug "${p.slug}"). Read the conventions you judge against from ${conventionsPath}/frontmatter.md, ${conventionsPath}/wiki-supersession.md, and ${conventionsPath}/wiki-index.md (read once, apply per page). ` +
  `Return ONLY findings about THIS page: its outbound [[wikilink]] targets (as slugs), its frontmatter sources: count (number of entries in the frontmatter sources: list), whether frontmatter is valid, its frontmatter category: value verbatim (empty if missing), whether topic: is a YAML list (false if a delimited string or missing), the summary: issue if any ('missing' / 'over-length (N chars)' / empty if fine), whether the frontmatter sources: and the prose Sources section diverge (Gap B), time-bound claims past shelf life lacking a [!stale] marker, within-page contradictions, unmarked supersessions, whether the page is thin, and up to 5 short key-claim summaries. Do not assess other pages — cross-page checks happen later.`

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

const slugSet = new Set(scans.map((s) => s.slug))
const inbound = new Map()
for (const s of scans) for (const l of s.outbound_links || []) inbound.set(l, (inbound.get(l) || 0) + 1)

const orphans = scans.filter((s) => !(inbound.get(s.slug) > 0)).map((s) => s.slug)
// A [[link]] target that resolves to a wiki slug OR a known cross-layer note (research / agent-zone,
// supplied by the SKILL which has filesystem access) is valid; only a target resolving to NOTHING
// anywhere is a missing target. Without crossLayer, valid cross-layer links false-positive en masse. (#3 §4)
const crossLayer = new Set(crossLayerSlugs)
const missing_targets = []
for (const s of scans) for (const l of s.outbound_links || []) if (!slugSet.has(l) && !crossLayer.has(l)) missing_targets.push(`${s.slug} → ${l}`)

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
const linkSets = scans.map((s) => new Set((s.outbound_links || []).filter((l) => !hubs.has(l))))
const stem = (slug) => slug.split('-').slice(0, 2).join('-')
const titleTokens = scans.map((s) => new Set((s.title || s.slug).toLowerCase().split(/[^a-z0-9]+/).filter((t) => t.length > 2)))
const titleSimilar = (i, j) => {
  const A = titleTokens[i], B = titleTokens[j]
  if (!A.size || !B.size) return false
  let inter = 0
  for (const t of A) if (B.has(t)) inter++
  return inter / (A.size + B.size - inter) >= 0.5 // Jaccard ≥ 0.5 on title tokens
}
let pairBudget = 2_000_000
let nearCapped = false
outer: for (let i = 0; i < scans.length; i++) {
  for (let j = i + 1; j < scans.length; j++) {
    if (pairBudget-- <= 0) { nearCapped = true; break outer }
    let shared = 0
    for (const l of linkSets[i]) if (linkSets[j].has(l)) shared++
    if (shared < NEAR_SHARED_MIN) continue // shared-link signal is the necessary first gate
    const sameStem = stem(scans[i].slug) === stem(scans[j].slug)
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
  `You are a wiki-index linter. Read the live index at ${indexPath} and judge it against ${conventionsPath}/wiki-index.md. The wiki currently contains exactly these page slugs: ${[...slugSet].join(', ')}. Each page's frontmatter category: is: ${scans.map((s) => `${s.slug}=${s.category || '(none)'}`).join(', ')}. ` +
    `The index is a STRUCTURAL MAP — it carries no descriptions, source counts, or dates; do not check those. Report (1) index drift: pages missing from the index, listed pages that don't exist, miscategorized rows, malformed ## Stubs entries; and (2) category_violations: every page above whose category does not EXACTLY match one of the index's ## H2 headings (the strict category↔H2 binding) — as "slug: category 'X' matches no H2". A page with category '(none)' is missing the field — report it as a violation too.`,
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
    const sLinks = new Set(s.outbound_links || [])
    let shared = 0
    for (const l of t.outbound_links || []) if (sLinks.has(l) || l === s.slug) shared++
    if (shared >= 2 || (t.outbound_links || []).includes(s.slug)) { group.push(t); clustered.add(t.slug) }
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
          `Find incompatible claims ACROSS these pages that lack a supersession/contradiction callout (unhandled), and SEPARATELY list disagreements that ARE already documented with a Contradictions section or callout (handled — Gap B: surface them so a well-managed disagreement stays visible).`,
        { label: 'contradict-cluster', phase: 'Reduce + cross-page', schema: CLUSTER_FINDINGS, model: clusterModel },
      ),
    )
  )
).filter(Boolean)

// ── Assemble the structured report (vlt-lint Step 5 shape + Gap B slots) ─────
const flat = (key) => clusterResults.flatMap((c) => c[key] || [])
const collect = (key) => scans.flatMap((s) => (s[key] || []).map((v) => `${s.slug}: ${v}`))

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
      .filter((s) => s.topic_is_list === false || (s.summary_issue && s.summary_issue.length))
      .map((s) => `${s.slug}: ${[s.topic_is_list === false ? 'topic not a list' : '', s.summary_issue].filter(Boolean).join('; ')}`),
    unmarked_supersessions: collect('unmarked_supersession'),
    sources_vs_prose_mismatches: scans.filter((s) => s.sources_vs_prose_mismatch).map((s) => `${s.slug}: ${s.sources_vs_prose_detail || 'frontmatter sources: vs prose Sources diverge'}`),
  },
  flag_for_human: {
    category_no_match: indexScan ? indexScan.category_violations || [] : [],
    stale: collect('stale_unmarked'),
    contradictions: flat('cross_page_contradictions').concat(collect('within_page_contradictions')),
    // GAP B — handled contradictions get their own slot instead of vanishing into an empty list.
    contradictions_handled: flat('handled_contradictions'),
    thin_pages: scans.filter((s) => s.thin).map((s) => s.slug),
    malformed_frontmatter: scans.filter((s) => s.frontmatter_valid === false).map((s) => `${s.slug}: ${s.frontmatter_issue || 'invalid'}`),
    index_malformed: indexScan ? !!indexScan.malformed : false,
  },
  opportunities: {
    near_duplicates,
  },
  coverage_caps: coverageCaps,
}
