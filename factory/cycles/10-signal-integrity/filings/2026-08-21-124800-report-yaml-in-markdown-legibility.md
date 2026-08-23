# Reports are YAML fenced inside markdown — should they be plain `.yaml` files instead?

_Filed 2026-08-21 by the owner (via the factory clerk, owner's words in-session),
classification: **question / pattern candidate** — a design question for ideation, not an
asserted defect. **Provenance:** the vlt-core 0.11.0 → 0.12.0 upgrade run (2026-08-21);
the owner, reading the Step-4 report, noted the persisted-report format is "mostly yaml in
a codeblock on a markdown file" and asked whether plain `.yaml` files would be more
legible. Companion filing: `2026-08-21-124500-upgrade-reports-need-a-durable-vault-home.md`
(same hat, same run — that filing is about *whether* reports persist; this one is about
*what shape* they persist in)._

## The current shape (grounded 2026-08-21 against v0.12.0 @ `336d90b`)

- `vlt-lint`'s persisted report (`{lint_reports}/YYYY-MM-DD-HHMM-lint.md`) is a markdown
  file whose payload is one strict-YAML fenced block (`vlt-lint/references/report.md:3` —
  "The fenced report block is strict YAML as a whole — keep it parsing whole") plus a
  mode/scope line. The `.md` wrapper carries essentially nothing the fence doesn't.
- `vlt-upgrade`'s Step-4 report is the same shape in-session (a `yaml`-fenced `upgrade:`
  block). Its digest home (`_agent/upgrade-ledger.md`) is markdown bullets.

## The trade, both sides (for the ideation table)

**For `.yaml`:** the wrapper is ceremony — a machine-parseable artifact gains direct
`yq`/dashboard consumption, syntax highlighting, and one less strip step; "structured and
parseable (so a dashboard can read it)" is the report's own stated design goal
(`vlt-lint/SKILL.md:11`).

**For staying `.md`:** nearly all vault machinery walks markdown — frontmatter@9 and its
attestation pairs, wikilinks, lint's own scanners, the decay verbs' block grammar, and the
wake/reflex reads are all `.md`-shaped. A `.yaml` file is invisible to that machinery —
which cuts both ways: reports are deliberately *exempt* artifacts (never wake-read,
retention owned by the human, per the Decay-contracts exemption lint's persist rule cites),
so invisibility may be exactly right — or it may strand them from future tooling (e.g. a
report-reading acceptance instrument, or lint checking report retention).

**Middle shapes worth pricing:** (a) keep `.md` but define the contract as
"minimal-frontmatter + one fence, nothing else" so a consumer strips deterministically;
(b) `.yaml` sidecar + one-line `.md` pointer; (c) `.yaml` files under report dirs declared
as a lint-walker exclusion, making the invisibility explicit rather than incidental.

## What a build would owe (if ruled)

A format change to lint's persisted report touches `vlt-lint/SKILL.md:72`,
`references/report.md`, the `{lint_reports}` path docs, and any consumer that greps past
reports (census owed at capture — the lint-debt counter derivation reads the *session log*,
not the reports, but verify). If the companion filing ships an upgrade-report persist, the
two should land with the **same** format ruling — one contract, not two dialects.
