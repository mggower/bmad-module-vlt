# Pattern: auto-caption sources substitute *plausible real names*, and nothing in the ingest path can catch it

_Filed 2026-07-25 by the Librarian from **`vlt-core`**, after the failure mode fired a **third** time in
the same source family and produced a wiki contradiction in today's full lint. The vault has already
improvised two local workarounds; neither is mechanical, and both live where an upgrade won't carry
them. Classified **pattern** (a recurring source-class hazard), not a single defect._

## The failure mode, stated precisely

Auto-generated YouTube captions do not merely *mangle* proper nouns. They **substitute a different,
more famous real person from the same domain**. The distinction is the whole finding:

> A mangled spelling **announces itself**. A substituted real name **reads as clean data** and gets
> encoded as fact.

Measured instances from one 2026-07-15 episode (`vlt-core`, recorded as a source-class finding in
`_agent/research/2026-07-25-134816-nfc-west-preview-kimes-kelly.md:48-62`):

| Rendered as | Almost certainly is | Location |
|---|---|---|
| "Brian Schottenheimer" (×2) | the new Seahawks OC (unnamed in the audio) | line 33 |
| "Brian Flores" | the same unnamed Seahawks OC | line 59 |
| "Aaron Rodgers" | Aaron Donald | lines 281, 289 |

The same note contrasts these against the ordinary garble the vault already caveats — "Osa
Idigizuwa"/"Odigizuwa", "Judarian Price" — which is self-announcing and gets caught every time.

**The substitution is directional**: always *toward* the more famous figure in the same domain. That
is what makes it survive review — every substituted name is a plausible thing for the speaker to have
said, in a sentence that still parses.

## Why the existing caveat doesn't cover it

`vlt-core`'s vault-grown `ingest-youtube` capability already warns about proper nouns
(`_agent/partners/librarian/capabilities/ingest-youtube.md:102-103`):

> "Captions are the default — free, instant, no compute. They spell common words reliably but
> **butcher proper nouns** and carry no speaker labels (see attribution, below)."

"Butcher" frames the hazard as **corruption**, and the caveat's cross-reference goes to **speaker
attribution** — who said it — not **entity naming** — who they said it *about*. A reader holding that
caveat is watching for garbled strings. Substitution is invisible to that watch.

Factory-side, checked 2026-07-25 against v0.7.0 source: `skills/vlt-ingest/SKILL.md` handles transcript
sources (the prep-sub-agent split at `:50-54`, `trust: raw` at `:83`/`:114`) with **no proper-noun
guard of any kind**. Nothing cross-checks a new proper noun against what the wiki already knows.

## The cost, observed

1. **A wiki contradiction, in today's lint.** `los-angeles-rams` and `nfl-2026-offense-rankings` name
   the same Rams lineman's legal issue as **"Jonah Jackson"** and **"Alaric Jackson"** respectively —
   two different real players — from two episodes of the same programme. It surfaced as an unhandled
   cross-page contradiction, i.e. as a *knowledge* problem, when it is a *source-fidelity* problem.
2. **A named hole on a brand-new hub.** `seattle-seahawks` deliberately records its offensive
   coordinator's **role with no name**, because the transcript renders him as two different real,
   prominent coaches — one of which (Schottenheimer) collides with the vault's own well-sourced record
   of him as the *Cowboys'* head coach. The page is correct and unusable in the same breath.
3. **An open backlog item that a source can't close.** `vlt-core` carries "Name the Seahawks' 2026
   offensive coordinator" as a `knowledge-gap` — but it isn't a knowledge gap, it's caption damage.
4. **A prose warning doing a machine's job.** The vault wrote a **filing note into its own wiki index**
   (`_agent/wiki/index.md:191`) stating the rule in prose: *"a proper noun appearing exactly once in one
   of these transcripts is not sufficient grounding for a wiki claim, and where a name collides with an
   existing vault record, suspect the transcript before amending the record."* That is a genuinely good
   rule — invented locally, enforced by nobody, and living in a file no mechanism reads.

## Why this is module work, not vault work

