#!/usr/bin/env bash
# Cycle 16 build-3 — the instrument for acceptance check (1) Carrier (brief F1/F2).
#
# The `S-4` harness, re-pointed: instead of a hand-written probe vault it provisions a scratch vault
# from the SHIPPED `vlt-setup` §3 text (the two `@` import lines, the card path resolved from the
# structure map, the rung at `_agent/reflexes.md`), plants a CANARY line inside the card and inside
# the rung, and reads the RUNTIME'S ATTACHMENT RECORD out of each session transcript — the record the
# runtime writes before any model turn, naming every instruction file it delivered. A model asked
# "is the canary in your context?" can answer from the question; the attachment record cannot.
#
# Two vaults, because a passing probe on a FRESH vault is compatible with the property being violated
# for every INSTALLED vault:
#   A  fresh   — the seed branch: `CLAUDE.md` written by §3, imports present.
#   B  existing — the never-clobber branch: a `CLAUDE.md` that already references the contract in
#                 prose and carries NO imports. F2 re-keys the offer on the IMPORT LINES' absence
#                 precisely because the old key ("if it doesn't already reference the contract")
#                 never fires here. The probe asserts the pre-state (offer must fire), then appends
#                 the two lines as an ACCEPTED offer and re-probes.
#
# Each leg asserts: the card and the rung each appear in the attachment record EXACTLY ONCE (once,
# not twice — a double delivery would be a second carrier), and the canaries come back in the reply.
#
# Legs 1–3 run here (headless `claude -p`; an in-session skill summon; an Agent-tool subagent). The
# workflow-`agent()` leg is `S-4` row 5's kind — the one `vlt-delegate.js` is — and is run by
# invoking any one-agent workflow from inside a session whose cwd is the probe vault.
#
# Usage: bash probe.sh   (writes its scratch vaults under $TMPDIR; prints PASS/FAIL per leg)
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/../../../../.." && pwd)"
GOV="$REPO/skills/vlt-setup/assets/governance/_meta"
CANARY_CARD="CARRIER-CANARY-CARD-7731"
CANARY_RUNG="CARRIER-CANARY-RUNG-9912"
FAILS=0

pass() { echo "PASS  $1${2:+ — $2}"; }
fail() { FAILS=$((FAILS+1)); echo "FAIL  $1${2:+ — $2}"; }
ck()   { if [ "$2" = "1" ]; then pass "$1" "${3:-}"; else fail "$1" "${3:-}"; fi }

seed_vault() {  # $1 = root, $2 = "fresh" | "existing"
  local V="$1"
  rm -rf "$V"; mkdir -p "$V/_meta" "$V/_agent" "$V/resources/wiki" "$V/_bmad"
  printf 'vlt:\n  vault_structure:\n' > "$V/_bmad/config.yaml"
  # the card and the rung, as the shipped seed installs them, each carrying its canary
  sed "s|^# Vault Rule-Card|# Vault Rule-Card\n\nCANARY: $CANARY_CARD|" "$GOV/vault-rule-card.md" > "$V/_meta/vault-rule-card.md"
  cat > "$V/_agent/reflexes.md" <<RUNG
---
type: reflexes
scope: vault
cap_words: 900
---

research runs — any partner, as itself: the contract, *Capabilities*; the lane sentence.
CANARY: $CANARY_RUNG
RUNG
  cp "$GOV/vault-operating-contract.md" "$V/_meta/vault-operating-contract.md"
  if [ "$2" = "fresh" ]; then
    # vlt-setup §3, no-CLAUDE.md branch — verbatim in shape, paths resolved from the structure map
    cat > "$V/CLAUDE.md" <<'MD'
# Vault

@_meta/vault-rule-card.md
@_agent/reflexes.md

This vault is tended by the **Vault** BMad module — a cast of partners (Librarian, Researcher)
who share this wiki. The two lines above load the rule-card (the identity-bearing and act-blocking
rules) and this vault's rung (its pointer lines) into **every** session — partnered or not. The full
rules live in `_meta/vault-operating-contract.md`, read point-of-use by section; the conventions
every write obeys are in `_meta/conventions/`.

## Preferences

_Empty until you set one._
MD
  else
    # an INSTALLED vault: prose pointer at the contract, no imports — the old offer key never fires
    cat > "$V/CLAUDE.md" <<'MD'
# Vault

The operating rules live in `_meta/vault-operating-contract.md`; read it before writing anything.

## Preferences

_Empty until you set one._
MD
  fi
}

accept_offer() {  # F2's human-gated offer, accepted: the two lines appended, everything else kept
  local V="$1"
  local before; before="$(wc -c < "$V/CLAUDE.md")"
  printf '\n@_meta/vault-rule-card.md\n@_agent/reflexes.md\n' >> "$V/CLAUDE.md"
  local after; after="$(wc -c < "$V/CLAUDE.md")"
  [ "$after" -gt "$before" ] && grep -q 'read it before writing anything' "$V/CLAUDE.md"
}

