# utils.py
from pathlib import Path
from datetime import datetime
import shutil

SRC_TEST = Path.home() / "dotfiles/tests/file_test.txt"
DEST_TEST = Path.home() / "dotfiles/tests/symlink_dir/file_test.txt"

def is_correct_symlink(dest: Path, src: Path):
    if not dest.is_symlink():
        return False
    
    try:
        return dest.resolve() == src.resolve()
    except FileNotFoundError:
        return False

def backup_path(path: Path, dry_run=False) -> Path:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup = path.with_name(f"{path.name}.bak.{timestamp}")

    if dry_run:
        print(f"[dry-run] Backup {path} -> {backup}")
        return backup

    shutil.move(str(path), str(backup))
    return backup

def ensure_symlink(src: Path, dest: Path, dry_run=False):
    if is_correct_symlink(dest, src):
        print(f"✅ {dest} is already pointing to {src}")
        return
    
    if dest.exists() or dest.is_symlink():
        backup_path(dest, dry_run=dry_run)

    if dry_run:
        print(f"[dry-run] ln -s {src} {dest}")
        return

    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.symlink_to(src)
    print(f"🔗 {dest} -> {src}")
