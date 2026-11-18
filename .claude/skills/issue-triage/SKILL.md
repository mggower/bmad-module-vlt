---
name: issue-triage
description: Grounds open feedback issues against the plugin's source, rules them accepted or declined in one owner-approved batch, and writes each accepted issue into the inbox as a filing. Use when the user says 'run issue triage' or 'triage the tracker'.
---

# issue-triage

Vaults file feedback as labelled issues on the public tracker (`feedback.md` in the core kit). An issue sits `vault-filed` until the owner admits or declines it. This skill does the reading: it finds the untriaged issues, checks every claim against current source, and puts one table in front of the owner. Admitting and declining are the owner's verbs.

Every shape on the rail (labels, state flow, payload fields, `rail_contract`, the voice rule) is defined in `kits/core/files/resources/playbooks/feedback-field-contract.md`. Read it first; nothing of it is restated here.

The tracker is the `repository` in `.claude-plugin/marketplace.json`, as `OWNER/REPO`.

## Steps

1. **Pre-flight.** `gh` on PATH and `gh auth status` exits 0. If not, say which failed and stop. A failed pre-flight is never reported as an empty queue.
2. **Discover.** `gh issue list --repo <repo> --label vault-filed --state open --json number,title,labels,body`. Leave out issues that already carry `vault-accepted`, `captured`, `declined` or `needs-info`, and any whose number appears in an `origin:` line under `factory/inbox/`. Say how many were found and how many were left out, and why.
3. **Ground each issue.** Read the body's fields. For every claim about what the kits or the two skills do, open the file and check it at `path:line`. Filings often guess the wrong cause; record what the source actually shows. An issue about something 1.0 no longer ships (see `COMING-FROM-0.x.md`) is noted as that.
4. **One table for the owner**: issue, what it claims, what the source shows, and a proposed verdict (`accept`, `decline` with one of the contract's reasons, or `needs-info` with the question). Stop here for the ruling. With `--report`, stop here always.
5. **Apply the ruling**, under the voice rule: for each issue show the exact label change and the exact comment, and post only on approval.
6. **Materialise each accepted issue** as `factory/inbox/<YYYY-MM-DD>-<HHmmss>-<slug>.md`: the first line `origin: <repo>#<n>`, then the issue's fields and the grounding from step 3. Add the `captured` label to the issue. An issue whose number already has an `origin:` line is never written twice.
7. **Commit** the new filings.

## Report

Issues found, the verdict on each, the filings written, and anything left `needs-info`.
