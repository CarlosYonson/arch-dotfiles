from pathlib import Path
import shutil

CONTEXT = "[fontconfig]"
DOTFILES = Path.home() / "dotfiles"
SRC = DOTFILES / "fontconfig"
DEST = Path.home() / ".config/fontconfig"

def run():
    DEST.parent.mkdir(parents=True, exist_ok=True)

    if DEST.is_file() or DEST.is_symlink():
        print(f"{CONTEXT} ⚠️ A file or symlink already exists in the path.")
        DEST.unlink()
        print(f"{CONTEXT} 🗑️ Deleting...")
    elif DEST.is_dir():
        print(f"{CONTEXT} ⚠️ A directory already exists in the path.")
        shutil.rmtree(DEST)
        print(f"{CONTEXT} 🗑️ Deleting...")

    
    DEST.symlink_to(SRC)
    print(f"{CONTEXT} ✅ Symlink created succesfully.")

if __name__ == "__main__":
    run()