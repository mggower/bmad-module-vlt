export const meta = {
  name: 'vlt-lint-full',
  description: 'Fan-out health-check of the whole wiki — one agent per page, findings reduced into the structured lint report',
  whenToUse: 'Invoked by vlt-lint for a --full sweep once the wiki is large enough that single-context linting is expensive. Read-only: it FINDS and returns structured findings; the vlt-lint SKILL applies the safe fixes serially (single-writer).',
  phases: [
    { title: 'Scan pages', detail: 'one agent per wiki page returns its self-contained findings', model: 'haiku' },
    { title: 'Reduce + cross-page', detail: 'JS reduces the graph (orphans/missing/near-dup) from the SKILL-derived link sets; index + contradiction-cluster passes', model: 'sonnet' },
  ],
}

// depends_on: ["frontmatter@14", "wiki-supersession@2", "wiki-index@2", "write-verification@5"]
// ^ the asset ack (B7-6): this workflow's prompts instruct agents to read these
//   conventions, so it is a listed consumer in its own right — the flat pins
//   above are its handshake acks, bumped on reconciliation like a skill's
//   depends_on:. The release gate (package-lint E5) parses this line.
//   R4 (the fan-out currency rule): any ask in this file that enforces a
//   convention's rule adds that convention to `SCANNER_CONVENTIONS` (which
//   feeds convRead AND the cache key) AND to the pins above in the same edit; any edit to an ask or to the read list re-runs the
//   fan-out audit (every ask checked against the convention set its scanner
//   receives); restated convention instructions in prompts carry inline
//   `per <convention>@N` source markers, which consumer walks re-derive.

// ─────────────────────────────────────────────────────────────────────────────
// vlt-lint-full — the fan-out finder (owner-prioritized op-layer workflow).
//
// The script has NO filesystem access, so the vlt-lint SKILL discovers the page
// list (cheap: a glob over {wiki}) and passes it in, with LIVE absolute paths
// (the cache fix — agents read the live project tree, never a plugin copy) —
// and, since Cycle 15 build-4, each page's raw [[ ]] set and parsed summary
// length (pageLinks / summaryLengths, derived by vlt-lint/scripts/lint-page-facts.py),
// so the link graph and the length verdicts run on bytes this script cannot read
// and never on a scanner's return.
//
// args:
//   {
//     pages:           [{ slug, path }]   // every wiki page to scan (LIVE abs paths). required — together
//                                          //   with pageLinks + summaryLengths below (the args guard names all five).
//     indexPath:       string             // LIVE abs path to {index}. required.
//     conventionsPath: string             // LIVE abs path to {conventions} dir. required.
//     overlaysPath:    string  (optional) // LIVE abs path to {overlays} (vault-local convention overlays).
//     overlayNames:    [string] (optional)// convention names whose overlay file actually EXISTS on disk
//                                          //   (the SKILL has filesystem access, this script has none — the
//                                          //   crossLayerSlugs/stubSlugs division). e.g. ["frontmatter"].
//                                          //   Absent overlay args → pages are judged base-only and
//                                          //   coverage_caps says so loudly (never a silent base-only run).
//     crossLayerSlugs: [string] (optional)// normalized basenames of valid NON-wiki link targets (research /
//                                          //   agent-zone notes the SKILL globbed) — a [[link]] to one of these
//                                          //   is NOT a missing target. default []. (filing #3 §4)
//     stubSlugs:       [string] (optional)// slugs cataloged under {index}'s Stubs section as `wiki-index.md`
//                                          //   states it (the SKILL locates and parses it — `checks.md` Missing
//                                          //   targets) — a [[link]] to a registered stub is a RECORDED gap, not a
//                                          //   missing target. default []. A present non-array is refused before
//                                          //   dispatch (A15-2 / A15-10, D2). (B5-3)
//     pageHashes:      {slug: sha256} (optional) // content digest per page, computed by the SKILL with an
//                                          //   unwrapped instrument it names in the record. Absent → no page
//                                          //   is cacheable this run (a cold sweep, stated, never silent).
//     pageLinks:       {slug: [string]}   // every [[…]] inner text on the page, RAW, derived from the page's
//                                          //   bytes by vlt-lint/scripts/lint-page-facts.py (the SKILL has
//                                          //   filesystem access, this script has none — the crossLayerSlugs
//                                          //   division); the reduce normalizes (normalizeTarget) and builds the
//                                          //   link graph from THIS, never from a scanner return (A15-1 / A15-3 /
//                                          //   A15-4, D-C). REQUIRED. A present non-object, or a non-array entry
//                                          //   for a listed page, is refused before dispatch; a page with no entry
//                                          //   is a denominated cap. NOT a cache-key term — recomputed from bytes
//                                          //   every run; no cached fact depends on it (D4).
//     summaryLengths:  {slug: int}        // the parsed summary: scalar's length in characters, from the same
//                                          //   script (A15-5, D-A); the reduce measures from THIS, never from the
//                                          //   returned summary. REQUIRED; same refusal/cap posture. NOT a
//                                          //   cache-key term — recomputed from bytes every run (D4).
//     cachedScans:     [{slug, key, scan}] (optional) // prior PAGE_SCAN records the SKILL read from the
//                                          //   sidecar (_agent/lint-cache.json, read through
//                                          //   vlt-lint/scripts/lint-cache.py) — they are the PREVIOUS run's
//                                          //   returned `cache_records`, handed back verbatim. A record is
//                                          //   reusable iff its `key` equals the key recomputed here from
//                                          //   THIS run's inputs. default []. (A11-11 direction 2; A14-8)
//     rulesetComponents: {…}   (optional) // the SKILL-side INPUTS to the ruleset half of the fingerprint —
//                                          //   named slots, never a list and never a pre-joined string:
//                                          //     convention_digests: {name: digest} — merged (base + overlay) digest
//                                          //                                  for EACH name in SCANNER_CONVENTIONS
//                                          //                                  (the three conventions the page
//                                          //                                  scanner reads); names outside the set
//                                          //                                  are ignored for the key and logged;
//                                          //                                  ORDER DOES NOT MATTER, this script
//                                          //                                  sorts by name
//                                          //   The SKILL computes the digests (it has filesystem access, this
//                                          //   script has none — see the no-filesystem note above); this script
//                                          //   COMPOSES them into `rulesetFingerprint`. A slot or required name
//                                          //   ABSENT or EMPTY → the fingerprint is '' → a cold sweep, each named
//                                          //   in `coverage_caps` under its own word (`absent […]` / `empty […]`);
//                                          //   a slot or name PRESENT BUT OF THE WRONG TYPE → the run is REFUSED
//                                          //   before any agent dispatches (`status: 'failed'`, the reason names
//                                          //   the slot and the type received) — a wrong type is the SKILL's own
//                                          //   rendering error, detectable before the first dispatch (A15-10, D2).
//                                          //   `rulesetFingerprint` is NOT an accepted arg: it is composed here,
//                                          //   never passed. (A14-8, Q6.2; A15-9 D-B — facts-not-verdicts: no
//                                          //   version, pin or checks digest)
//     today:           string  (optional) // 'YYYY-MM-DD' — the SKILL passes it (scripts have no Date.now());
//                                          //   needed to compute review_due; absent → review_due not computed
//                                          //   (reported as a coverage cap).
//     budgetFloor:     number  (optional) // stop fanning out when budget.remaining() < this (default 40_000)
//     clusterCap:      number  (optional) // max cross-page contradiction clusters to check (default scales with page count)
//     pairCap:         number  (optional) // max callout-seeded entity pairs to compare in the second pass (default 24);
//                                          //   excess seeded pairs are reported in coverage_caps, never silently dropped
//     scanModel:       string  (optional) // model for the per-page scanners (pure extraction). default 'haiku' — the ~10x cost win.
//                                          //   — enters the per-page cache key as the extractor identity; must be a non-empty string.
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
// Overlay args (B7-6): the merged-on-read contract crosses the fan-out boundary here.
const overlaysPath = typeof a.overlaysPath === 'string' ? a.overlaysPath : ''
const overlayNames = (Array.isArray(a.overlayNames) ? a.overlayNames : []).map((n) => String(n).replace(/\.overlay\.md$/i, '')).filter(Boolean)
const crossLayerSlugs = (Array.isArray(a.crossLayerSlugs) ? a.crossLayerSlugs : []).map(normalizeTarget).filter(Boolean)
// Wrong-type intake (A15-10, D2 — build-3): for the two D2 slots that cross the fan-out boundary,
// ABSENT (key not in args) keeps its empty default, but PRESENT-AND-WRONG-TYPE is recorded here and
// REFUSED before any agent dispatches (the pre-dispatch refusal below the cache reader) — never
// coerced to the empty value, which rendered a rendering error as an honest absence. The other
// four optional args (overlayNames, crossLayerSlugs, pageHashes, cachedScans) are NOT refused:
// D2's population is the three denominated slots and no further — a wrong type there still
// coerces to its empty value (a stated cold / base-only sweep), on record as a candidate filing.
// The two byte-fact slots (pageLinks, summaryLengths — Cycle 15 build-4) take the same refusal on
// that build's own ruling, not D2's: a slot introduced after the cycle established the posture
// takes it rather than adding a fifth to the candidate above.
const typeName = (v) => (Array.isArray(v) ? 'array' : v === null ? 'null' : typeof v)
const isPlainObject = (v) => !!v && typeof v === 'object' && !Array.isArray(v)
const wrongTypeSlots = []
if (a.stubSlugs !== undefined && !Array.isArray(a.stubSlugs)) wrongTypeSlots.push({ slot: 'stubSlugs', got: typeName(a.stubSlugs), expected: 'array' })
if (a.rulesetComponents !== undefined && !isPlainObject(a.rulesetComponents)) wrongTypeSlots.push({ slot: 'rulesetComponents', got: typeName(a.rulesetComponents), expected: 'plain object' })
const stubSlugs = (Array.isArray(a.stubSlugs) ? a.stubSlugs : []).map(normalizeTarget).filter(Boolean)
const today = typeof a.today === 'string' ? a.today : ''
// Findings-cache args (A11-11 direction 2). All three optional; any one absent → a cold sweep.
// Read from the PARSED `a` above, never from the raw `args` string.
const pageHashes = isPlainObject(a.pageHashes) ? a.pageHashes : {}
// Byte-fact args (Cycle 15 build-4, D-C / D-A): REQUIRED — absent is the args-guard error below;
// present-and-wrong-type (the map itself, or an entry for a listed page) is refused pre-dispatch,
// BY NAME (`pageLinks[<slug>]`, the convention_digests[<name>] grammar). Absent entries are not
// refused: a page with no entry is computed anyway and named on a denominated cap in the reduce.
if (a.pageLinks !== undefined && !isPlainObject(a.pageLinks)) wrongTypeSlots.push({ slot: 'pageLinks', got: typeName(a.pageLinks), expected: 'plain object' })
if (a.summaryLengths !== undefined && !isPlainObject(a.summaryLengths)) wrongTypeSlots.push({ slot: 'summaryLengths', got: typeName(a.summaryLengths), expected: 'plain object' })
const pageLinks = isPlainObject(a.pageLinks) ? a.pageLinks : {}
const summaryLengths = isPlainObject(a.summaryLengths) ? a.summaryLengths : {}
for (const p of pages) {
  const slug = p && p.slug
  if (slug === undefined) continue
  const l = pageLinks[slug]
  if (l !== undefined && !Array.isArray(l)) wrongTypeSlots.push({ slot: `pageLinks[${slug}]`, got: typeName(l), expected: 'array' })
  const n = summaryLengths[slug]
  if (n !== undefined && !(Number.isInteger(n) && n >= 0)) wrongTypeSlots.push({ slot: `summaryLengths[${slug}]`, got: typeName(n), expected: 'integer' })
}
const cachedScans = Array.isArray(a.cachedScans) ? a.cachedScans : []
const rulesetComponents = isPlainObject(a.rulesetComponents) ? a.rulesetComponents : {}
const budgetFloor = a.budgetFloor || 40_000
// Cluster cap scales with the wiki size — a fixed 12 sat one below the 13 natural clusters on the
// live wiki and falsely tripped the coverage cap every run. Floor of 12 holds for small wikis. (#3 §6)
const clusterCap = a.clusterCap || Math.max(12, Math.ceil(pages.length / 4))
// Model tiering — the page scanners are pure structured extraction (the bulk of the spend); a cheap
// model is sufficient and is where the ~10x cost win lives. Index + cluster passes do light reasoning. (#3 §2)
const pairCap = Number.isInteger(a.pairCap) ? a.pairCap : 24 // 0 is a valid (test) value — no || fallback
// The extractor identity enters the cache key (A15-9 D-B), so a present override must be a
// non-empty string — String([...]) would otherwise compose a junk key term and dispatch anyway.
const scanModel = a.scanModel === undefined ? 'haiku' : a.scanModel
const indexModel = a.indexModel || 'sonnet'
const clusterModel = a.clusterModel || 'sonnet'

