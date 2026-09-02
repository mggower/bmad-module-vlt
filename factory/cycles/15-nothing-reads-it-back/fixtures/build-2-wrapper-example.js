// Cycle 15 build-2 — the `full-scale.md` step 3 recipe's wrapper, with a two-page payload.
// In the field this file is WRITTEN BY THE DISCOVERY SCRIPT into a scratch directory outside
// the vault (`mktemp -d`) and invoked as `Workflow({ scriptPath: '<scratch>/vlt-lint-full-run.js' })`;
// on resume, `resumeFromRunId` rides with the SAME scriptPath and nothing is re-sent. The three
// elements the recipe requires: (1) the args EMBEDDED here, never passed as `args`; (2) invocation
// by `scriptPath`; (3) resume with the same `scriptPath`. Placeholder paths throughout.
export const meta = { name: 'vlt-lint-full-run', description: 'one-shot wrapper: the full-lint args embedded so no payload transits the caller', phases: [] }

const LINT_ARGS = {
  pages: [
    { slug: 'wiki-page-alpha', path: '/vault/wiki/wiki-page-alpha.md' },
    { slug: 'wiki-page-beta', path: '/vault/wiki/wiki-page-beta.md' },
  ],
  indexPath: '/vault/wiki/index.md',
  conventionsPath: '/vault/_agent/conventions',
  overlaysPath: '/vault/_agent/conventions/overlays',
  overlayNames: ['frontmatter'],
  crossLayerSlugs: ['2026-07-26-112444-espn-top-10-cornerbacks-2026', 'wiki.base', 'index'],
  stubSlugs: [],
  today: '2026-09-02',
  pageHashes: {
    'wiki-page-alpha': '0000000000000000000000000000000000000000000000000000000000000001',
    'wiki-page-beta': '0000000000000000000000000000000000000000000000000000000000000002',
  },
  cachedScans: [],
  rulesetComponents: {
    convention_digests: {
      frontmatter: '1111111111111111',
      'wiki-supersession': '2222222222222222',
      'write-verification': '3333333333333333',
    },
  },
}

return await workflow('vlt-lint-full', LINT_ARGS)
