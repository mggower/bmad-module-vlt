# Give vlt-lint-full a file-based args route — the inline payload costs the caller ~84KB of context before the first agent dispatches

origin: mggower/bmad-module-vlt#13

- **filed:** 2026-08-26 (GitHub issue opened 12:31:51Z via the vlt-feedback rail)
- **origin vault:** vlt-core · **module_version:** 0.16.0 · **rail_contract:** 1 · **kind:** candidate
- **materialized:** 2026-08-26 by the factory intake (github-intake)

---

### what_happened

`vlt-lint-full` has no filesystem access by design, so `vlt-lint` discovers the page list and passes it in as literal args. On a mature wiki that payload is large: `pages` (one `{slug, path}` per page, live absolute paths), `pageHashes` (a sha256 per page), and `crossLayerSlugs` (every walker-visible non-wiki link target in the vault).

On a ~146-page wiki, `crossLayerSlugs` alone was **1,849 entries**, and the composed args object was **~84KB**. Sending that inline through the `Workflow` tool's `args` parameter spends a large chunk of the calling session's context before a single scanner agent dispatches — and the caller pays it again on every resume, because `full-scale.md` step 3 requires re-passing the full args object on `resumeFromRunId`.

The cost scales with vault size on three axes at once (pages, page digests, cross-layer targets), so it gets worse exactly where the fan-out is most needed.

### evidence

Composed args for one full-mode sweep:

```
pages            146 entries  ({slug, path}, absolute paths)
pageHashes       146 entries  (sha256 each)
crossLayerSlugs  1849 entries
stubSlugs        6 entries
total            ~84KB serialized JSON
```

**Workaround that worked**, offered as a fix direction rather than a complaint: build the args object with a script that has filesystem access, write a thin wrapper workflow to disk that embeds it, and invoke by `scriptPath` instead of `args`:

```js
export const meta = { name: 'vlt-lint-full-run', description: '...', phases: [...] }

const LINT_ARGS = { /* the ~84KB object, written to disk by the discovery script */ }

return await workflow('vlt-lint-full', LINT_ARGS)
```

`Workflow({scriptPath: '<path>'})` then runs the sweep with the payload never entering the caller's context. This works today with no module change — it is undocumented, not unavailable.

Second, smaller observation in the same area: invoking the workflow by name with no args (`Workflow({name: 'vlt-lint-full'})`) fails instantly with

> vlt-lint-full requires { pages:[{slug,path}], indexPath, conventionsPath }. The vlt-lint SKILL discovers pages and passes live paths.

which is a correct and well-worded refusal, but it is the first thing anyone reaching for the workflow directly will hit, and it reads as a broken asset rather than as "you are holding it wrong." A pointer to the SKILL route in that message would close it.

### provenance_guess

**A guess.** `references/full-scale.md` step 1 (the discovery + derivation spec) and step 3 (the `workflow(...)` invocation contract, including the re-pass-on-resume rule) are where this lives. The workflow's own arg-parsing header block documents each key.

Two candidate fixes, not mutually exclusive:

1. **Document the wrapper-script route in `full-scale.md` step 3** as the recommended invocation at scale, with the resume implication stated (a `scriptPath` wrapper resumes without re-sending the payload, which also removes the step-3 re-pass footgun).
2. **Accept an args-file parameter** — e.g. `argsPath` pointing at a JSON file the runtime reads and injects — so the SKILL writes the payload once and passes a path. This is the cleaner fix if the runtime can read a file on the workflow's behalf; the workflow itself stays filesystem-free, which is the property the current design is protecting.

Option 1 costs a documentation edit and is available immediately. Option 2 needs runtime support and may be out of the module's control.

### kind

candidate

### origin_vault

vlt-core

### acceptance_vault

Any vault large enough to cross the ~30-page fan-out threshold; the payload cost only becomes visible well above it, so a 100+ page wiki reproduces it best.

### module_version

0.16.0

### rail_contract

1

