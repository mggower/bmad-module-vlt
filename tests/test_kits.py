import hashlib
import json

from conftest import commit_all, run_kits, write

RULES = "_meta/vault.md"
README = "resources/playbooks/README.md"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def lock(vault):
    return json.loads((vault / "_agent" / "kits.lock").read_text())


def lines(proc):
    return proc.stdout.strip().splitlines()


def seeded(vault, kits_dir):
    r = run_kits(vault, kits_dir, "seed")
    assert r.returncode == 0, r.stderr
    commit_all(vault, "seed")
    return r


def test_seed_copies_and_locks(vault, kits_dir):
    r = run_kits(vault, kits_dir, "seed")
    assert r.returncode == 0, r.stderr
    src = kits_dir / "core" / "files"
    assert (vault / RULES).read_bytes() == (src / RULES).read_bytes()
    assert (vault / README).read_bytes() == (src / README).read_bytes()
    lk = lock(vault)
    assert lk["schema"] == 1
    assert lk["kits"]["core"]["version"] == "1.0.0"
    assert lk["kits"]["core"]["files"][RULES] == sha(src / RULES)
    assert f"seeded {RULES}" in lines(r)


def test_seed_never_overwrites(vault, kits_dir):
    write(vault / RULES, "mine")
    r = run_kits(vault, kits_dir, "seed")
    assert r.returncode == 0, r.stderr
    assert (vault / RULES).read_text() == "mine"
    assert f"kept-yours {RULES}" in lines(r)
    # the lock still records what shipped, so pull can tell the two apart later
    assert lock(vault)["kits"]["core"]["files"][RULES] == sha(kits_dir / "core" / "files" / RULES)


def test_seed_twice_is_idempotent(vault, kits_dir):
    run_kits(vault, kits_dir, "seed")
    before = (vault / "_agent" / "kits.lock").read_bytes()
    r = run_kits(vault, kits_dir, "seed")
    assert r.returncode == 0
    assert lines(r) and all(l.startswith("same ") for l in lines(r))
    assert (vault / "_agent" / "kits.lock").read_bytes() == before


def test_state_table():
    from kits import state
    assert state("a", "a", "a") == "unchanged"
    assert state("a", "b", "b") == "unchanged"          # vault already matches the kit
    assert state(None, "a", None) == "new"
    assert state("a", None, "a") == "retired"
    assert state("a", "a", None) == "vault-removed"
    assert state("a", "b", None) == "vault-removed"
    assert state("a", "b", "a") == "shipped-changed"
    assert state("a", "a", "c") == "vault-changed"
    assert state("a", "b", "c") == "both-changed"
    assert state(None, "a", "c") == "both-changed"      # new in the kit, vault has its own


def test_status_after_kit_edit(vault, kits_dir):
    seeded(vault, kits_dir)
    write(kits_dir / "core" / "files" / RULES, "# rules v2\n")
    r = run_kits(vault, kits_dir, "status")
    assert r.returncode == 0, r.stderr
    assert f"shipped-changed core {RULES}" in lines(r)
    assert f"unchanged core {README}" in lines(r)


def test_deleted_vault_file_is_vault_removed_not_recreated(vault, kits_dir):
    seeded(vault, kits_dir)
    (vault / RULES).unlink()
    assert f"vault-removed core {RULES}" in lines(run_kits(vault, kits_dir, "status"))
    r = run_kits(vault, kits_dir, "seed")
    assert r.returncode == 0
    assert not (vault / RULES).exists()
    assert f"vault-removed core {RULES}" in lines(run_kits(vault, kits_dir, "status"))


def test_take_refuses_uncommitted_vault_edit(vault, kits_dir):
    seeded(vault, kits_dir)
    write(vault / RULES, "my uncommitted edit")
    write(kits_dir / "core" / "files" / RULES, "# rules v2\n")
    r = run_kits(vault, kits_dir, "take", RULES)
    assert r.returncode == 1
    assert "uncommitted" in r.stderr
    assert (vault / RULES).read_text() == "my uncommitted edit"


def test_take_applies_and_records(vault, kits_dir):
    seeded(vault, kits_dir)
    write(kits_dir / "core" / "files" / RULES, "# rules v2\n")
    r = run_kits(vault, kits_dir, "take", RULES)
    assert r.returncode == 0, r.stderr
    assert (vault / RULES).read_text() == "# rules v2\n"
    assert f"unchanged core {RULES}" in lines(run_kits(vault, kits_dir, "status"))


