"""Launcher used only by the PyInstaller build.

Kept out of the package so `python -m windows_mcp` and the console script
stay untouched; the exe is a pure consumer of the library.
"""

from windows_mcp.__main__ import main

if __name__ == "__main__":
    main()
