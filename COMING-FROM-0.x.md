# Coming from vlt 0.x

vlt 1.0 is a different thing from 0.x: a toolkit a vault owns, not a cast of partners governed by a contract. It ships **no migration**. This page is a map: what 0.19 put into a vault, where it is, and what in 1.0 replaces it. A session working in the vault uses it to decide what to retire and when. That work is the vault's own, done at its own pace.

Four things hold whatever the vault decides:

- **Run the plugin's setup, not the vault's.** A 0.x vault holds its own older `vlt-setup` and `vlt-upgrade` in `.claude/skills/`, and they answer the same words. Invoke the new one as `/vlt:vlt-setup`, or archive the two old skills first.
- **`vlt-setup` is safe to run first.** It never overwrites or deletes an existing file. Where a 1.0 file would land on one the vault already has (`CLAUDE.md`, a skill of the same name), it leaves the vault's copy and shows the difference.
- **Nothing in 1.0 reads anything in the table below.** The old machinery can be retired before setup, after it, or piece by piece.
- **Retiring is moving, not deleting.** `git mv` into `_agent/archive/`, keeping the path under it.

## What 0.19 installed, and what replaces it

### Skills (`.claude/skills/`)

| 0.19 | In 1.0 |
|---|---|
| `vlt-ingest`, `vlt-query`, `vlt-research`, `vlt-feedback` | The same names, now thin pointers at playbooks (`resources/playbooks/ingest.md` and so on). Setup keeps the vault's 0.19 copies; to switch, commit, then `vlt-pull` and take the kit's copy of each. |
| `vlt-setup`, `vlt-upgrade` | Served by the plugin, not copied into the vault: `vlt-setup` and `vlt-pull`. The vault's copies can be archived. |
| `vlt-mint` | `resources/playbooks/add-a-tool.md`: a short method for adding a tool or a playbook. No partner minting. |
| `vlt-lint` | Nothing vault-wide. `python3 _agent/tools/checks/run.py` runs the small checks a vault has. |
| `vlt-extract`, `vlt-track`, `vlt-dispatch`, `vlt-groom`, `vlt-decay`, `vlt-review-council` | Nothing. |
| `vlt-agent-librarian`, `vlt-agent-researcher`, `vlt-agent-creative`, and any minted `vlt-agent-*` | Nothing. The wiki procedures and research are playbooks any session runs. To retire a partner and keep what it could do, see `FLATTEN-A-PARTNER.md`. |

### Governance (`_meta/`)

| 0.19 | In 1.0 |
|---|---|
| `vault-operating-contract.md`, `vault-rule-card.md` | `_meta/vault.md`: the rules, in two pages, owned by the vault. |
| `conventions/frontmatter.md` | `_meta/frontmatter.md`. |
| `conventions/wiki-index.md`, `wiki-supersession.md`, `wiki-consolidation.md` | `_meta/wiki.md`. The index shape, the callouts and the `superseded_*` keys are unchanged, so existing wiki pages stay valid. |
| `conventions/write-verification.md` | The attestation keys in `_meta/frontmatter.md`. `verified_by` now names a playbook (`ingest`), not a skill (`vlt-ingest`); older values are left as they are. |
| `conventions/extraction.md`, `spec.md`, `consult.md`, `decision-log.md` | Nothing. |
| `personas/` (five review lenses) | Nothing. |
| `_agent/conventions/` overlays and `.baseline/` | Nothing. A vault edits its own `_meta/` files directly; there is no overlay layer. A rule an overlay added is carried into the file it belongs to by hand. |

### Runtime pieces (`.claude/`, `_agent/`, `_bmad/`)

| 0.19 | In 1.0 |
|---|---|
| `.claude/workflows/vlt-consult.js`, `vlt-delegate.js`, `vlt-lint-full.js`, `vlt-review-council.js` | Nothing. |
| `.claude/hooks/vlt-vitals.py`, and its `SessionStart` entry in `.claude/settings.json` | Nothing. Remove the settings entry when the hook is archived, or every session start reports a missing file. |
| `_agent/tripwires.yaml` | Nothing. |
| `.claude/skills/.skill-manifest*` (the asset manifest) | `_agent/kits.lock`. |
| `_bmad/config.yaml` (`vlt` section), `_bmad/config.user.yaml`, `_bmad/module-help.csv` rows, `_bmad/vlt/` | Nothing. 1.0 is a Claude Code plugin and reads no `_bmad` file. Other BMad modules in the vault are unaffected. |
| The `CLAUDE.md` block importing `@_meta/vault-rule-card.md` and `@_agent/reflexes.md` | One line: `@_meta/vault.md`. Setup shows it and adds it only when asked. |

### What the vault grew under 0.19 (`_agent/`)

| 0.19 | In 1.0 |
|---|---|
| `_agent/log.md`, `_agent/sessions/`, `_agent/research/` | Kept, same places. New log entries drop the partner name in parentheses; readers accept both shapes. |
| `resources/wiki/`, `sources/` | Kept, same places and same rules. |
| `_agent/backlog.md` | Task boards: `<zone>/tasks/` for work in a zone, `_agent/tasks/` for the vault itself (`resources/playbooks/task-board.md`). Open entries are moved by hand, each to the board that owns it. |
| `_agent/partners/` (identity, thread, casebook, capabilities, subscriptions) | Nothing. See `FLATTEN-A-PARTNER.md`. |
| `_agent/capabilities/`, `_agent/capabilities/families/` | Playbooks in `resources/playbooks/`, tools in `_agent/tools/<name>/`. |
| `_agent/reflexes.md` | Nothing. A standing pointer the vault still wants goes in its `CLAUDE.md`. |
| `_agent/dispatch.md`, `_agent/specs/`, `_agent/handoffs/` | Nothing. |
| `_agent/mint/` (planning documents, `decision-log.md`) | Nothing. It is history; archive it or leave it. |
| `_agent/upgrade-ledger.md`, `_agent/upgrade-reports/`, `_agent/lint-reports/`, `_agent/lint-cache.json` | Nothing. |
| `trust: raw` on existing notes | `trust: draft` is what a session writes now. `raw` means the same; renaming old notes is optional. |

## Where 1.0 files land

`_meta/vault.md`, `_meta/wiki.md`, `_meta/frontmatter.md`; `resources/playbooks/`; `.claude/skills/vlt-playbook/` and the four named pointer skills; `_agent/tools/`, `_agent/templates/`, `_agent/bases/`, `_agent/tasks/`, `_agent/tasks.base`; `_agent/kits.lock`; and `CLAUDE.md` in a vault that has none. The exact list is `python3 scripts/kits.py status --vault <vault>` after setup.
