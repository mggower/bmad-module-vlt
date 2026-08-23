# vlt-setup — Verification Notes

_Friction observed running `/vlt-setup` on a fresh installer-built vault (`vlt-core`), 2026-06-03. For module iteration._

Setup completed successfully on the first pass — no hard failures, no script errors, idempotent guards all behaved. The notes below are friction/ambiguity that slowed the agent or required a judgment call, ordered roughly by impact.

## 1. Interactive-vs-non-interactive is underspecified when the installer already collected answers

The skill's **Collect Configuration** section says "Ask the user for values" and "present values together so the user can answer once." But on an installer-built vault, the installer's `config.toml`/`config.user.toml` *already hold the user's answers* (`user_name = "Mikey"`, `communication_language = "English"`, `output_folder`, `document_output_language`). The user ran `/vlt-setup` with no args.

There's no explicit guidance for this common case, so the agent had to decide between (a) re-prompting for values the installer already has, or (b) silently reusing them. I chose (b) and surfaced everything in the confirmation. This worked but was a guess.

**Suggested fix:** add a rule like — "If `config.toml` (installer) already contains core answers and config.yaml lacks them, treat the TOML values as collected defaults and proceed non-interactively unless the user passed values to change."

## 2. `output_folder` default conflicts between the skill and the installer

- Skill default (`module.yaml`/skill text): `{project-root}/_bmad-output`
- Installer's `config.toml`: `{project-root}/_output`

The "Default priority" rule (existing new config > legacy > module.yaml defaults) implies the installer value should win, but the installer's TOML isn't clearly named in that priority list ("legacy config" is described as per-module staging YAML, not the root `config.toml`). I went with `{project-root}/_output` to stay consistent with what the user already chose, but the precedence wasn't unambiguous.

**Suggested fix:** explicitly state where the installer's root `config.toml` sits in the default-priority chain.

## 3. Dependency check gives a false-negative for host-provided skills

The **Check Dependencies** step says to look in `{project-root}/.claude/skills/`. `deep-research` is **not** in that directory, so the literal check reports it MISSING — yet it *is* available as a host/plugin skill (it appears in the session's available-skills list and the Researcher can call it). A naive run of this check would warn the user about a missing dependency that isn't actually missing.

**Suggested fix:** broaden the check to also account for host/plugin-provided skills (or soften the wording: "if not found locally, it may still be host-provided").

## 4. The `vault_structure = "[object Object]"` TOML wart

The skill does document this (installer serializes the structure map as `"[object Object]"` in TOML, harmless because the runtime reads `config.yaml`). Calling it out is good — but it's a confidence-eroding artifact for anyone inspecting `config.toml`. Worth flagging upstream to the installer team since the skill itself can't fix it.

## 5. `{project-root}` literal-token trap is real (and the skill knows it)

The skill repeats — three times — that `{project-root}` is a literal token in config *values* but must be the resolved path in shell *arguments*. The fact that it needs saying that many times confirms it's genuinely error-prone. The `$ROOT="$(pwd)"` / `$SKILL=<base dir>` pattern worked cleanly once followed, so the guidance is effective — just inherently a sharp edge.

## 6. `vlt-setup` scaffolds every state file *except* `{log}` — the one append-only file the activation ritual reads

_(Owner-side record of a finding first hit downstream — see `librarian-ingest-friction.md §2`. The fix belongs here, in `vlt-setup`, which is why it's documented in this doc and not only in the consumer's.)_

`vlt-setup` scaffolds the wiki index, the backlog, and the partner threads — but **not `{log}` (`_agent/log.md`)**. Yet every partner's activation ritual step 2 is "read recent `{log}`," and `vlt-ingest` Step 1 greps `{log}` for a re-ingest check. So on a freshly-set-up vault:

- the activation "read the log" step **silently no-ops** (file absent), and
- a literal re-ingest `grep ... {log}` **errors** on the missing file (the Librarian skipped it by knowing the vault was empty; a naive pass would hit the error).

The log gets created lazily on the first write that happens to append to it — meaning the vault's canonical chronological record only springs into existence as a side effect, rather than being scaffolded with the other state files. This is the same fresh-vault-edge family as the empty `vault_structure` and the lint-cadence-with-no-baseline findings.

**Suggested fix (module-direct):** have `vlt-setup` create `{log}` at scaffold time with its header (`# Log\n\nAppend-only chronological record…`), exactly alongside the backlog/index/threads it already creates. Optionally also harden the `vlt-ingest` re-ingest grep with `2>/dev/null` as defense-in-depth. **This finding is confirmed as a real fix (not a doc-clarification) and has been filed to `{backlog}` as a `maintenance` item** — resolving the "undecided" thread item the Librarian carried across two sessions.

## What went smoothly (for balance)

- `merge-config.py` / `merge-help-csv.py` ran clean under `uv run`, returned clear JSON, anti-zombie behaved (fresh install: `core_updated: true`, 10 help rows added).
- Governance bundle copied all 10 files with no clobbering; absence-guards correct.
- Partner threads, backlog, wiki index, CLAUDE.md pointer all scaffolded with proper idempotent skips. (**But not `{log}`** — see §6; the chronological record is the one state file setup omits.)
- Co-installed modules (`core`, `bmm`, `bmb`) were untouched, as intended.

---

_Net: setup is solid. The friction is almost entirely about disambiguating behavior on an **installer-built** vault (config precedence, reusing installer answers, host-provided dependency detection) rather than any broken mechanism — with one concrete scaffolding gap (§6: `{log}` is not created at setup time) now confirmed as a fix and backlogged._