def test_take_restores_a_removed_file_when_asked(vault, kits_dir):
    seeded(vault, kits_dir)
    (vault / RULES).unlink()
    commit_all(vault, "rm")
    r = run_kits(vault, kits_dir, "take", RULES)
    assert r.returncode == 0, r.stderr
    assert (vault / RULES).read_text() == "# rules v1\n"


def test_leave_records_without_writing(vault, kits_dir):
    seeded(vault, kits_dir)
    write(vault / RULES, "mine now")
    commit_all(vault)
    write(kits_dir / "core" / "files" / RULES, "# rules v2\n")
    assert f"both-changed core {RULES}" in lines(run_kits(vault, kits_dir, "status"))
    r = run_kits(vault, kits_dir, "leave", RULES)
    assert r.returncode == 0, r.stderr
    assert (vault / RULES).read_text() == "mine now"
    assert f"vault-changed core {RULES}" in lines(run_kits(vault, kits_dir, "status"))


def test_missing_lock_stops_pull_commands(vault, kits_dir):
    for cmd in (["status"], ["take", RULES], ["leave", RULES]):
        r = run_kits(vault, kits_dir, *cmd)
        assert r.returncode == 2, cmd
        assert "run vlt-setup" in r.stderr
    assert not (vault / RULES).exists()


def test_corrupt_lock_stops(vault, kits_dir):
    write(vault / "_agent" / "kits.lock", "{")
    r = run_kits(vault, kits_dir, "status")
    assert r.returncode == 2
    assert "run vlt-setup" in r.stderr


def test_corrupt_lock_stops_seed_too(vault, kits_dir):
    write(vault / "_agent" / "kits.lock", "{")
    r = run_kits(vault, kits_dir, "seed")
    assert r.returncode == 2
    assert (vault / "_agent" / "kits.lock").read_text() == "{"


def test_retired_file_is_reported_and_kept(vault, kits_dir):
    seeded(vault, kits_dir)
    (kits_dir / "core" / "files" / RULES).unlink()
    r = run_kits(vault, kits_dir, "status")
    assert f"retired core {RULES}" in lines(r)
    assert (vault / RULES).read_text() == "# rules v1\n"


def test_new_kit_file_is_offered_not_written(vault, kits_dir):
    seeded(vault, kits_dir)
    write(kits_dir / "core" / "files" / "_meta" / "extra.md", "x\n")
    assert "new core _meta/extra.md" in lines(run_kits(vault, kits_dir, "status"))
    assert not (vault / "_meta" / "extra.md").exists()


def test_diff_shows_vault_against_kit(vault, kits_dir):
    seeded(vault, kits_dir)
    write(kits_dir / "core" / "files" / RULES, "# rules v2\n")
    r = run_kits(vault, kits_dir, "diff", RULES)
    assert r.returncode == 0, r.stderr
    assert "-# rules v1" in r.stdout and "+# rules v2" in r.stdout


def test_unknown_path_is_an_error(vault, kits_dir):
    seeded(vault, kits_dir)
    r = run_kits(vault, kits_dir, "take", "nope.md")
    assert r.returncode == 1
    assert "nope.md" in r.stderr


def test_status_json(vault, kits_dir):
    seeded(vault, kits_dir)
    r = run_kits(vault, kits_dir, "status", "--json")
    rows = json.loads(r.stdout)
    assert {"state": "unchanged", "kit": "core", "path": RULES} in rows


def test_path_with_spaces(vault, kits_dir):
    p = "resources/play books/x.md"
    write(kits_dir / "core" / "files" / p, "x\n")
    seeded(vault, kits_dir)
    assert (vault / p).read_text() == "x\n"
    assert f"unchanged core {p}" in lines(run_kits(vault, kits_dir, "status"))


def test_same_path_in_two_kits_is_refused(vault, kits_dir):
    write(kits_dir / "wiki" / "kit.yaml", "name: wiki\nversion: 1.0.0\n")
    write(kits_dir / "wiki" / "files" / RULES, "dup\n")
    r = run_kits(vault, kits_dir, "seed")
    assert r.returncode == 2
    assert RULES in r.stderr
