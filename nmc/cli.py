import argparse
import os
import shutil
import time
from pathlib import Path
from tqdm import tqdm


def format_size(size):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f}{unit}"
        size /= 1024


def get_size(path: Path):
    total = 0
    for f in path.rglob("*"):
        try:
            if f.is_file():
                total += f.stat().st_size
        except:
            pass
    return total


def main():
    parser = argparse.ArgumentParser(
        description="🧹 Limpeza automática de node_modules esquecidos"
    )

    parser.add_argument(
        "path", help="Diretório base para escanear", nargs="?", default="."
    )

    parser.add_argument("--days", type=int, default=30, help="Não acessado há X dias")

    parser.add_argument(
        "--min-size", type=int, default=0, help="Tamanho mínimo em MB"
    )

    parser.add_argument("--dry-run", action="store_true", help="Simula sem apagar")

    args = parser.parse_args()

    base_path = Path(args.path).expanduser().resolve()

    if not base_path.exists():
        print("❌ Caminho inválido.")
        return

    print(f"\n🔍 Escaneando: {base_path}")
    print(f"🕒 Filtro: +{args.days} dias | 📦 > {args.min_size}MB\n")

    now = time.time()
    limit = args.days * 86400

    found = []

    for root, dirs, _ in os.walk(base_path):
        if "node_modules" in dirs:
            nm_path = Path(root) / "node_modules"

            try:
                last_access = nm_path.stat().st_atime
                size = get_size(nm_path)

                if (now - last_access) > limit and size >= args.min_size * 1024 * 1024:
                    found.append((nm_path, size))

            except:
                pass

    if not found:
        print("✨ Nada para limpar.")
        return

    total_space = sum(size for _, size in found)

    print(f"📦 Encontrados: {len(found)} diretórios")
    print(f"💾 Espaço potencial: {format_size(total_space)}\n")

    for path, size in tqdm(found, desc="🧹 Limpando", unit="dir"):
        if args.dry_run:
            print(f"🔎 [DRY] {path} ({format_size(size)})")
        else:
            shutil.rmtree(path, ignore_errors=True)

    print("\n✅ Finalizado!")
    print(f"📦 Diretórios: {len(found)}")
    print(f"💾 Espaço liberado: {format_size(total_space)}")


if __name__ == "__main__":
    main()