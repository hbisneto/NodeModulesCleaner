import os
import time
import shutil
from pathlib import Path
from nmc.cli import main
# from .cli import main


def create_fake_project(base: Path, days_old=40):
    proj = base / "fake_project"
    nm = proj / "node_modules"

    nm.mkdir(parents=True)

    fake_file = nm / "index.js"
    fake_file.write_text("console.log('test')")

    old_time = time.time() - (days_old * 86400)
    os.utime(nm, (old_time, old_time))

    return nm


def test_cleanup(tmp_path, monkeypatch):
    nm = create_fake_project(tmp_path)

    monkeypatch.setattr("sys.argv", ["nmc", str(tmp_path), "--days", "30"])

    main()

    assert not nm.exists()


def test_dry_run(tmp_path, monkeypatch):
    nm = create_fake_project(tmp_path)

    monkeypatch.setattr("sys.argv", ["nmc", str(tmp_path), "--dry-run"])

    main()

    assert nm.exists()