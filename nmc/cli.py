import argparse
from pathlib import Path
import nmc.about as about
from nmc.core import find_node_modules, cleanup, format_size

def run(args) -> int:
    base_path = Path(args.path).expanduser().resolve()

    if not base_path.exists():
        print("❌ Invalid path.")
        return 1
    
    if args.version:
        about.show_version()
        return 0

    print(f"\n🔍 Scanning: {base_path}")
    print(f"🕒 Filter: +{args.days} days | 📦 > {args.min_size} MB\n")

    found = find_node_modules(base_path, args.days, args.min_size)

    if not found:
        print("✨ Nothing to clean.")
        return 0

    total_space = sum(size for _, size in found)

    print(f"📦 Found: {len(found)} directories")
    print(f"💾 Potential space: {format_size(total_space)}\n")

    print("📂 Found directories:\n")
    for path, size in found:
        print(f"  • {path} ({format_size(size)})")

    print()

    if not args.dry_run and not args.yes:
        confirm = input("⚠️ Would you like to proceed with deletion? [y/N]: ").strip().lower()
        if confirm not in ("y", "yes"):
            print("❌ Canceled operation.")
            return 0

    if args.dry_run:
        for path, _ in found:
            print(f"🔎 [DRY] {path}")
    else:
        cleanup(found, args.dry_run)

    print("\n✅ Finalized!")
    print(f"📦 Directories removed: {len(found)}")
    print(f"💾 Space freed: {format_size(total_space)}")

    return 0


def main():
    parser = argparse.ArgumentParser(
        description="🧹 Automatic cleanup of forgotten node_modules"
    )

    # 
    parser.add_argument(
        "-v", "--version",
        action="store_true",
        help="Show version information"
    )

    # Where to scan
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Directory to scan (default: current directory)"
    )

    # Filters
    parser.add_argument(
        "--days",
        type=int,
        default=30,
        help="Ignore node_modules accessed within the last N days (default: 30)"
    )

    parser.add_argument(
        "--min-size",
        type=int,
        default=0,
        help="Minimum size in MB (default: 0)"
    )

    # Modes
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate the cleanup without deleting anything"
    )

    parser.add_argument(
        "-y", "--yes",
        action="store_true",
        help="Automatically confirm deletion"
    )

    args = parser.parse_args()
    raise SystemExit(run(args))


if __name__ == "__main__":
    main()