if (!pages.length || !indexPath || !conventionsPath || a.pageLinks === undefined || a.summaryLengths === undefined) {
  return { error: 'vlt-lint-full requires { pages:[{slug,path}], indexPath, conventionsPath, pageLinks:{slug:[string]}, summaryLengths:{slug:int} }. The vlt-lint SKILL discovers pages and passes live paths, and derives pageLinks/summaryLengths by scripts/lint-page-facts.py (references/full-scale.md step 1) — without them a fan-out cannot compute orphans, missing_targets, near_duplicates or the summary clauses of frontmatter_drift, and an empty slot would read as health.' }
}
if (typeof scanModel !== 'string' || scanModel.length === 0) {
  return { error: `vlt-lint-full requires scanModel to be a non-empty string when passed (got ${Array.isArray(a.scanModel) ? 'array' : typeof a.scanModel}) — it is the extractor identity in every per-page cache key; omit it for the default 'haiku'.` }
}

// ── Cost accounting (A11-11 direction 0) ─────────────────────────────────────
// Per-phase spend, computed in plain JS from facts already in hand — agents
// dispatched, model, workflow-composed prompt characters, and the runtime budget
// delta where a budget is set (null otherwise, prompt_chars the honest fallback
// estimate). No new agent asks, no fs reads, no schema change — facts, not
// verdicts. Attached to BOTH return shapes: the findings return and the
// status:'failed' near-total-shortfall return (a failed sweep's numbers are
// still measurement evidence).
const budgetSample = () => (budget.total ? budget.remaining() : null)
const costPhases = []
const costRow = (name, dispatched, model, promptChars, budgetBefore) => {
  const after = budgetSample()
  costPhases.push({
    phase: name,
    agents_dispatched: dispatched,
    model,
    prompt_chars: promptChars,
    tokens_spent: budget.total && budgetBefore != null && after != null ? budgetBefore - after : null,
  })
}
const costAccounting = () => ({
  phases: costPhases,
  pages_total: pages.length,
  budget_total: budget.total || null,
  budget_remaining_at_return: budgetSample(),
  note: 'prompt_chars is workflow-composed prompt text only — agent-side file reads (page + convention bytes) are not visible from JS; tokens_spent is the runtime budget delta where a budget was set',
})

const PAGE_SCAN = {
  type: 'object',
  additionalProperties: false,
  required: ['slug', 'available', 'title', 'frontmatter_defect', 'category', 'topic_is_list', 'summary', 'last_updated', 'verified_by', 'verified_at', 'review_after', 'name_callout_targets', 'sources_vs_prose'],
  properties: {
    slug: { type: 'string' },
    available: { type: 'boolean', description: 'false if the page file could not be read' },
    title: { type: 'string', description: "the page's frontmatter title value verbatim (empty if absent)" },
    created: { type: 'string', description: "the page's frontmatter created date (empty if absent)" },
    last_updated: { type: 'string', description: "the page's frontmatter last_updated (empty if absent)" },
    verified_by: { type: 'string', description: "the frontmatter verified_by value verbatim (empty if absent)" },
    verified_at: { type: 'string', description: "the frontmatter verified_at value verbatim (empty if absent)" },
    review_after: { type: 'string', description: "the frontmatter review_after date verbatim (empty if absent)" },
    frontmatter_defect: { type: 'string', enum: ['none', 'missing_required', 'malformed_block', 'unclassified'], description: 'none | missing_required (keys in _fields) | malformed_block (absent/unparseable) | unclassified (_detail)' },
    category: { type: 'string', description: "the frontmatter category: value verbatim (empty if missing)" },
    topic_is_list: { type: 'boolean', description: 'true if topic: is a YAML list; false if a delimited string or missing' },
    summary: { type: 'string', description: 'the frontmatter summary: value verbatim (empty if absent)' },
    frontmatter_defect_fields: { type: 'array', items: { type: 'string' }, description: 'bare key names, one per entry; else empty' },
    frontmatter_defect_detail: { type: 'string', description: 'the break in words; else empty' },
    sources_vs_prose: { type: 'string', enum: ['match', 'diverge_prose_gap', 'diverge_frontmatter_gap', 'diverge_unclassified', 'no_prose_section'], description: 'GAP B verdict — apply the prompt Gap B rule, per write-verification@5' },
    sources_vs_prose_detail: { type: 'string', description: 'the diverging entries; else empty' },
    stale_unmarked: { type: 'array', items: { type: 'string' }, description: 'time-bound claims past shelf life lacking a [!stale] marker' },
    within_page_contradictions: { type: 'array', items: { type: 'string' }, description: 'incompatible claims inside this one page' },
    unmarked_supersession: { type: 'array', items: { type: 'string' }, description: 'silently-updated/conflicting claims lacking a [!superseded]/[!stale] callout, or consensus claims lacking citations. A missing or stale attestation is NEVER an unmarked supersession (per write-verification@5 Scope rule).' },
    thin: { type: 'boolean', description: 'few claims, no connections, single source — a merge/stub candidate' },
    name_callout_targets: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['target', 'name'], properties: {
      target: { type: 'string', description: "the callout's [[wikilink]] target, raw inner text verbatim; do not normalize" },
      name: { type: 'string', description: 'the proper noun the callout questions' },
    } }, description: 'one entry per callout on this page questioning a proper noun against another named wiki page; empty when the page carries none' },
  },
}

