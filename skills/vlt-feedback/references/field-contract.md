# The field contract — the module's remote feedback rail

The **single home** of the filing shape shared by three surfaces: the repo-side issue forms
(`.github/ISSUE_TEMPLATE/` on the module repo), the `vlt-feedback` skill's composed payload,
and the factory intake that materializes accepted issues. Those surfaces **point here and
derive from here — never restate this contract**. GitHub issues are transport; the module
repo's inbox stays the source of truth; capture is the airlock.

## Contract version

```
rail_contract: 1
```

**Evolution rule — additive-only.** Adding a payload field does **not** bump
`rail_contract`. Renaming a field, removing a field, or changing a field's meaning **does**
bump it. Every filed issue carries the `rail_contract` value it was composed under; the
factory intake compares the stamp against the current contract and flags a stale-shape
filing for hand-handling instead of parsing it hopefully.

## The payload field set

Field ids are **normative**: the issue forms use them as each form field's `id:`, and
`vlt-feedback` composes the issue body (and the transport-failure artifact) as one
`### <field_id>` section per field, in this order.

| Field id | Required | Content |
| --- | --- | --- |
| `what_happened` | yes | What happened / the observation, concretely, as hit in real use. |
| `evidence` | yes | Generalized evidence: placeholder paths (`_agent/{zone}/{file}.md` style), quoted behavior, exact error text. **No vault-local literals, no personal-domain content.** |
| `provenance_guess` | no | Where in the module source this probably lives — **explicitly marked as a guess**; the factory grounds every claim before capture. |
| `kind` | yes | Honest classification: `defect` (shipped behavior is wrong), `pattern` (a recurring shape worth naming), or `candidate` (a "this should ship upstream" proposal). |
| `origin_vault` | yes | The vault the signal originated in (a short vault name, not a path) — attribution is by vault, not by GitHub account. |
| `acceptance_vault` | no | Where acceptance should run — the vault (or kind of vault) that can actually reproduce/verify the fix. |
| `module_version` | yes | The filing vault's installed module version (from config's `vlt` section, `version` metadata). |
| `rail_contract` | yes | The contract version this payload was composed under (see above). |

## The `origin:` header — factory-materialized filings

When the factory intake materializes an accepted issue into an inbox filing, the filing
carries a machine-written header line:

```
origin: <repo>#<n>
```

for example `origin: mggower/bmad-module-vlt#1`. This is the **idempotency key**: an issue
whose number already appears in an `origin:` header is never materialized twice, and
discovery excludes already-materialized issues by it. The intake writes it; nothing else
does.

## The label set

Seven labels, defined once, here. State-transition **mechanics** belong to the factory
intake; both halves of the rail read this one table.

| Label | Applied by | Meaning |
| --- | --- | --- |
| `field:defect` | template (defect form) or filer/triage | Classification: shipped behavior is wrong. |
| `field:pattern` | filer or owner triage | Classification: recurring shape worth naming. (The shared pattern/candidate form cannot branch labels — the `kind` field in the body is authoritative.) |
| `field:candidate` | filer or owner triage | Classification: upstream-this proposal. (Same form note as `field:pattern`.) |
| `vault-filed` | issue form frontmatter, automatic | **Candidacy, not admission** — this issue claims to follow the field contract. |
| `vault-accepted` | owner, at triage | The owner admits the filing; this is the factory intake's materialization trigger. |
| `captured` | factory intake, at materialization | The issue now exists as an inbox filing (with an `origin:` header) and rides the normal capture lifecycle. |
| `declined` | owner, terminal | Not admitted — issue closed with a stated reason; nothing is materialized. |

**State flow:** `vault-filed → vault-accepted → captured`, or `vault-filed → declined`. An
issue without `vault-filed` is not on the rail at all and is invisible to the intake's
discovery by construction.
