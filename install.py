#!/usr/bin/env python3
from scripts.install_fontconfig import run as install_fontconfig
from scripts.install_fonts import run as install_fonts

def main(dry_run=False):
    install_fontconfig(dry_run=dry_run)
    install_fonts(dry_run=dry_run)

if __name__ == "__main__":
    main(dry_run=True)