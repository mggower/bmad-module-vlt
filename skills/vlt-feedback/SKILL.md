---
name: vlt-feedback
depends_on: []
description: "File a field note upstream to the Vault module's public tracker as a labelled GitHub issue — classify honestly (defect / pattern / candidate), scrub it of vault paths and personal-domain content, render the exact public payload and halt for the user's approval, then post via gh with origin-vault and contract-version stamps. Use when the user says 'file this upstream', 'send feedback to the module', 'report this to the module', or when a partner has proposed a filing and the user says go. Invoked-only — a partner may propose a filing; only the user's explicit go executes. Degrades loudly: missing or unauthenticated gh yields a named error plus a paste-ready local filing, never a silent drop."
---

# vlt-feedback

## Overview

The module that runs this vault evolves on field signal — friction hit in anger, defects,
"this should ship upstream" observations. This skill is the vault's **remote feedback
rail**: it composes a filing under the module's **field contract**, scrubs it, previews it,
and posts it as a labelled issue on the module's public tracker. The issue is **transport**,
not the record — the module's factory materializes accepted issues into its own inbox and
its normal capture lifecycle takes over from there.

The contract this skill writes under — payload field set, labels, `origin:` header,
`rail_contract` version and its additive-only evolution rule — is single-homed at
`references/field-contract.md`. Read it before composing; restate it nowhere.

## On Activation

Load config from `{project-root}/_bmad/config.yaml` and
`{project-root}/_bmad/config.user.yaml` (root level and the `vlt` section). If the module
isn't set up (no `vlt` config in this project), tell the user `vlt-setup` can configure it.

**Resolve the transport endpoint:** the `feedback_repo` key in config's `vlt` section — an
`OWNER/REPO` slug passed to `gh --repo`. If the key is absent (a config written before the
rail shipped), read the default from the installed module manifest at
`.claude/skills/vlt-setup/assets/module.yaml` (`feedback_repo.default`) and **tell the user
loudly that the config is stale** — re-running setup (reconfigure) will materialize the key.
Never hard-code the endpoint here: the manifest default is its single home.

Also read `module_version` from config's `vlt` section (`version` metadata) and
`rail_contract` from `references/field-contract.md` — both are stamped into every payload.

## Trigger model — invoked-only, never auto-file

A partner may **propose** a filing when it hits something worth upstreaming; **only the
user's explicit go executes**. No filing composes, previews, or posts as a side effect of
other work.

## The judgment core

1. **Route first.** Is this actually module-source signal — shipped skill behavior,
   governance-bundle content, merge/upgrade machinery — rather than a vault-local matter
   (this vault's own overlays, minted skills, content, or configuration)? Vault-local
   matters are handled in the vault, not filed upstream. **When unsure, hand the question to
   the user with your reasoning — never guess the route silently.**
2. **Classify honestly** per the contract's `kind` field: `defect` (shipped behavior is
   wrong), `pattern` (a recurring shape worth naming), `candidate` (an upstream-this
   proposal). Don't inflate a preference into a defect.
3. **Duplicate guard.** Before composing, search the tracker:
   `gh issue list --repo <feedback_repo> --label vault-filed --search "<key terms>"`. If a
   plausible duplicate exists, show it to the user and ask whether to file anyway, comment
   there instead, or drop.

## Compose, scrub, and the approval gate

Compose the full payload per the contract: one `### <field_id>` section per field, in the
contract's order, plus the issue title (imperative, one line, no vault-local terms).

**The scrub checklist** (every item, every time):

- **No vault paths** — evidence uses placeholder paths (`_agent/{zone}/{file}.md` style),
  never this vault's literal file paths or artifact names.
- **No personal-domain content** — no journal/health/relationship/work-content material,
  even as illustration; describe the *machinery*, not the life it was holding.
- **No third-party names** — no people, employers, or private projects.
- **Two-tier escape hatch:** if the module maintainer would genuinely need detail the scrub
  removes, write a vault-side companion note (e.g.
  `_agent/feedback-outbox/{date}-{slug}-detail.md`) holding the detail locally, and
  **reference its existence** in the issue ("detail held vault-side, available on request")
  — never paste it.

**The approval gate — mandatory, no exceptions.** Render the **exact** issue title, the
**exact** body bytes, and the label list that would be posted, then **HALT for the user's
approval. Nothing posts without the gate.** This filing goes from a private vault to a
public tracker, irreversibly — the user sees the exact public bytes first, every time.
Declined material is not posted and not retained outside the session. This gate enacts
the field contract's **voice rule** (`references/field-contract.md`, *The voice rule* —
single-homed there); this paragraph is its procedure, nothing more.

## Transport

Labels per the contract: `vault-filed` always, plus the `field:<kind>` label matching the
classification.

**Pre-flight, before any transport attempt:**

- `gh` not on PATH → report the named error **`gh-missing`**, then take the failure path
  below.
- `gh auth status` exits non-zero → report the named error **`gh-unauthenticated`**, then
  the failure path.

On a clean pre-flight, post:

```
gh issue create --repo <feedback_repo> --title "<title>" --body "<body>" \
  --label vault-filed --label "field:<kind>"
```

Show the user the created issue URL. Every posted body carries the `origin_vault`,
`module_version`, and `rail_contract` sections — the stamps the factory intake reads.

## The failure path — paste-ready, never a silent drop

On **any** transport failure — `gh-missing`, `gh-unauthenticated`, a network failure, any
non-zero `gh` exit — write the fully-composed filing to
`_agent/feedback-outbox/{YYYY-MM-DD-HHmmss}-{slug}.md`: the title, the complete body with
every payload section, and the **label names and origin vault pre-written, paste-ready**.
Then print the file path and the manual route: open an issue at the transport repo
(`https://github.com/<feedback_repo>/issues/new/choose`), paste the body, apply the named
labels. The outbox is transient — delete or archive the file once it has been pasted; it is
a recovery artifact, not a record.

(`_agent/feedback-outbox/` is deliberately **not** a `vault_structure` logical name: it
exists only on transport failure, is never always-loaded, and accumulates nothing — a
fixed agent-zone path, like the dispatch board's.)

## References

- `references/field-contract.md` — the field contract: payload field ids, the label set and
  who applies each, the `origin:` header shape, `rail_contract` and the additive-only
  evolution rule. The single home; this skill derives from it.
