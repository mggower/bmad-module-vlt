import shutil
import subprocess
import sys

import pytest

from conftest import REPO, write

CHECK_SRC = REPO / "kits" / "wiki" / "files" / "_agent" / "tools" / "wiki" / "check.py"
WIKI = "resources/wiki"


def page(extra="", drop=None):
    keys = {
        "type": "wiki", "created": "2026-01-01", "last_updated": "2026-01-02", "title": "T",
        "author": "agent", "trust": "draft", "verified_by": "ingest", "verified_at": "2026-01-02",
    }
    if drop:
        del keys[drop]
    body = "".join(f"{k}: {v}\n" for k, v in keys.items())
    return f"---\n{body}{extra}---\n# T\n"


INDEX = "---\ntype: index\ntitle: Wiki Index\n---\n# Wiki Index\n\n## Coffee\n- [[brewing]] · hub\n  - [[cold-brew]]\n"


@pytest.fixture
def wv(tmp_path):
    v = tmp_path / "vault"
    dest = v / "_agent" / "tools" / "wiki" / "check.py"
    dest.parent.mkdir(parents=True)
    shutil.copy(CHECK_SRC, dest)
    write(v / WIKI / "index.md", INDEX)
    write(v / WIKI / "brewing.md", page())
    write(v / WIKI / "cold-brew.md", page())
    return v


def run(v):
    return subprocess.run([sys.executable, str(v / "_agent/tools/wiki/check.py")],
                          capture_output=True, text=True, cwd="/")


def test_clean_wiki_passes(wv):
    r = run(wv)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "2 pages" in r.stdout


def test_missing_attestation_key_fails(wv):
    write(wv / WIKI / "brewing.md", page(drop="verified_by"))
    r = run(wv)
    assert r.returncode == 1
    assert "brewing.md" in r.stdout and "verified_by" in r.stdout


def test_empty_attestation_value_fails(wv):
    write(wv / WIKI / "brewing.md", page(drop="trust", extra="trust:\n"))
    r = run(wv)
    assert r.returncode == 1
    assert "brewing.md" in r.stdout and "trust" in r.stdout


def test_dangling_successor_fails(wv):
    write(wv / WIKI / "brewing.md", page(extra='superseded_by: "[[gone]]"\n'))
    r = run(wv)
    assert r.returncode == 1
    assert "brewing.md" in r.stdout and "gone" in r.stdout


def test_existing_successor_passes_in_either_spelling(wv):
    write(wv / WIKI / "brewing.md", page(extra='superseded_by: "[[cold-brew]]"\n'))
    assert run(wv).returncode == 0
    write(wv / WIKI / "brewing.md", page(extra="superseded_by: cold-brew.md\n"))
    assert run(wv).returncode == 0


def test_page_missing_from_index_fails(wv):
    write(wv / WIKI / "espresso.md", page())
    r = run(wv)
    assert r.returncode == 1
    assert "espresso.md" in r.stdout and "index" in r.stdout


def test_index_entry_without_page_fails(wv):
    write(wv / WIKI / "index.md", INDEX + "- [[ghost]]\n")
    r = run(wv)
    assert r.returncode == 1
    assert "ghost" in r.stdout


def test_index_row_with_alias_and_stub_section(wv):
    write(wv / WIKI / "index.md",
          INDEX.replace("[[cold-brew]]", "[[cold-brew|Cold brew]] · slow")
          + "\n## Stubs (linked, not yet written)\n\n- `aeropress` — awaiting a source.\n")
    assert run(wv).returncode == 0


def test_empty_wiki_passes(tmp_path):
    v = tmp_path / "vault"
    dest = v / "_agent" / "tools" / "wiki" / "check.py"
    dest.parent.mkdir(parents=True)
    shutil.copy(CHECK_SRC, dest)
    r = run(v)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "0 pages" in r.stdout
    (v / WIKI).mkdir(parents=True)
    assert run(v).returncode == 0


def test_pages_without_an_index_fail(wv):
    (wv / WIKI / "index.md").unlink()
    r = run(wv)
    assert r.returncode == 1
    assert "index.md" in r.stdout


def test_page_without_frontmatter_fails_cleanly(wv):
    write(wv / WIKI / "brewing.md", "# just a heading\n")
    r = run(wv)
    assert r.returncode == 1
    assert "brewing.md" in r.stdout
    assert "Traceback" not in r.stderr


def test_says_what_it_did_not_look_at(wv):
    assert "does not check" in run(wv).stdout
