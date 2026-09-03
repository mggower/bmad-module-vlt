// Cycle 15 — the shared runtime shim for the at-rest harnesses over `vlt-lint-full.js`.
//
// Factored out by build-4 (the third harness): build-3's header ruled "a shared shim is a
// refactor for whichever build adds a third harness". Loads the workflow the way package-lint's
// E6 does (node over the file), rewrites `export const meta` to `const meta`, wraps the body in
// an AsyncFunction with the runtime globals stubbed, and delivers `args` as a JSON STRING —
// exactly as the runtime does. The agent stub is wrapped in a COUNTER (build-3's instrument): a
// refusal case must show 0 invocations, not merely `files_checked: 0`.
//
// Imported by build-2-key-harness.mjs, build-3-type-harness.mjs and build-4-return-harness.mjs.

import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

export const HERE = path.dirname(fileURLToPath(import.meta.url))
export const REPO = path.resolve(HERE, '..', '..', '..', '..')
export const SHIPPED = path.join(REPO, 'skills', 'vlt-setup', 'assets', 'workflows', 'vlt-lint-full.js')

const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor
export const compile = (src) => new AsyncFunction('args', 'agent', 'parallel', 'phase', 'log', 'budget', 'workflow',
  src.replace(/^export const meta =/m, 'const meta ='))

export async function run(src, args, agentStub = async () => null) {
  const logs = []
  let invocations = 0
  const labels = []
  const counting = async (prompt, o) => { invocations++; labels.push(o && o.label); return agentStub(prompt, o) }
  const fn = compile(src)
  const result = await fn(
    JSON.stringify(args),                       // the runtime delivers args as a JSON string
    counting,
    (thunks) => Promise.all(thunks.map((t) => t())),
    () => {},
    (m) => logs.push(String(m)),
    { total: 0, remaining: () => 0 },
    async () => null,
  )
  return { result, logs, invocations, labels }
}

// A `scan:` stub returning each slug's own record (the gen-pass stub both prior harnesses use).
export const scanStubFrom = (bySlug) => async (_prompt, o) =>
  (o && typeof o.label === 'string' && o.label.startsWith('scan:')) ? structuredClone(bySlug.get(o.label.slice(5))) : null

export const readSrc = (workflowPath = SHIPPED) => fs.readFileSync(workflowPath, 'utf8')
