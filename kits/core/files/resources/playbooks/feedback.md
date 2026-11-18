---
type: resource
created: 2026-11-18
last_updated: 2026-11-18
title: Playbook — file feedback upstream to the module
need: "File this upstream, or send feedback to the vlt module"
state: live
domain: vault
companion: resources/playbooks/feedback-field-contract.md
---
# File feedback upstream

The kits this vault was seeded from are developed in a public repository, and they change on what vaults report: a defect hit in real use, a pattern worth naming, something that should ship. This playbook files one such report as a labelled issue on that repository's tracker. The issue goes from a private vault to a public page and cannot be taken back, so the owner sees the exact bytes before anything is posted.

The shape of a filing (field ids, their order, the labels) is defined in the companion, `feedback-field-contract.md`. Read it before composing.

## Prerequisites

- `gh` installed and signed in (`gh auth status` exits 0). Without it the playbook still runs and ends at the paste-ready file under *Output*.
- The tracker: `mggower/bmad-module-vlt`. A vault that reports somewhere else changes that line here.
- The owner has asked for the filing, or has said yes to one a session suggested. A filing is never composed or posted as a side effect of other work.

## Procedure

1. **Decide whether it belongs upstream.** Upstream signal is about what the kits shipped: a seeded playbook, rule, skill, check or script, or `vlt-setup` and `vlt-pull`. Something this vault changed or grew itself is the vault's to fix, here. When it is unclear, put the question to the owner with your reasoning.
2. **Classify it honestly**, as the contract's `kind`: `defect` (what shipped is wrong), `pattern` (a recurring shape worth naming), `candidate` (this should ship), `supersession` (something shipped is now redundant; name the rule and what replaces it). A preference is not a defect.
3. **Look for a duplicate.** `gh issue list --repo mggower/bmad-module-vlt --label vault-filed --search "<key terms>"`. If one is plausible, show it to the owner and ask: file anyway, comment there, or drop.
4. **Compose** the title (imperative, one line, no vault-local terms) and the body: one `### <field_id>` section per field, in the contract's order. `module_version` is the `core` kit's `version` in `_agent/kits.lock`. For a `supersession` both conditional sections are required.
5. **Scrub**, every item, every time:
   - no vault paths: evidence uses placeholder paths (`_agent/{zone}/{file}.md`), never this vault's real ones;
   - no personal content: describe the machinery, not what it was holding;
   - no third-party names: no people, employers or private projects.
   If the maintainer would need detail the scrub removes, write it to `_agent/feedback-outbox/{date}-{slug}-detail.md` and say in the issue that detail is held in the vault and available on request.
6. **Show the owner the exact title, the exact body and the labels, and stop.** Nothing is posted without their yes. If they decline, nothing is posted and nothing is kept.
7. **Post.** `gh issue create --repo mggower/bmad-module-vlt --title "<title>" --body "<body>" --label vault-filed --label "field:<kind>"`. Show the owner the issue URL.
8. **If the vault is working around the problem meanwhile,** file a task on the vault board (`_agent/tasks/`) that states what the kits do today that forces the workaround, and links the issue. It does not record the commands to undo the workaround: those are worked out when the answer arrives, against the files as they are then.

## Output

- A posted issue, and its URL shown to the owner.
- On any failure to post (no `gh`, not signed in, a network error, a non-zero exit): say which, then write the whole filing to `_agent/feedback-outbox/{YYYY-MM-DD-HHmmss}-{slug}.md` with the title, the full body and the label names, and give the owner the path and the page to paste it into (`https://github.com/mggower/bmad-module-vlt/issues/new/choose`). A filing is never dropped silently. Delete the file once it has been pasted.

## Rules

- The owner approves the exact bytes, every time. There is no path around step 6.
- Nothing personal and no real vault path leaves the vault.
- One filing, one subject.
