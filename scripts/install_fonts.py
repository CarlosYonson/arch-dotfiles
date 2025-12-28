from pathlib import Path
import subprocess

DOTFILES = Path.home() / "dotfiles"
SRC = DOTFILES / "fonts"
DEST = Path.home() / ".local/share/fonts"

def run():
    DEST.parent.mkdir(parents=True, exist_ok=True)

    if DEST.exists() or DEST.is_symlink():
        DEST.unlink()
    DEST.symlink_to(SRC)

    subprocess.run(["fc-cache", "-rv"], check=True)

if __name__ == "__main__":
    run()