const INDEX_SCAN = {
  type: 'object',
  additionalProperties: false,
  required: ['drift', 'malformed', 'h2_headings'],
  properties: {
    malformed: { type: 'boolean', description: "true if the index's own structure is broken per wiki-index.md" },
    drift: { type: 'array', items: { type: 'string' }, description: 'index problems: a page missing from the index, a listed page that does not exist, a miscategorized row, or a malformed entry under the Stubs section. The index is a structural map — it carries NO descriptions, source counts, or dates, so do not check those.' },
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

// Merged-on-read (B7-6): a convention is the base file PLUS its overlay, merged on read
// (vault-operating-contract.md, Convention overlays). When the caller says an overlay
// exists, the scanner reads base + overlay together — mirroring the vlt-lint SKILL's own
// inline reads ("read each together with its {overlays}/{name}.overlay.md if present,
// honoring the overlay's appended rules").
// The conventions the page scanner reads — SINGLE-HOMED here (A15-9 d1, roundtable A4). Two
// consumers, no third statement: pageScanPrompt's read clause below, and the three-way slot loop /
// composeRulesetFingerprint (the cache key's ruleset half requires exactly these names, by name).
// Adding an ask that reads a fourth convention adds it HERE and to the pins in the header (R4).
const SCANNER_CONVENTIONS = ['frontmatter', 'wiki-supersession', 'write-verification']
const convRead = (name) =>
  overlaysPath && overlayNames.includes(name)
    ? `${conventionsPath}/${name}.md together with its overlay ${overlaysPath}/${name}.overlay.md, honoring the overlay's appended rules (the convention is the base file plus its overlay, merged on read)`
    : `${conventionsPath}/${name}.md`

const pageScanPrompt = (p) =>
  `You are a wiki-lint page scanner. Read the wiki page at the LIVE path ${p.path} (slug "${p.slug}"). Read the conventions you judge against: ${SCANNER_CONVENTIONS.map((n) => convRead(n)).join('; ')} (read once, apply per page; judge the frontmatter defect verdict and the sources-vs-prose comparison against the MERGED rules wherever an overlay is named). When comparing frontmatter sources: entries against the prose Sources section (Gap B), normalize both sides first per frontmatter@14 rule 4 — strip surrounding quotes and [[ ]], strip a trailing .md, compare on the vault-relative path — so a wikilink-form entry and its bare-path twin compare equal. A mixed state — wikilink-form and legacy bare-path sources: entries on one page or across pages — is conformant and never a finding: existing bare-path entries stay legal and there is no backfill sweep (per frontmatter@14 rule 4, coexistence posture). For the sources-vs-prose comparison (Gap B), report sources_vs_prose: 'no_prose_section' when the page carries no prose ## Sources section — such a page is conformant (per write-verification@5, the wiki-page tier-1 item: frontmatter is the source of truth); where both exist and an entry in one is not traceable in the other, report the DIRECTION: 'diverge_prose_gap' when every divergent entry is one frontmatter carries and the prose section lacks; 'diverge_frontmatter_gap' when every divergent entry is one the prose section cites and frontmatter lacks; 'diverge_unclassified' when both kinds are present OR you cannot tell which side is missing the entry — that is the safe answer and it is flagged for a human, never auto-fixed, so never guess a direction; otherwise 'match'. A callout is only the Obsidian > [!type] blockquote form (per wiki-supersession@2): a supersession/staleness note written as a bullet, heading, or plain prose is NOT a marker — the claim it covers is still an unmarked supersession — and a bullet or heading questioning a name is NOT a name-verification callout (it yields no name_callout_targets entry). ` +
  `Return ONLY findings about THIS page, and return EVERY field the schema requires — populated, or an empty string / empty array where the page genuinely carries nothing. The schema's field descriptions are the field contract; follow them exactly. Extract verbatim: do not normalize — a name-verification callout's [[wikilink]] target keeps any |alias, #anchor, or path prefix intact. Do NOT report the page's outbound links: the link set is derived from the page's own bytes downstream and is never asked of you. Do not assess other pages — cross-page checks happen later. ` +
  `The frontmatter verdict is STRUCTURED, and it is three fields, not prose. frontmatter_defect is exactly one of: 'none' — the frontmatter block is present, parses, and satisfies the wiki-page schema; 'missing_required' — the block parses but one or more schema keys are absent, and you list EXACTLY those keys in frontmatter_defect_fields; 'malformed_block' — the frontmatter block is absent entirely, or its delimiters/YAML cannot be parsed at all; 'unclassified' — a genuine break that fits none of the above, with the words in frontmatter_defect_detail. Never force a break into a member that fits badly — 'unclassified' exists precisely so an unforeseen break is reported honestly rather than mis-filed, and it is never discarded downstream. frontmatter_defect_fields carries BARE frontmatter key names only, one per entry — \`summary\`, not "missing summary field", never a sentence, never a phrase, never a rule citation. A rule citation, a justification, or any explanatory wording belongs in frontmatter_defect_detail and NEVER in frontmatter_defect_fields. When frontmatter_defect is 'none', frontmatter_defect_fields is empty and frontmatter_defect_detail is empty. The summary's LENGTH is never a frontmatter defect of any kind — it is measured downstream from the page's own bytes (per frontmatter@14, the 160-character limit); never report a length complaint in frontmatter_defect, frontmatter_defect_fields, or frontmatter_defect_detail.`

// The scan-surface fingerprint (A10). Any edit to the prompt's invariant half or to
// PAGE_SCAN changes it, so a sidecar written under the old surface cannot be reused —
// build-1 rewrote both in this very release, which is why this exists. The variable head
// (${p.path}/${p.slug}) is stripped by building the canonical string from empty fields, so
// the value is page-independent. No crypto import exists here (and none is needed: this
// half only has to change whenever the text changes) — the strong digest is the SKILL's.
const fnv1a = (str) => {
  let h = 0x811c9dc5
  for (let i = 0; i < str.length; i++) {
    h ^= str.charCodeAt(i)
    h = (h + ((h << 1) + (h << 4) + (h << 7) + (h << 8) + (h << 24))) >>> 0
  }
  return h.toString(16).padStart(8, '0')
}
const canonicalScan = pageScanPrompt({ path: '', slug: '' }) + ' ' + JSON.stringify(PAGE_SCAN)
const scanFingerprint = fnv1a(canonicalScan) + fnv1a(canonicalScan.split('').reverse().join('')) + canonicalScan.length.toString(16)

// The ruleset half — COMPOSED HERE, from the SKILL's named component slots (A14-8, Q6.2).
// Why the composition is here and the component digests are not: this script has no
// filesystem access (see the header), so the SKILL must compute the digests; but a
// composition stated in prose for the SKILL to execute is exactly the defect A14-8 names —
// one contract, two implementations, no enforcement point where they meet. So the SKILL
// supplies INPUTS and this file supplies the ALGORITHM, once. The inputs are FACTS, NOT
// VERDICTS (A15-9, D-B): a cached record is what ONE scanner returned from ONE page under ONE
// prompt + schema (scanFingerprint) reading EXACTLY the SCANNER_CONVENTIONS — so the ruleset
// half is the resolved scanModel (the extractor identity) plus those three conventions' merged
// digests, and nothing else. The version string, the pin vector and checks.md left the key: none is
// an input to any scanner, and the reduce re-runs over cached facts every sweep, so a release
// that moves none of the three inputs leaves every record reusable (a record reused under a
// moved SCANNER-READ rule would be a false clean — D4 — and still cannot happen). The canonical
// order is code, never prose: scanModel, then every required convention digest as `name=digest`
// with names sorted lexicographically — joined with '|'. A caller passing the same components
// in a different key order composes the identical value; names outside SCANNER_CONVENTIONS
// never enter it (they are logged, once). The digest itself is the same fnv1a-pair-plus-length
// construction scanFingerprint uses: no crypto import exists here and none is needed — this
// half only has to change whenever its inputs change, and the strong digest is the SKILL's
// (full-scale.md step 2 names the instrument).
const RULESET_SLOTS = ['convention_digests']
// Three-way, at two levels (A15-10, D2 — build-3): each slot, and each required name inside it,
// is ABSENT (key not present), EMPTY (`{}` / `''`) or PRESENT BUT OF THE WRONG TYPE — three lists,
// never one word. Absent and empty are cold caps named under their own word; wrong type is a
// pre-dispatch REFUSAL (below the cache reader), because a value the SKILL rendered in a form
// this script cannot use is a rendering error, not an absence, and rendering it as an absence is
// exactly what sent 146 pages cold under an honest-looking reason. Reported BY NAME
// (`convention_digests[write-verification]`), never as the bare slot, except when the map itself
// is absent, empty or mis-typed (then the name loop is skipped — there is no map to walk).
const rulesetSlotsAbsent = []
const rulesetSlotsEmpty = []
const rulesetSlotsWrongType = [] // {slot, got, expected}
// A mis-typed `rulesetComponents` itself (recorded at intake) is refused as such — the loop is
// skipped, so nothing derived from its coerced `{}` default is ever rendered as an absence.
const rulesetComponentsWrongTyped = wrongTypeSlots.some((w) => w.slot === 'rulesetComponents')
for (const k of rulesetComponentsWrongTyped ? [] : RULESET_SLOTS) {
  const v = rulesetComponents[k]
  if (v === undefined) { rulesetSlotsAbsent.push(k); continue }
  if (!isPlainObject(v)) { rulesetSlotsWrongType.push({ slot: k, got: typeName(v), expected: 'plain object' }); continue }
  if (Object.keys(v).length === 0) { rulesetSlotsEmpty.push(k); continue }
  for (const n of SCANNER_CONVENTIONS) {
    const d = v[n]
    if (d === undefined) rulesetSlotsAbsent.push(`${k}[${n}]`)
    else if (typeof d !== 'string') rulesetSlotsWrongType.push({ slot: `${k}[${n}]`, got: typeName(d), expected: 'string' })
    else if (d.length === 0) rulesetSlotsEmpty.push(`${k}[${n}]`)
  }
}
// Completeness is enforced, not assumed: any required name absent, empty or mis-typed ⇒ '' ⇒
// reusable() is false for every page ⇒ nothing is reused (D4 holds on a refused run too — moot,
// since it never dispatches). Absent/empty carry a named cap (the same loud-degrade posture the
// overlay args carry below).
const composeRulesetFingerprint = () => {
  if (rulesetComponentsWrongTyped || rulesetSlotsAbsent.length || rulesetSlotsEmpty.length || rulesetSlotsWrongType.length) return ''
  const cd = rulesetComponents.convention_digests
  const extras = Object.keys(cd).filter((n) => !SCANNER_CONVENTIONS.includes(n))
  if (extras.length) log(`rulesetComponents.convention_digests names conventions the page scanner never reads — ignored for the cache key: [${extras.join(', ')}] (the key carries exactly ${SCANNER_CONVENTIONS.join(', ')})`)
  const pairs = [...SCANNER_CONVENTIONS].sort().map((n) => `${n}=${cd[n]}`)
  const canonical = [scanModel, ...pairs].join('|')
  return fnv1a(canonical) + fnv1a(canonical.split('').reverse().join('')) + canonical.length.toString(16)
}
const rulesetFingerprint = composeRulesetFingerprint()
// The ruleset half's inputs as composed THIS run — a fact returned as `cache_components` and
// stored beside the sidecar's informational `fingerprint` so the SKILL can name which convention
// moved on a cold run. Never a source of any reuse decision (lint-cache.py's docstring rule).
const cacheComponents = {
  scan_model: scanModel,
  convention_digests: Object.fromEntries(SCANNER_CONVENTIONS.map((n) => {
    const cd = rulesetComponents.convention_digests
    return [n, cd && typeof cd === 'object' && typeof cd[n] === 'string' ? cd[n] : '']
  })),
}

// The composite per-page key, and the split of the page list (A11-11 direction 2).
// A record is reusable iff its recorded key equals the key recomputed from THIS run's
// inputs — the page's own digest crossed with the two fingerprint halves. Nothing in the
// sidecar is ever a SOURCE of that comparison, only its object: a corrupt, forged or stale
// record cannot serve a stale finding, it can only cause a cache miss. (Brief disposition 3
// — this is the recorded-state branch of the contract's derive-first rule, not the
// inferred-from-residue branch.)
// The key's three terms are unchanged in shape (A4); only the THIRD term's provenance moved —
// it is COMPOSED here from the SKILL-supplied components above, so two conformant executors
// cannot disagree about it — and, since A15-9, its INPUTS are facts-not-verdicts (see above).
// scanFingerprint stays a term: it is workflow-internal by construction (the SKILL cannot
// compute it), and dropping it would make a sidecar written under one PAGE_SCAN reusable under
// another.
const runKey = (slug) => `${pageHashes[slug] || ''}|${scanFingerprint}|${rulesetFingerprint}`
const cacheBySlug = new Map(cachedScans.filter((c) => c && c.slug && c.key && c.scan).map((c) => [c.slug, c]))
// Miss attribution (A15-9 / A20): for every sidecar record that will NOT be reused, the FIRST of
// the three '|'-separated key terms that differs from this run's — page_bytes / scan_surface /
// ruleset — counted, so a cold run can say WHICH term moved rather than merely that one did.
// Page-bytes misses are churn, not cold; the SKILL renders the cold reason from the other two
// (plus the by-name diff of the sidecar's stored `components` against `cache_components`).
const KEY_TERMS = ['page_bytes', 'scan_surface', 'ruleset']
const cacheMissTerms = { page_bytes: 0, scan_surface: 0, ruleset: 0 }
for (const [slug, c] of cacheBySlug) {
  const now = runKey(slug)
  if (c.key === now) continue
  const had = String(c.key).split('|'), cur = now.split('|')
  const i = KEY_TERMS.findIndex((_, k) => had[k] !== cur[k])
  // A key of foreign arity whose first three terms all match is a ruleset-shaped miss (the
  // ruleset term is the one whose composition a release can reshape).
  cacheMissTerms[KEY_TERMS[i === -1 ? 2 : i]]++
}
// The enforcement point for full-scale.md step 2's standing mandate — "a missing, unparseable
// or schema-mismatched sidecar is a cold run, STATED IN THE REPORT, never a silent full sweep
// presented as a cached one" (A39). The mandate has existed since the cache shipped with
// nothing anywhere that could see it: in the field 146 flat records were passed in, the filter
// above discarded every one, and the report said only `cold`. These two numbers ship WITH each
// other — a bare rejected count is a cardinality with no referent.
const cacheRecordsRead = cachedScans.length
const cacheRejected = cacheRecordsRead - cacheBySlug.size
const reusable = (p) => !!(pageHashes[p.slug] && rulesetFingerprint &&
  cacheBySlug.get(p.slug) && cacheBySlug.get(p.slug).key === runKey(p.slug))
const toScan = pages.filter((p) => !reusable(p))
const reused = pages.filter(reusable)

const scans = []
// The FRESH half — records this run actually dispatched an agent for. `files_checked` is
// denominated on this (Gap B rule unchanged: scanned this run), and so are both fan-out
// guards below (brief dispositions 10 and 11) — the cache must never make up the numbers
// for agents that died.
const freshScans = []
const freshBySlug = new Map()
const coverageCaps = []
// Loud degrade (A14-8; three-way since build-3): an incomplete rulesetComponents object is a cold
// sweep with the absent and the empty names each NAMED under their own word — never a silent cold
// run whose cause has to be guessed from a miss count, and never one word for two cases. Wrong
// type is NOT a cap: it is the refusal below.
if (rulesetSlotsAbsent.length) {
  const m = `findings cache cold: rulesetComponents — absent [${rulesetSlotsAbsent.join(', ')}]; no page was reusable this run`
  coverageCaps.push(m)
  log(m)
}
if (rulesetSlotsEmpty.length) {
  const m = `findings cache cold: rulesetComponents — empty [${rulesetSlotsEmpty.join(', ')}]; no page was reusable this run`
  coverageCaps.push(m)
  log(m)
}
// Loud degrade (B7-6): an old caller passing no overlay args gets a base-only sweep with
// its cap on the record — never a silent base-only judgment.
if (!overlaysPath) {
  const m = 'no overlay args passed — pages were judged against base conventions only; overlay-compliant content may be falsely flagged'
  coverageCaps.push(m)
  log(m)
}
// The pre-dispatch refusal (A15-10, D2 ii/iii — build-3). A D2 slot (`rulesetComponents`, a
// `convention_digests` entry, `stubSlugs`) that arrived PRESENT BUT OF THE WRONG TYPE is the
// SKILL's own rendering error, and it is detectable here — after the cache reader (so the record
// counts are real) and before the fan-out loop (so no agent has been dispatched and
// cost_accounting says so). It rides the failed-run shape the near-total-shortfall guard returns
// below, field-for-field, so full-scale.md step 4's reader sees one shape: the SKILL persists a
// `…-lint-failed` record, applies nothing, resets no counter, and surfaces the directed `next:`.
// Never a coverage cap — the owner would otherwise still pay every agent to read it afterwards.
const wrongTyped = [...wrongTypeSlots, ...rulesetSlotsWrongType]
if (wrongTyped.length) {
  const reason = wrongTyped.map((w) => `slot rendered with the wrong type: ${w.slot} (got ${w.got}, expected ${w.expected})`).join('; ')
  const msg = `pre-dispatch refusal — ${reason}; no agent was dispatched, nothing was spent`
  log(msg)
  // Every phase renders at 0 dispatched — a refused run's cost row is a fact, not an absence.
  const at = budgetSample()
  costRow('Scan pages', 0, scanModel, 0, at)
  costRow('Index pass', 0, indexModel, 0, at)
  costRow('Cluster pass', 0, clusterModel, 0, at)
  costRow('Seeded-pair pass', 0, clusterModel, 0, at)
  return {
    status: 'failed',
    mode: 'full',
    reason,
    files_listed: pages.length,
    files_checked: 0,
    files_cached: 0,
    agent_failed: [],
    page_unreadable: [],
    coverage_caps: coverageCaps,
    cost_accounting: costAccounting(),
    cache_miss_terms: cacheMissTerms,
    cache_records_read: cacheRecordsRead,
    cache_rejected: cacheRejected,
    next: `re-render ${[...new Set(wrongTyped.map((w) => (w.slot.startsWith('stubSlugs') ? 'stubSlugs' : w.slot.startsWith('pageLinks') ? 'pageLinks' : w.slot.startsWith('summaryLengths') ? 'summaryLengths' : 'rulesetComponents')))].join(' / ')} per references/full-scale.md step 2 / references/checks.md Missing targets / pageLinks and summaryLengths per references/full-scale.md step 1 (re-run scripts/lint-page-facts.py) and re-run — no agent was dispatched, nothing was spent`,
  }
}
// Reason-partitioned shortfall accounting (A10-16 Defect 2): a fan-out agent the harness
// rejected pre-read resolves to null (no catchable error — the v0.13.0 classifier-ceiling
// failure that silently dropped 145/146 pages read as a clean report). parallel() preserves
// position, so chunk[k] names the page for part[k]: a null is an AGENT-FAILED slug; an
// available:false result is a PAGE-UNREADABLE slug. Both are counted, never silently dropped.
const agentFailedSlugs = []
const pageUnreadableSlugs = []
let budgetCapped = false
const CHUNK = 16
const scanBudgetAt = budgetSample() // cost accounting: phase-start budget sample
let scanDispatched = 0
let scanPromptChars = 0
for (let i = 0; i < toScan.length; i += CHUNK) {
  if (budget.total && budget.remaining() < budgetFloor) {
    const msg = `budget guard: scanned ${freshScans.length}/${toScan.length} pages needing a scan (${reused.length} reused from the findings cache) before the remaining budget fell below ${budgetFloor} — the rest were NOT checked`
    coverageCaps.push(msg)
    log(msg)
    budgetCapped = true
    break
  }
  const chunk = toScan.slice(i, i + CHUNK)
  const chunkPrompts = chunk.map((p) => pageScanPrompt(p))
  scanDispatched += chunk.length
  for (const t of chunkPrompts) scanPromptChars += t.length
  const part = await parallel(chunk.map((p, k) => () => agent(chunkPrompts[k], { label: `scan:${p.slug}`, phase: 'Scan pages', schema: PAGE_SCAN, model: scanModel })))
  for (let k = 0; k < chunk.length; k++) {
    const r = part[k]
    if (!r) agentFailedSlugs.push(chunk[k].slug)
    else if (r.available === false) pageUnreadableSlugs.push(chunk[k].slug)
    else { freshScans.push(r); freshBySlug.set(chunk[k].slug, r) }
  }
  log(`scanned ${freshScans.length}/${toScan.length} pages (${reused.length} reused from the findings cache)`)
}
costRow('Scan pages', scanDispatched, scanModel, scanPromptChars, scanBudgetAt)
// Loud degrade at the reduce boundary (A10-16 Defect 2): a dead agent adds a loud cap, never
// vanishes. When the sweep scanned fewer pages than listed for any reason OTHER than the budget
// guard already having capped, push a coverage cap naming the count + reason partition + the
// failed slugs — mirroring the overlay/budget-guard cap posture above.
if (!budgetCapped && freshScans.length < toScan.length) {
  const parts = []
  if (agentFailedSlugs.length) parts.push(`${agentFailedSlugs.length} agent-rejected [${agentFailedSlugs.join(', ')}]`)
  if (pageUnreadableSlugs.length) parts.push(`${pageUnreadableSlugs.length} page-unreadable [${pageUnreadableSlugs.join(', ')}]`)
  const m = `partial sweep: scanned ${freshScans.length}/${toScan.length} pages needing a scan (${reused.length} reused from the findings cache, ${pages.length} listed) — ${parts.join(', ')}; the rest were NOT checked`
  coverageCaps.push(m)
  log(m)
}

// Near-total shortfall → error, never a findings report (A10-16 Defect 2, disposition 3):
// below MAJORITY coverage the cross-page reduce is dominated by absent pages and any "clean"
// bucket is far more likely shortfall than health (the exact 0.7%-coverage field failure). The
// guard is freshScans.length === 0 (the hard sub-case) OR freshScans.length < ceil(toScan.length / 2).
// The error shape carries status:'failed' and NO findings buckets — distinct from a report, mirroring
// the args-guard error convention above. Owner-adjustable threshold.
// It measures the DISPATCHED population, not the corpus (brief disposition 11): with cached
// records spliced in, a corpus-denominated floor would pass on a run where every dispatched
// agent died, because the cache made up the numbers. A fully-cached run has no fan-out and
// therefore no fan-out shortfall — the guard is skipped when toScan is empty.
if (toScan.length > 0 && (freshScans.length === 0 || freshScans.length < Math.ceil(toScan.length / 2))) {
  const msg = `near-total fan-out shortfall: only ${freshScans.length}/${toScan.length} pages needing a scan were scanned (below the majority-coverage floor; ${reused.length} of ${pages.length} listed pages were reused from the findings cache) — a findings report over this set cannot be honest. The most likely cause is a stale vault-local workflow copy; re-run after confirming the workflow copy is current.`
  log(msg)
  return {
    status: 'failed',
    mode: 'full',
    reason: msg,
    files_listed: pages.length,
    files_checked: freshScans.length,
    files_cached: reused.length,
    agent_failed: agentFailedSlugs,
    page_unreadable: pageUnreadableSlugs,
    coverage_caps: coverageCaps,
    cost_accounting: costAccounting(), // A11-11 direction 0 — a failed sweep's numbers are still measurement evidence
    cache_miss_terms: cacheMissTerms, // A15-9 — likewise: why the cache missed is evidence even when the sweep failed
    cache_records_read: cacheRecordsRead,
    cache_rejected: cacheRejected,
    next: 're-run after confirming the vault-local workflow copy is current (vlt-upgrade); if the shortfall persists at full coverage, file it',
  }
}

// The corpus the whole-corpus reduce runs over: fresh scans and reused cached FACTS
// together, assembled in page order so a run's findings never depend on which pages
// happened to be cached. The reduce, the index pass and the cluster/pair passes all still
// run over the WHOLE corpus every run — the cache buys recomputation, never coverage.
const recordOf = (p) => freshBySlug.get(p.slug) || (reusable(p) ? cacheBySlug.get(p.slug).scan : null)
for (const p of pages) {
  const rec = recordOf(p)
  if (rec) scans.push(rec)
}

// ── JS reduce: the link graph (free — no agents) ─────────────────────────────
phase('Reduce + cross-page')

// The link sets, from BYTES (Cycle 15 build-4, D-C): the SKILL's script
// (vlt-lint/scripts/lint-page-facts.py) extracts every [[ ]] inner text RAW; every comparison
// below runs on the normal form computed HERE (B5-3's seam, re-nouned) — never on a scanner's
// link return, which this workflow no longer asks for. Empty-after-normalization targets (a bare
// [[#anchor]]) are dropped, not compared; duplicates are set here. Computed once, over `pages`
// (filesystem truth, the A10-17 posture), never over `scans`.
const linksOf = new Map(pages.map((p) => [p.slug, [...new Set((Array.isArray(pageLinks[p.slug]) ? pageLinks[p.slug] : []).map(normalizeTarget).filter(Boolean))]]))
const links = (slug) => linksOf.get(slug) || []
const nslug = (s) => normalizeTarget(s.slug)
// A page with no entry (the script's `unreadable` list, or a hand-composed map) is computed
// anyway and NAMED — a denominated cap, never a suppressed slot (build-3's split applied to this
// build's own slots; suppressing the slots was DA7's shape, retired with its cause).
const noLinkSet = pages.filter((p) => !Array.isArray(pageLinks[p.slug])).map((p) => p.slug)
if (noLinkSet.length) {
  const m = `pageLinks: ${noLinkSet.length} of ${pages.length} pages carry no link set — [${noLinkSet.join(', ')}]; an orphan whose only inbound link would sit on one of these is not visible, and their own missing targets were not computed`
  coverageCaps.push(m)
  log(m)
}
const noSummaryLength = pages.filter((p) => !Number.isInteger(summaryLengths[p.slug])).map((p) => p.slug)
if (noSummaryLength.length) {
  const m = `summaryLengths: ${noSummaryLength.length} of ${pages.length} pages carry no summary length — [${noSummaryLength.join(', ')}]; the summary clauses of frontmatter_drift were rendered for ${pages.length - noSummaryLength.length} pages`
  coverageCaps.push(m)
  log(m)
}

// The single-writer clause's read-back (Cycle 15 build-4, disposition 5 / A12): the ONE
// scanner-returned value the reduce still consumes that has a byte-fact to read against is a
// name-verification callout's target — the seed of the entity-pair pass. A callout's target must
// be among the page's own links; a returned target that is not is a fabricated seed. The seed is
// dropped, and the page's record is EXCLUDED from cacheRecords below — a record whose returned
// target is invented is one the same scanner can be served from the cache next sweep,
// permanently (A15-4's amplification), so it is re-derived instead (build-2's eviction posture,
// applied at derivation time). Keyed by the record's slug, which every path below (the pair
// prompt's path lookup, the cluster labels) already reads as the page's slug. Denominated on
// every completing run as the top-level fact `scanner_return_rejected` (T = scans.length); the
// cap renders only when N > 0 — a `0 of T` line in the caps list would read as a health claim.
const scannerRejected = new Map() // slug -> reason
const calloutsOf = new Map() // slug -> the callouts that passed the read-back
for (const s of scans) {
  const kept = []
  for (const t of s.name_callout_targets || []) {
    const target = t && normalizeTarget(t.target) // raw wikilink text in, normal form compared (B5-3)
    if (!target) continue
    if (!links(s.slug).includes(target)) { scannerRejected.set(s.slug, `callout target '${t.target}' is not among the page's links`); continue }
    kept.push({ target, name: t.name })
  }
  calloutsOf.set(s.slug, kept)
}
if (scannerRejected.size) {
  const m = `scanner_return_rejected: ${scannerRejected.size} of ${scans.length} records — ${[...scannerRejected].map(([slug, why]) => `${slug}: ${why}`).join('; ')}; each record was not cached and is re-derived next sweep`
  coverageCaps.push(m)
  log(m)
}

// The WRITE-READY records the SKILL persists (A14-8, A6). Built here, after the corpus is
// assembled and normalized, so the stored payload is exactly the payload the reduce
// adjudicated — one site, no snapshot to keep in sync. One record per page adjudicated this
// run, FRESH AND REUSED: the shipped spec used to hand back fresh records only and ask the
// SKILL to re-add "the reused records that are still valid", where validity is a key match
// against scanFingerprint — a workflow-internal value the SKILL structurally cannot compute.
// The SKILL is never asked to re-derive reusability. It writes what it is handed.
//   - slug is p.slug, the SKILL-SUPPLIED slug from the page list, never the agent-returned
//     s.slug: the key's first term is pageHashes[p.slug], and keying a record by an
//     agent-returned string would let a scanner's typo poison a page's cache line.
//   - key is runKey(p.slug) for every record. For a reused page the recomputed key is by
//     definition equal to the reused record's key — that is what made it reusable — so one
//     code path serves both halves and there is no fresh/reused branch to keep in agreement.
//   - a record is emitted only when pageHashes[p.slug] and rulesetFingerprint are BOTH
//     non-empty; otherwise the key is degenerate (`|scanFp|`) and storing it is storing junk
//     that can never hit. A cold run with no components rewrites the sidecar with records: [].
//   - the record carries no link list (Cycle 15 build-4): links come from bytes every run, so
//     no cached fact depends on pageLinks / summaryLengths and neither enters the key (D4).
//   - a record whose returned callout target failed the read-back above (scannerRejected) is
//     SKIPPED: a fabricated return must not be served from the cache next sweep.
const cacheRecords = []
if (rulesetFingerprint) {
  for (const p of pages) {
    const rec = recordOf(p)
    if (rec && pageHashes[p.slug] && !scannerRejected.has(p.slug)) cacheRecords.push({ slug: p.slug, key: runKey(p.slug), scan: rec })
  }
}

// Filesystem-truth page set (A10-17 root fix): valid-target space is every page that
// EXISTS on disk (the input page list the SKILL globbed), not only pages whose agent scan
// survived. A wikilink to a real page that merely failed to scan is no longer a fabricated
// missing-target. Inbound-derived slots are computed from the SKILL-derived link sets and are
// complete regardless of scan coverage (Cycle 15 build-4, D-C).
const pageSlugSet = new Set(pages.map((p) => normalizeTarget(p.slug)))
// Inbound over every page on disk, self-links excluded: a page's link to itself is not an
// inbound link (checks.md, Orphan pages: "no inbound links from OTHER wiki pages").
const inbound = new Map()
for (const p of pages) {
  const self = normalizeTarget(p.slug)
  for (const l of links(p.slug)) if (l !== self) inbound.set(l, (inbound.get(l) || 0) + 1)
}
// The population is every page on disk, not every page that scanned. (The DA7 suppression —
// orphans / near-duplicates emitted empty under partial shortfall — retired with its cause: the
// inbound map no longer depends on what scanned.)
const orphans = pages.filter((p) => !(inbound.get(normalizeTarget(p.slug)) > 0)).map((p) => p.slug)
// A [[link]] target that resolves to a wiki slug OR a known cross-layer note (research / agent-zone,
// supplied by the SKILL which has filesystem access) is valid; only a target resolving to NOTHING
// anywhere is a missing target. Without crossLayer, valid cross-layer links false-positive en masse. (#3 §4)
// A target registered under the index's Stubs section as `wiki-index.md` states it (the SKILL locates and
// parses it — `checks.md` Missing targets) is a RECORDED gap, not a missing target (B5-3).
// The value compared is the page's own bytes — a same-page anchor (A15-3) or a substituted noun
// (A15-4) cannot reach this slot through a scanner.
const crossLayer = new Set(crossLayerSlugs)
const stubs = new Set(stubSlugs)
const missing_targets = []
for (const p of pages) for (const l of links(p.slug)) if (!pageSlugSet.has(l) && !crossLayer.has(l) && !stubs.has(l)) missing_targets.push(`${p.slug} → ${l}`)

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
const linkSets = scans.map((s) => new Set(links(s.slug).filter((l) => !hubs.has(l))))
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
const indexPrompt =
  `You are a wiki-index linter. Read the live index at ${indexPath} and judge it against ${convRead('wiki-index')}. The wiki currently contains exactly these page slugs: ${[...pageSlugSet].join(', ')}. ` +
  `The index is a STRUCTURAL MAP — it carries no descriptions, source counts, or dates; do not check those. Report (1) index drift: pages missing from the index, listed pages that don't exist, miscategorized rows, malformed entries under the Stubs section as the convention states it; and (2) h2_headings: every H2 heading in the index, verbatim and in order — the heading text exactly as written, with only the leading '## ' marker removed. Do not judge page categories against the headings; that comparison is computed downstream.`
const indexBudgetAt = budgetSample()
const indexScan = await agent(indexPrompt, { label: 'index-drift', phase: 'Reduce + cross-page', schema: INDEX_SCAN, model: indexModel })
costRow('Index pass', 1, indexModel, indexPrompt.length, indexBudgetAt)

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
    const sLinks = new Set(links(s.slug))
    let shared = 0
    for (const l of links(t.slug)) if (sLinks.has(l) || l === nslug(s)) shared++
    if (shared >= 2 || links(t.slug).includes(nslug(s))) { group.push(t); clustered.add(t.slug) }
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

const clusterPrompt = (group) =>
  `You are a cross-page contradiction checker. These wiki pages share topic/links and may conflict. For each, read its LIVE path. Pages: ${group.map((g) => `${g.slug} (${pages.find((p) => p.slug === g.slug)?.path || '?'})`).join('; ')}. ` +
  `Find incompatible claims ACROSS these pages that lack a supersession/contradiction callout (unhandled). SEPARATELY, for disagreements that ARE already documented with a Contradictions section or callout, split them by the callout's recorded "**Disposition:**" line (per wiki-supersession@2): open -> documented_open, adjudicable -> documented_adjudicable. A documented disagreement whose callout carries NO Disposition line goes to documented_undispositioned — do NOT infer a disposition for it, and never guess it into open or adjudicable. A disagreement recorded only as a bullet, heading, or plain prose — not an Obsidian > [!type] callout — is NOT documented (per wiki-supersession@2); report it in cross_page_contradictions. ` +
  `ALSO report entity_collisions: the same proper noun recorded with incompatible attributes across two of these pages. PRECEDENCE — a conflict that is one name carrying incompatible attributes goes to entity_collisions and NOT to cross_page_contradictions; report it once, in one slot.`

const clusterBudgetAt = budgetSample()
const clusterPrompts = clustersToCheck.map((group) => clusterPrompt(group))
const clusterResults = (
  await parallel(
    clustersToCheck.map((group, k) => () =>
      agent(clusterPrompts[k], { label: 'contradict-cluster', phase: 'Reduce + cross-page', schema: CLUSTER_FINDINGS, model: clusterModel }),
    )
  )
).filter(Boolean)
costRow('Cluster pass', clustersToCheck.length, clusterModel, clusterPrompts.reduce((n, t) => n + t.length, 0), clusterBudgetAt)

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
// Seeds are the callouts that PASSED the read-back above (calloutsOf — targets already in the
// normal form); a fabricated target never seeds a pair.
for (const s of scans)
  for (const t of calloutsOf.get(s.slug) || []) {
    const target = t.target
    if (!pageSlugSet.has(target) || target === nslug(s)) continue
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

const pairPrompt = (pr) =>
  `You are a cross-page entity-collision checker. A name-verification callout marked these two wiki pages as a suspect pair over the proper noun "${pr.name}". Read BOTH at their LIVE paths: ${pr.a} (${pages.find((p) => p.slug === pr.a)?.path || '?'}); ${pr.b} (${pages.find((p) => p.slug === pr.b)?.path || '?'}). ` +
  `Judge the PAGES, not the callout: report entity_collisions — the same proper noun recorded with incompatible attributes across these two pages, as "page-a vs page-b: <name> — <attribute A> vs <attribute B>". PRECEDENCE — a conflict that is one name carrying incompatible attributes is an entity collision, never also a contradiction. Report nothing else; a marked pair whose pages do not actually collide returns empty (that is the pass working, not failing).`

const pairBudgetAt = budgetSample()
const pairPrompts = seededPairs.map((pr) => pairPrompt(pr))
const seededResults = (
  await parallel(
    seededPairs.map((pr, k) => () =>
      agent(pairPrompts[k], { label: `entity-pair:${pr.a}+${pr.b}`, phase: 'Reduce + cross-page', schema: PAIR_FINDINGS, model: clusterModel }),
    )
  )
).filter(Boolean)
costRow('Seeded-pair pass', seededPairs.length, clusterModel, pairPrompts.reduce((n, t) => n + t.length, 0), pairBudgetAt)
// Duplication with cluster findings is impossible by construction — only never-compared pairs run.
const seededCollisions = seededResults.flatMap((r) => (r.entity_collisions || []).map((f) => `${f} (callout-seeded)`))

// ── Assemble the structured report (vlt-lint Step 5 shape + Gap B slots) ─────
const flat = (key) => clusterResults.flatMap((c) => c[key] || [])
const collect = (key) => scans.flatMap((s) => (s[key] || []).map((v) => `${s.slug}: ${v}`))

// Verdicts computed from facts (B5-3, re-nouned by Cycle 15 build-4): the SKILL's script measures
// the parsed summary: scalar in characters from the page's bytes, JS does the verdict. The
// returned `summary` string is read by NO verdict (D-A) — the 160 here is the reduce's single
// home for the limit (checks.md / frontmatter.md are the rule's).
const summaryIssue = (slug) => {
  const n = summaryLengths[slug]
  if (!Number.isInteger(n)) return ''
  return n === 0 ? 'summary missing' : n > 160 ? `over-length (${n} chars)` : ''
}
const attested = (s) => !!(s.verified_by && s.verified_at) // present = both non-empty
const isStale = (s) => attested(s) && !!s.last_updated && s.last_updated > s.verified_at

// ── Reduce-side guards on the frontmatter-validity claim (A13-1 F1/F3/F5) ────────────────
// This reduce used to admit the scanner's boolean validity verdict and print its free-text
// issue slot unread. The PAGE_SCAN descriptions already forbid routing a missing attestation
// pair into a validity defect (see the frontmatter verdict's description) or an unmarked
// supersession (see unmarked_supersession), and that text is correct — but a schema description is an
// INSTRUCTION, not an enforcement point. Cycle 12 build-1 shipped exactly that prohibition
// and the very next two full sweeps reported the defect unchanged (20 entries hand-folded
// 2026-08-24, 6 on 2026-08-25). So what the reduce can decide WITHOUT page content, it now
// decides here, at the only point in the pipeline that can enforce it.
//
// Cycle 14 build-1 removed the parse rather than tuning it. The verdict now arrives
// STRUCTURED — frontmatter_defect (a closed enum), frontmatter_defect_fields (bare key names)
// and frontmatter_defect_detail — so the guards classify a machine-shaped value instead of
// interpreting prose. The prior mechanism was defeated in the field on 2026-08-26 by a scanner
// that merely CITED the rule it was applying: the quoted rule named real required keys and left
// leftover prose behind, defeating the closing conjunction on two independent legs at once.
// Nothing about the pages had changed; only the phrasing had. Set containment over a bare field
// list cannot be defeated by wording.
//
// The invariant, restated for the structured return: the guards only ever REFUSE an entry, they
// never add one, and they fire ONLY on frontmatter_defect === 'missing_required' whose field
// list is non-empty and lies WHOLLY inside a known set. 'unclassified' and 'malformed_block' are
// never refused by either disposition — 'unclassified' is the deliberate fail-OPEN escape, the
// member a scanner reaches for when a genuine break fits no other, and it always reports. So the
// failure direction remains over-reporting, never swallowing a genuine schema break — but that is
// now a property of the enum's escape member rather than of a filler word list, and it is TESTED
// by this build's acceptance (check 1's five controls) rather than asserted here.

// The page-required frontmatter set is the WIKI PAGE SCHEMA's ({conventions}/frontmatter.md,
// *Wiki pages* — base fields plus the wiki additions), deliberately NOT PAGE_SCAN.required
// above: that list governs what the AGENT must RETURN, not what a PAGE must CARRY. Conflating
// the two is the defect these sets guard — a scanner reported a page as invalid for `missing
// review_after` because review_after is a required RETURN value, while the page schema
// documents it as OPTIONAL (absence = evergreen). Where the two disagree, the page schema governs.
// Their live role since build-1: frontmatter_defect_fields is classified by set containment
// against them directly — that arithmetic IS the "and NOTHING else" half of both dispositions.
const PAGE_REQUIRED_FRONTMATTER = ['type', 'created', 'title', 'author', 'trust', 'last_updated', 'summary', 'category', 'topic', 'status', 'sources']
// Documented-optional page slots — absence is conformant, so "missing X" over one of these is
// not a finding at all (frontmatter@14, *Wiki pages*).
const PAGE_OPTIONAL_FRONTMATTER = ['review_after', 'source_type', 'review_note']
// Attestation is a self-marker under write-verification@5's Scope rule: its absence is never a
// validity defect and never an unmarked supersession. It is reported independently, from the
// same returned values, by unattested_write and attestation_census below.
const ATTESTATION_FRONTMATTER = ['verified_by', 'verified_at']

// The "and NOTHING else" test, as set arithmetic over the returned field list. A list qualifies
// only if it is non-empty, every entry is a bare key inside `set`, and no entry is a page-REQUIRED
// key. The last clause is what keeps a COMPOUND claim reporting ("malformed AND unattested" names
// a required key alongside the attestation pair, so it satisfies no containment) — and it is
// checked explicitly rather than inferred from the sets being disjoint today, because the three
// sets are hand-maintained: a later edit that promotes a key from optional to required without
// removing it from the optional list would otherwise silently teach a guard to swallow a genuine
// requirement. Anything not a bare key name (a sentence, a rule citation) is in no set and so
// qualifies nowhere — the defeat mechanism has no purchase here.
const whollyWithin = (fields, set) =>
  Array.isArray(fields) && fields.length > 0 &&
  fields.every((f) => typeof f === 'string' && set.includes(f)) &&
  !fields.some((f) => PAGE_REQUIRED_FRONTMATTER.includes(f))

// Disposition 1 — the attestation-only complaint. The test is "attestation and NOTHING else",
// never "mentions attestation": a page that is genuinely malformed AND also unattested must
// still be reported. The refused entry loses no fact — the page's unattestedness is already
// reported, computed independently from attested() over the same returned values, through
// unattested_write and attestation_census. Refusing here removes a DUPLICATE, not a finding.
const attestationOnlyComplaint = (s) =>
  s.frontmatter_defect === 'missing_required' && whollyWithin(s.frontmatter_defect_fields, ATTESTATION_FRONTMATTER)

// Disposition 2 — the invented requirement. "missing X" where X is documented-optional of a
// page is not a finding at all. Unlike disposition 1 this refusal carries NO fact anywhere —
// the requirement does not exist — so the entry is simply dropped. That asymmetry is
// deliberate: disposition 1 drops a duplicate, disposition 2 drops a non-event.
const inventedRequirement = (s) =>
  s.frontmatter_defect === 'missing_required' && whollyWithin(s.frontmatter_defect_fields, PAGE_OPTIONAL_FRONTMATTER)

const refusedFrontmatterClaim = (s) => attestationOnlyComplaint(s) || inventedRequirement(s)
// The finding line, rendered from the structured verdict rather than echoed from free text.
const frontmatterDefectText = (s) => {
  const fields = (Array.isArray(s.frontmatter_defect_fields) ? s.frontmatter_defect_fields : []).filter(Boolean)
  const detail = String(s.frontmatter_defect_detail || '').trim()
  if (s.frontmatter_defect === 'missing_required') {
    return `missing required frontmatter: ${fields.join(', ') || '(unnamed)'}${detail ? ` — ${detail}` : ''}`
  }
  if (s.frontmatter_defect === 'malformed_block') {
    return `frontmatter block absent or unparseable${detail ? ` — ${detail}` : ''}`
  }
  return `unclassified frontmatter defect${detail ? `: ${detail}` : ''}`
}
// The attestation census (E6/B10-11): the denominated wiki-wide line for the browsable
// wiki — pure arithmetic over the attestation values the scanners ALREADY return (no new
// ask, no PAGE_SCAN change). fresh = attested and current; stale = attested but
// last_updated > verified_at; unattested_pre_adoption = the unattested class the
// unattested_write slot lists (its created-vs-adoption informationality gate is the
// SKILL's, per checks.md). The three buckets partition pages_total.
const attestation_census = {
  pages_total: scans.length,
  fresh: scans.filter((s) => attested(s) && !isStale(s)).length,
  stale: scans.filter(isStale).length,
  unattested_pre_adoption: scans.filter((s) => !attested(s)).length,
}
// Transport normalization for the category↔H2 seam (A14-3). Both sides of that comparison are
// AGENT-returned — the page's category: and the index's H2 list — and an agent that HTML-escapes
// what it read returns `Energy &amp; Clean Tech` for a page carrying `Energy & Clean Tech`. On the
// page side that falsifies one page; on the INDEX side it falsifies every page in that category at
// once. Decoding is done at the comparison seam and NOT on intake into `scans`, so the stored scan
// record stays a byte-faithful verbatim agent return. Single pass by construction — the replace
// runs once over the source string, so `&amp;amp;` decodes to `&amp;` and never cascades to `&`.
const HTML_ENTITIES = { amp: '&', lt: '<', gt: '>', quot: '"', apos: "'", nbsp: ' ' }
const decodeEntities = (text) => String(text == null ? '' : text).replace(
  /&(?:#(\d+)|#[xX]([0-9a-fA-F]+)|([a-zA-Z]+));/g,
  (m, dec, hex, name) => {
    if (dec !== undefined) { const n = parseInt(dec, 10); return n >= 0 && n <= 0x10ffff ? String.fromCodePoint(n) : m }
    if (hex !== undefined) { const n = parseInt(hex, 16); return n >= 0 && n <= 0x10ffff ? String.fromCodePoint(n) : m }
    return Object.prototype.hasOwnProperty.call(HTML_ENTITIES, name) ? HTML_ENTITIES[name] : m
  },
)
const h2set = new Set((indexScan ? indexScan.h2_headings || [] : []).map(decodeEntities))

return {
  mode: 'full',
  // GAP B — files_checked counting rule: pages an agent actually SCANNED (not merely listed).
  files_checked: freshScans.length,
  // Reused under an unchanged key — ADJUDICATED this run, not scanned (A11-11 direction 2).
  files_cached: reused.length,
  files_listed: pages.length,
  fix_now: {
    orphans,
    missing_targets,
    index_drift: indexScan ? indexScan.drift : [],
    frontmatter_drift: scans
      .filter((s) => s.topic_is_list === false || summaryIssue(s.slug))
      .map((s) => `${s.slug}: ${[s.topic_is_list === false ? 'topic not a list' : '', summaryIssue(s.slug)].filter(Boolean).join('; ')}`),
    // UNGUARDED since Cycle 14 build-1, deliberately and on the record (owner ruling A-R1).
    // This site used to filter attestation-only complaints out of the class, because A13-1
    // Finding 1's sixth entry arrived here after the same prompt-side prohibition was ignored.
    // Once the predicate takes a STRUCTURED record instead of text it cannot be applied to a
    // free-text string at all — `unmarked_supersession` is an array of prose and Cycle 14 build-1
    // does not structure it (PAGE_SCAN closes at 3688 of a 3700 budget; there is no room, and
    // structuring it is the successor build's act). So the guard here is not removed by
    // preference, it becomes inexpressible, and the A13-1 exposure returns. The only remaining
    // depth for this class is the prompt-side prohibition in unmarked_supersession's own schema
    // description — which this cycle's own D1 rules is never an enforcement point, and which
    // :550-557 records was already field-refuted once. That is a live dissent (Victor, Amelia),
    // carried not resolved, and the exposure is MEASURED by acceptance check 7 rather than
    // assumed away: if that sweep finds an attestation-only entry here, the dissent becomes the
    // ruling and the successor build structures unmarked_supersession.
    // Interim posture until then: entries in this class are read as CANDIDATES, not verdicts —
    // an entry naming only verified_by/verified_at is refuted by the reader and no fix is
    // applied (the page's unattestedness is already reported independently by unattested_write
    // and attestation_census, computed from attested() over the same returned values), and the
    // hand-fold is recorded in the sweep's fixes_applied: so it stays countable.
    unmarked_supersessions: scans.flatMap((s) => (s.unmarked_supersession || []).map((v) => `${s.slug}: ${v}`)),
    // A14-4: the class routes on the scanner's RETURNED verdict, never on sources_vs_prose_detail's
    // free text (D1 — a schema description is not an enforcement point, and reduce-side prose
    // parsing is the debt build-1 retired). Only the prose-gap direction is auto-fixable: adding
    // the frontmatter entries the prose section omits deletes nothing. The other two directions
    // land in flag_for_human.sources_vs_prose_unresolved below.
    sources_vs_prose_mismatches: scans.filter((s) => s.sources_vs_prose === 'diverge_prose_gap').map((s) => `${s.slug}: ${s.sources_vs_prose_detail || 'frontmatter sources: entries missing from the prose Sources section'}`),
  },
  flag_for_human: {
    // Exact match against the extracted H2 set, computed here (B5-3) — the strict category↔H2
    // binding is case-sensitive by design: no trimming, no case folding. HTML entities are
    // decoded on BOTH sides first (A14-3) as a transport normalization — a scanner escaping what
    // it read is a transport artefact, not a category difference — and that is the ONLY latitude:
    // the comparison itself is no looser than before.
    category_no_match: indexScan
      ? scans.filter((s) => !h2set.has(decodeEntities(s.category))).map((s) => `${s.slug}: category '${decodeEntities(s.category) || '(none)'}' matches no H2`)
      : [],
    // Attestation findings (write-verification contract). PARA files are outside this workflow's
    // page set (it sweeps {wiki}) — para_missing_attestation is a structural slot the SKILL fills
    // from its own PARA jurisdiction scan; it is emitted here so the report shape is complete.
    para_missing_attestation: [],
    // ISO YYYY-MM-DD strings compare lexicographically — the same property review_due relies on.
    unattested_write: scans.filter((s) => !attested(s)).map((s) => `${s.slug} (created ${s.created || '?'})`),
    attestation_stale: scans.filter(isStale).map((s) => `${s.slug}: last_updated > verified_at`),
    // The census line rides beside the per-page slots — the scale-honesty layer above
    // them, never a replacement (checks.md, Attestation findings; report.md slot).
    attestation_census,
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
    // The scan's frontmatter verdict is no longer taken on faith: a 'missing_required' naming
    // ONLY the attestation pair, or ONLY documented-optional fields, is refused entry (see the
    // reduce-side guards above for why the prompt cannot enforce this and the reduce can).
    // 'unclassified' and 'malformed_block' are never refused — they always report.
    malformed_frontmatter: scans
      .filter((s) => s.frontmatter_defect && s.frontmatter_defect !== 'none' && !refusedFrontmatterClaim(s))
      .map((s) => `${s.slug}: ${frontmatterDefectText(s)}`),
    // A14-4, the flagged half: the prose section cites entries frontmatter lacks (reconciling it
    // mechanically would DELETE a real citation — a provenance judgment, never a serial fix), and
    // the unclassifiable divergence (the closed enum's escape member, A35). Both are reported,
    // neither is ever auto-applied.
    sources_vs_prose_unresolved: scans
      .filter((s) => s.sources_vs_prose === 'diverge_frontmatter_gap' || s.sources_vs_prose === 'diverge_unclassified')
      .map((s) => `${s.slug}: ${s.sources_vs_prose_detail || (s.sources_vs_prose === 'diverge_frontmatter_gap' ? 'prose Sources cites entries absent from frontmatter sources:' : 'divergence the scanner could not direction-classify')}`),
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
  // Cycle 15 build-4 (A12): the read-back's denominated count, returned on every completing run
  // — the SKILL renders it as the report's own `scanner_return_rejected:` line (report.md), so
  // `0 of T` is a measured zero on the report, never a cap that reads as health.
  scanner_return_rejected: { count: scannerRejected.size, of: scans.length, slugs: [...scannerRejected.keys()] },
  coverage_caps: coverageCaps,
  // A11-11 direction 0: the per-phase cost line, emitted on every completing run.
  cost_accounting: costAccounting(),
  // A11-11 direction 2: the fingerprint the reused records were adjudicated under (null on a
  // cold run), and the records the SKILL writes back to _agent/lint-cache.json. This
  // workflow stays READ-ONLY — it returns the records, the SKILL persists them. The records
  // are WRITE-READY (A14-8, A6): the SKILL persists them through vlt-lint's
  // scripts/lint-cache.py exactly as handed over, and never derives a key or a reusability
  // judgment itself.
  cache_fingerprint: rulesetFingerprint ? `${scanFingerprint}|${rulesetFingerprint}` : null,
  cache_records: cacheRecords,
  // Step 2's "stated in the report" mandate, given numbers (A39): how many records were read
  // from the sidecar, and how many of them the reader filter above discarded as
  // schema-mismatched. The denominator ships with the count, and report.md renders both on
  // BOTH branches including zero — `rejected 0` on a cold run means no records were read, not
  // that the cache is healthy.
  cache_records_read: cacheRecordsRead,
  cache_rejected: cacheRejected,
  // A15-9 / A20: WHY records missed, by first differing key term, and the ruleset half's inputs
  // as composed this run — both facts, never a reuse source. The SKILL stores cache_components
  // in the sidecar (`write --components`) and names the moved term(s) on a cold run.
  cache_miss_terms: cacheMissTerms,
  cache_components: cacheComponents,
}
