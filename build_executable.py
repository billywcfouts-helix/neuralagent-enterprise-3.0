#!/usr/bin/env python3
"""
Build standalone executable for NeuralAgent Enterprise 3.0
Usage: python build_executable.py
"""
import os
import sys
import shutil
from pathlib import Path

def build():
    try:
        import PyInstaller.__main__
    except ImportError:
        print("PyInstaller not found. Installing...")
        os.system(f"{sys.executable} -m pip install pyinstaller")
        import PyInstaller.__main__

    project_root = Path(__file__).parent.resolve()
    gui_script = project_root / "gui" / "app.py"

    print("Building NeuralAgent Enterprise 3.0 executable...")

    for folder in ["build", "dist"]:
        if (project_root / folder).exists():
            shutil.rmtree(project_root / folder)

    PyInstaller.__main__.run([
        str(gui_script),
        "--name", "NeuralAgent-Enterprise-3.0",
        "--onefile",
        "--windowed",
        "--add-data", f"{project_root / 'core'}:core",
        "--add-data", f"{project_root / 'agents'}:agents",
        "--add-data", f"{project_root / 'tools'}:tools",
        "--add-data", f"{project_root / 'utils'}:utils",
        "--add-data", f"{project_root / 'memory'}:memory",
        "--add-data", f"{project_root / '.env.example'}:.",
        "--add-data", f"{project_root / 'README.md'}:.",
        "--hidden-import", "streamlit",
        "--hidden-import", "litellm",
        "--hidden-import", "pynput",
        "--hidden-import", "playwright",
        "--hidden-import", "pytesseract",
        "--hidden-import", "PIL",
        "--hidden-import", "mss",
        "--hidden-import", "loguru",
        "--hidden-import", "pydantic",
        "--collect-all", "streamlit",
        "--collect-all", "litellm",
        "--noconfirm",
        "--clean",
    ])

    print("\nBuild complete! Executable in dist/") 

if __name__ == "__main__":
    build()