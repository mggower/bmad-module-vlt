# Rename the loop-profile slot non-negotiable-gate to write-gate

origin: mggower/bmad-module-vlt#19

- **filed:** 2026-09-09 (GitHub issue opened 18:48:40Z via the vlt-feedback rail)
- **origin vault:** vlt-core · **module_version:** 0.18.0 · **rail_contract:** 1 · **kind:** defect
- **materialized:** 2026-09-16 by the factory intake (github-intake)

---

### what_happened

The loop-profile block a vertical partner fills in its `capabilities/track.md` (the `vlt-track` wearer profile) has a slot named `non-negotiable-gate`. What the slot actually carries is the rule that bites **at the PARA write** — the method-grounding / provenance firewall `vlt-track` re-asserts before writing the polished protocol. That is not, in general, the partner's stated non-negotiable, which bites live in conversation and is inert at a program write.

Three wearing partners in one vault have now each carried an apologetic parenthetical beside the slot explaining that the name misdescribes what is in it ("the slot is named `non-negotiable-gate`; see the note below"). A council on the second occurrence ruled the explanation must not be copied a fourth time and that the remedy is upstream. This filing is that remedy; the earlier records that cite "the standing upstream filing" were wrong — no filing had been posted.

Motivating instance now moot, defect stands: one wearing partner was rebuilt so that its non-negotiable and its write-gate became the same rule, so for that partner the slot name is accidentally honest. A partner whose live non-negotiable differs from its write-gate (the common case — a coaching partner that withholds an answer in conversation, say) still has no honest slot to put the write-gate in.

### evidence

- The shipped capability template's loop-profile block: `- non-negotiable-gate: <this partner's named method gate — re-asserted at the write>` — the description says "method gate … at the write", the key says "non-negotiable". The two disagree in the template itself.
- Observed shape in a wearer's `_agent/partners/{partner}/capabilities/track.md`: `write-gate *(the profile slot is named `non-negotiable-gate`; see the note below)*: **grounded or marked** — …` followed by a blockquote explaining the mismatch. The same shape appeared in two other wearers' profiles.
- Council record (vault-side, `_agent/mint/decision-log.md`): "Upstream `write-gate` slot-name bug — third occurrence, and the note must not be written a fourth time … the filing has no owner and no date."

Proposed change: rename the slot to `write-gate` in the template and in `vlt-track`'s profile read, and accept `non-negotiable-gate` as a deprecated alias for one release so existing wearers keep parsing. The template description line already says what the slot is; only the key is wrong.

### provenance_guess

Guess, unverified against module source: `skills/vlt-mint/assets/capability-template.md` (loop-profile block, the `non-negotiable-gate` line — observed at line 68 in the installed 0.18.0 copy) and `skills/vlt-track/SKILL.md` (the On-Activation profile binding that names the slot). The build brief that upstreamed `vlt-track` lists the slot among the profile keys, so the name likely dates from that lift.

### kind

defect

### origin_vault

vlt-core

### acceptance_vault

Any vault with at least one `vlt-track` wearer whose live non-negotiable is not its write-gate (a coaching-style partner); acceptance = the profile parses under the new key and the old key with no explanatory note needed.

### module_version

0.18.0

### rail_contract

1

