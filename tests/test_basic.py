from argparse import Namespace
from nmc.core import find_node_modules, cleanup
from pathlib import Path
import os
import time


def create_fake_project(base: Path, days_old=40):
    proj = base / "fake_project"
    nm = proj / "node_modules"

    nm.mkdir(parents=True)
    fake_file = nm / "index.js"
    fake_file.write_text("console.log('test')")

    old_time = time.time() - (days_old * 86400)
    os.utime(nm, (old_time, old_time))

    return nm


def test_cleanup(tmp_path):
    nm = create_fake_project(tmp_path)

    found = find_node_modules(tmp_path, days=30, min_size_mb=0)
    cleanup(found, dry_run=False)

    assert not nm.exists()


def test_dry_run(tmp_path):
    nm = create_fake_project(tmp_path)

    found = find_node_modules(tmp_path, days=30, min_size_mb=0)
    cleanup(found, dry_run=True)

    assert nm.exists()