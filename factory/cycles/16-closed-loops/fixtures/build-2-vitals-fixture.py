"""Build a throwaway vault tree with six synthesized partners for the
`partners_over_activation_budget` derivation. Prints the fixture root."""
import sys, shutil, tempfile
from pathlib import Path

def w(p, text):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)

def words(n, seed="lorem"):
    return " ".join([seed] * n)

def build(root, tripwires_src):
    root = Path(root)
    w(root / "_bmad" / "config.yaml", "vlt:\n  vault_structure:\n")
    w(root / "_agent" / "log.md", "# Log\n\n## [2026-09-01 10:00] session (librarian) | a sitting\n")
    w(root / "_agent" / "backlog.md", "# Backlog\n\n## Open\n\n## Done\n")
    w(root / "resources" / "wiki" / "index.md", "# Index\n")
    w(root / "_agent" / "dispatch.md", "# Dispatch\n")
    shutil.copy(tripwires_src, root / "_agent" / "tripwires.yaml")

    P = root / "_agent" / "partners"
    S = root / ".claude" / "skills"

    # 1. heavy-identity: over on identity.md mass (posture full)
    w(S / "vlt-agent-heavy-identity" / "SKILL.md", words(2000))
    w(P / "heavy-identity" / "identity.md", "---\ntype: identity\npartner: heavy-identity\n---\n\n## Charter\n<what you want this partner for>\n\n## Self\n" + words(11000))
    w(P / "heavy-identity" / "reflexes.md", "---\ntype: reflexes\n---\n" + words(100))

    # 2. heavy-skill: over on SKILL.md mass
    w(S / "vlt-agent-heavy-skill" / "SKILL.md", words(13000))
    w(P / "heavy-skill" / "identity.md", "---\ntype: identity\npartner: heavy-skill\n---\n\n## Self\n" + words(200))
    w(P / "heavy-skill" / "reflexes.md", "---\ntype: reflexes\n---\n" + words(50))

    # 3. light: comfortably under
    w(S / "vlt-agent-light" / "SKILL.md", words(1000))
    w(P / "light" / "identity.md", "---\ntype: identity\npartner: light\n---\n\n## Self\n" + words(500))
    w(P / "light" / "reflexes.md", "---\ntype: reflexes\n---\n" + words(50))

    # 4. reflex-posture: full-set total OVER, reflexes-set total UNDER
    w(S / "vlt-agent-reflex-posture" / "SKILL.md", words(5000))
    w(P / "reflex-posture" / "identity.md", "---\ntype: identity\npartner: reflex-posture\nmemory: reflexes\n---\n\n## Self\n" + words(9000))
    w(P / "reflex-posture" / "reflexes.md", "---\ntype: reflexes\n---\n" + words(100))

    # 5. no-skill: SKILL.md unresolvable — words n/a, NOT counted as under
    w(P / "no-skill" / "identity.md", "---\ntype: identity\npartner: no-skill\n---\n\n## Self\n" + words(300))
    w(P / "no-skill" / "reflexes.md", "---\ntype: reflexes\n---\n" + words(20))

    # 6. with-casebook: has a casebook.md (bytes only; never wake-read), no reflexes.md
    w(S / "vlt-agent-with-casebook" / "SKILL.md", words(800))
    w(P / "with-casebook" / "identity.md", "---\ntype: identity\npartner: with-casebook\n---\n\n## Self\n" + words(400))
    w(P / "with-casebook" / "casebook.md", "---\ntype: casebook\npartner: with-casebook\n---\n\n### 2026-09-01 a case\n" + words(5000))
    return root

if __name__ == "__main__":
    print(build(tempfile.mkdtemp(prefix="vlt-fixture-"), sys.argv[1]))