transcript_dir() {  # the session transcripts for a project path (keyed by its REAL path, slugged)
  local V; V="$(cd "$1" && pwd -P)"
  echo "$HOME/.claude/projects/$(echo "$V" | sed 's|/|-|g')"
}

probe() {  # $1 = vault root, $2 = leg label, $3 = the prompt, $4 = present|absent (default present)
  local V="$1" LABEL="$2" PROMPT="$3" EXPECT="${4:-present}"
  local TD; TD="$(transcript_dir "$V")"
  local BEFORE; BEFORE="$(ls -1 "$TD" 2>/dev/null | wc -l | tr -d ' ')"
  local REPLY; REPLY="$(cd "$V" && claude -p "$PROMPT" 2>&1)"
  local T; T="$(ls -1t "$TD"/*.jsonl 2>/dev/null | head -1)"
  if [ -z "$T" ]; then fail "$LABEL: a transcript was written"; return; fi
  # the attachment record: one entry per delivered instruction file, written before any model turn
  local CARD RUNG
  CARD="$(grep -o '"path":"[^"]*vault-rule-card.md"' "$T" | sort -u | wc -l | tr -d ' ')"
  RUNG="$(grep -o '"path":"[^"]*_agent/reflexes.md"' "$T" | sort -u | wc -l | tr -d ' ')"
  local WANT=1; [ "$EXPECT" = "absent" ] && WANT=0
  ck "$LABEL: the attachment record names the CARD exactly $WANT time(s)" "$([ "$CARD" = "$WANT" ] && echo 1 || echo 0)" "entries=$CARD"
  ck "$LABEL: the attachment record names the RUNG exactly $WANT time(s)" "$([ "$RUNG" = "$WANT" ] && echo 1 || echo 0)" "entries=$RUNG"
  local GOT=0
  echo "$REPLY" | grep -q "$CANARY_CARD" && echo "$REPLY" | grep -q "$CANARY_RUNG" && GOT=1
  ck "$LABEL: the canaries are $EXPECT in the reply" "$([ "$GOT" = "$WANT" ] && echo 1 || echo 0)" \
     "$(echo "$REPLY" | tr '\n' ' ' | cut -c1-120)"
  echo "      transcript: $T   (dir had $BEFORE before)"
}

PROMPT='Two instruction files may have been delivered to you. Reply with exactly two lines: CARD=<the CANARY value from the rule-card, or UNKNOWN> and RUNG=<the CANARY value from the vault rung, or UNKNOWN>. Do not guess; do not read any file; answer only from what was delivered.'
SUMMON='First run the Skill tool for any available skill if one exists, then answer: reply with exactly two lines: CARD=<the CANARY value from the rule-card, or UNKNOWN> and RUNG=<the CANARY value from the vault rung, or UNKNOWN>.'
SUBAGENT='Spawn one Agent (subagent_type general-purpose) and ask it to report, from what was delivered to IT at its own start, the two CANARY values (the rule-card one and the vault rung one). Relay its answer as exactly two lines: CARD=<value|UNKNOWN> RUNG=<value|UNKNOWN>.'

A="${TMPDIR:-/tmp}/build-3-carrier-fresh"
B="${TMPDIR:-/tmp}/build-3-carrier-existing"

echo "== vault A (fresh — the §3 seed branch)"
seed_vault "$A" fresh
probe "$A" "leg 1 headless" "$PROMPT"
probe "$A" "leg 2 in-session summon" "$SUMMON"
probe "$A" "leg 3 Agent-tool subagent" "$SUBAGENT"

echo
echo "== vault B (existing — the never-clobber branch, F2's re-keyed offer)"
seed_vault "$B" existing
ck "B: the old offer key would NOT fire (the file already references the contract)" \
   "$(grep -q 'vault-operating-contract.md' "$B/CLAUDE.md" && echo 1 || echo 0)"
ck "B: the NEW key DOES fire (neither import line is present)" \
   "$(grep -q '^@_meta/vault-rule-card.md' "$B/CLAUDE.md" && echo 0 || echo 1)"
probe "$B" "leg 4 existing vault, offer NOT yet accepted (expect UNKNOWN twice)" "$PROMPT" absent
ck "B: accepting the offer preserves the existing prose byte-for-byte" "$(accept_offer "$B" && echo 1 || echo 0)"
probe "$B" "leg 5 existing vault, offer ACCEPTED" "$PROMPT"

echo
[ "$FAILS" = "0" ] && echo "all expectations hold" || echo "$FAILS expectation(s) FAILED"
exit $([ "$FAILS" = "0" ] && echo 0 || echo 1)
