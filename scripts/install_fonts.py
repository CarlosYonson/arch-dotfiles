from pathlib import Path
import subprocess

from scripts.utils import ensure_symlink

DOTFILES = Path.home() / "dotfiles"
SRC = DOTFILES / "fonts"
DEST = Path.home() / ".local/share/fonts"

def run(dry_run=False):
    ensure_symlink(
        src=SRC,
        dest=DEST,
        dry_run=dry_run
    )

    if dry_run:
        print(f"[dry-run] fc-cache -rv")
        return

    subprocess.run(["fc-cache", "-rv"], check=True)

if __name__ == "__main__":
    run()