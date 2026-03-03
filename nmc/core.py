import os
import time
import subprocess
from pathlib import Path
from filesystem import directory as dir

def safe_rmtree(path: Path):
    subprocess.run(["rm", "-rf", str(path)], check=False)

def format_size(size):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

def find_node_modules(base_path: Path, days: int, min_size_mb: int):
    now = time.time()
    limit = days * 86400

    found = []

    for root, dirs, _ in os.walk(base_path):
        if "node_modules" in dirs:
            nm_path = Path(root) / "node_modules"

            try:
                last_access = nm_path.stat().st_atime

                if (now - last_access) > limit:
                    size = dir.get_size(str(nm_path))

                    if size >= min_size_mb * 1024 * 1024:
                        found.append((nm_path, size))

            except Exception:
                continue

    return found

def cleanup(found, dry_run: bool):
    for path, _ in found:
        if not dry_run:
            safe_rmtree(path)