Applying the capability's own test — *would fixing this change module source?* — yes, on every candidate
shape below. The hazard is **generic to caption-sourced ingest**, not specific to this vault, this
programme, or this domain: any vault ingesting talk-format video hits it, and the sports domain merely
makes it legible because proper nouns carry the payload.

Note the asymmetry that makes it worth shipping something: the vault **can** detect this class cheaply
(a name colliding with an existing wiki record is exactly the signal), but only if something looks.
Today nothing does, and the detection happens by a human noticing a contradiction two sweeps later.

## Candidate shapes (for the capture to weigh — not rulings)

1. **A new-proper-noun cross-check at ingest.** For `trust: raw` transcript sources, cross-check every
   *new* proper noun against existing wiki pages and **flag collisions before writing** — "this source
   says Schottenheimer coaches Seattle; the wiki says he coaches Dallas." Highest value, and it fires
   exactly where the damage enters. Cost: needs an entity pass over the source.
2. **A grounding-sufficiency rule in convention.** Codify `vlt-core`'s improvised index note: a proper
   noun appearing **once** in an auto-caption source is insufficient grounding for a wiki claim.
   Cheapest; pure prose; inherits the usual "rule with no bell" weakness the enforcement arc exists to
   fix — so probably wants pairing with 1 or 3.
3. **A `vlt-lint` check for entity collisions.** Same person recorded on two teams / in two
   incompatible roles in the same season. Catches it late but catches it *mechanically*, and lint is
   already the corpus-knowledge tier where cross-page checks live.
4. **Promote the caveat's framing.** Whatever else ships, the shipped wording should distinguish
   **mangling** (self-announcing, low risk) from **substitution** (self-concealing, high risk). The
   current "butcher proper nouns" phrasing actively misdirects the reader's attention.

Shapes 1 and 3 are complementary — 1 prevents, 3 catches what 1 misses.

## Honest limits of this filing

- **One vault, one programme, one domain.** All instances come from `vlt-core` ingesting the Mina Kimes
  Show. I cannot show this generalizes to other channels, though the mechanism (ASR language models
  biased toward frequent names) predicts it should, and predicts it worsens for *less* famous subjects.
- **"Almost certainly is" is inference, not verification.** The substitution table's right-hand column
  is the vault's reading from context; no roster source was consulted to confirm any of them. The
  Schottenheimer case is strong (it collides with a well-sourced vault record); the Aaron Donald one is
  contextual. **Nobody has verified the Jonah/Alaric Jackson pair either way** — one of those two is
  presumably correct and I do not know which.
- **The capability involved is vault-local and unshipped.** `ingest-youtube` is vault-grown, so its
  caveat wording is not module source. I cite it as *evidence that a careful local author already tried
  and still missed this*, not as a defect in shipped text. The shipped gap is `vlt-ingest`'s absence of
  any guard.
- **Frequency is three, in one family.** Enough to call a pattern, not enough to size the rate. I have
  not audited the other five episodes in the cluster for undetected substitutions — and by construction,
  undetected is the expected state.
- **Provenance guess, marked as a guess:** I suspect no guard exists because transcript ingest was
  designed around the *volume* problem (the prep-sub-agent split for context saturation) rather than the
  *fidelity* problem, so source-fidelity never got its own step. Unverified — I have not read the
  design history.

## Provenance

- Vault: `vlt-core` (0.7.0, factory machine). Six Kimes-show episodes now feed the NFL cluster via
  auto-captions.
- Evidence: `_agent/research/2026-07-25-134816-nfc-west-preview-kimes-kelly.md:48-62` (the substitution
  table), `_agent/wiki/index.md:191` (the improvised filing note), `_agent/wiki/seattle-seahawks.md`
  (the deliberately unnamed coordinator), and the 2026-07-25 full-lint contradiction report
  (Jonah/Alaric Jackson).
- Origin backlog item: "Consider a source-provenance rule for the auto-caption transcript family"
  (`capability-gap`, by: librarian), flagged in-vault as a module-feedback candidate on 2026-07-15 and
  filed here after its third firing.
- Companion filing, same sweep: `inbox/2026-07-25-160239-contradictions-have-no-drain.md` — the
  Jonah/Alaric contradiction is cited there as evidence for a *different* defect (lint's disposition
  model). Same symptom, two independent causes; capture may want to read them together.
