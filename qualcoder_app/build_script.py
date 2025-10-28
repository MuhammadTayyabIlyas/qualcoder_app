import os
import subprocess
from pathlib import Path

# --- CONFIGURATION ---
APP_NAME = "QualCoderApp"
MAIN_SCRIPT = "app.py"
CORE_FILE = "qualcoder_core.py"
BAT_FILE = f"run_{APP_NAME.lower()}.bat"

# --- STEP 1: Install dependencies ---
print("📦 Installing dependencies...")
subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
subprocess.run(["pip", "install", "pyinstaller"], check=True)

# --- STEP 2: Build the standalone executable ---
print("🚀 Building the standalone Streamlit app...")
subprocess.run([
    "pyinstaller",
    "--onefile",
    "--noconfirm",
    "--clean",
    "--strip",
    "--add-data", f"{CORE_FILE};.",
    "--hidden-import", "streamlit",
    "--hidden-import", "pandas",
    "--hidden-import", "openpyxl",
    "--hidden-import", "PyPDF2",
    "--hidden-import", "python-docx",
    "--hidden-import", "sklearn",
    "--hidden-import", "PIL",
    MAIN_SCRIPT
], check=True)

# --- STEP 3: Create launcher .bat file ---
# Build the path to the generated EXE safely
exe_name = f"{Path(MAIN_SCRIPT).stem}.exe"
dist_path = Path("dist") / exe_name
bat_content = f"""@echo off
echo Starting {APP_NAME}...
cd /d "%~dp0"
if exist "dist\\{exe_name}" (
    start "" "dist\\{exe_name}"
) else (
    echo Error: Executable not found at dist\\{exe_name}
    echo Please run the build script first.
    pause
)
exit
"""

bat_path = Path(BAT_FILE)
with open(bat_path, "w") as f:
    f.write(bat_content)

print(f"\n✅ Build complete!")
print(f"Executable created at: dist/{MAIN_SCRIPT.replace('.py', '.exe')}")
print(f"Launcher created: {BAT_FILE}")

print("\n📂 To share:")
print("1️⃣ Copy the entire 'dist' folder and the .bat file.")
print("2️⃣ Your users can double-click the .bat file to launch the app.")
print("   Streamlit will open automatically in their default browser.")

