# vlt-lint mandates a strict-YAML report persist but assumes a YAML library that may not be installable

origin: mggower/bmad-module-vlt#14

- **filed:** 2026-08-26 (GitHub issue opened 12:31:53Z via the vlt-feedback rail)
- **origin vault:** vlt-core · **module_version:** 0.16.0 · **rail_contract:** 1 · **kind:** candidate
- **materialized:** 2026-08-26 by the factory intake (github-intake)

---

### what_happened

`vlt-lint` Step 6 requires the report be persisted as plain YAML to `{lint_reports}/YYYY-MM-DD-HHMM-lint.yaml`, and `references/report.md` requires the block parse as strict YAML "whole, in both homes."

That is a reasonable requirement, but the module ships no way to satisfy it and no guidance for an environment without a YAML serializer. On this machine `python3` has no `yaml` module, and installing one is refused:

```
ModuleNotFoundError: No module named 'yaml'
$ python3 -m pip install pyyaml
error: externally-managed-environment
hint: See PEP 668 for the detailed specification.
```

PEP 668 environment management is now the default on Homebrew Python and most current Linux distributions, so this is the common case rather than an unusual one.

The run completed — I hand-wrote a small emitter that serializes every scalar as a JSON string (JSON being a subset of YAML 1.2), which parses correctly. But that is an unverified ad-hoc serializer standing between a mandated machine-readable artifact and the dashboard the report exists to feed, and every vault in a PEP 668 environment will independently reinvent it, differently.

### evidence

The requirement, from `vlt-lint` Step 6:

> Also **persist the report** (both modes): write the Step-5 report block **verbatim** to `{lint_reports}/YYYY-MM-DD-HHMM-lint.yaml` — plain YAML, the block's content without the fence

and from `references/report.md`:

> The fenced report block is strict YAML as a whole — emitted fenced in-session and **persisted as the plain `.yaml` file** — same content, no fence; keep it parsing whole in both homes.

The report contains free-text findings with em-dashes, colons inside values, quoted strings, arrows, and nested structures — exactly the content where naive YAML emission breaks and where "it looked fine" is not verification. There is no round-trip check available either, since the same missing library blocks parsing it back.

Worth noting the report schema is otherwise unusually disciplined about honest measurement — it mandates naming the unwrapped instrument behind every derived verdict. An unverified hand-rolled serializer is the one place that discipline currently has no answer.

### provenance_guess

**A guess.** `vlt-lint` Step 6 and `references/report.md` are where the requirement is stated; neither names a mechanism.

Candidate fixes:

1. **State the no-dependency requirement explicitly** and specify the JSON-subset emission strategy in `report.md` — every scalar as a JSON string, lists as `- <json>`, nested maps by indentation. This is a documentation fix, costs nothing, and makes every vault's serializer identical instead of independently invented.
2. **Ship a small emitter** as a skill asset, so the strategy is executed rather than described.
3. Or, if the persist format is genuinely negotiable, allow `.json` as an alternative persist — the report's consumers are machines, JSON is trivially emittable everywhere, and the fenced in-session block can stay YAML for human reading.

Option 1 alone would have closed it here.

### kind

candidate

### origin_vault

vlt-core

### acceptance_vault

Any vault on a PEP 668-managed Python (current Homebrew, Debian/Ubuntu, Fedora) with no YAML library in the interpreter the session reaches.

### module_version

0.16.0

### rail_contract

1

