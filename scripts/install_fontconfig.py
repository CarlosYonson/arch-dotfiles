from pathlib import Path

from scripts.utils import ensure_symlink

CONTEXT = "[fontconfig]"
DOTFILES = Path.home() / "dotfiles"
SRC = DOTFILES / "fontconfig"
DEST = Path.home() / ".config/fontconfig"

def run(dry_run=False):
    ensure_symlink(
        src=SRC,
        dest=DEST,
        dry_run=dry_run
    )

if __name__ == "__main__":
    run()