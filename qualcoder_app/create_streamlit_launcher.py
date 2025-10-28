"""
Alternative launcher creation script for Streamlit apps
This creates a more reliable bat file for running Streamlit apps
"""

import os
import subprocess
from pathlib import Path

# --- CONFIGURATION ---
APP_NAME = "QualCoderApp"
MAIN_SCRIPT = "app.py"
BAT_FILE = f"run_{APP_NAME.lower()}.bat"

def create_streamlit_launcher():
    """Create a bat file that runs the Streamlit app directly"""
    
    # Check if requirements are installed
    try:
        import streamlit
        print("✅ Streamlit is installed")
    except ImportError:
        print("❌ Streamlit not found. Installing requirements...")
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
    
    # Create the bat file content
    bat_content = f"""@echo off
echo Starting {APP_NAME}...
echo.
echo This will open your web browser automatically.
echo If it doesn't open, go to: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

cd /d "%~dp0"

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Check if the main script exists
if not exist "{MAIN_SCRIPT}" (
    echo Error: {MAIN_SCRIPT} not found in current directory
    echo Please make sure you're running this from the correct folder
    pause
    exit /b 1
)

REM Run the Streamlit app
echo Starting Streamlit server...
streamlit run {MAIN_SCRIPT} --server.headless true --server.port 8501

pause
"""

    # Write the bat file
    bat_path = Path(BAT_FILE)
    with open(bat_path, "w") as f:
        f.write(bat_content)
    
    print(f"✅ Launcher created: {BAT_FILE}")
    print(f"📂 Location: {bat_path.absolute()}")
    print("\n🚀 To use:")
    print("1. Double-click the .bat file")
    print("2. The app will open in your default browser")
    print("3. Press Ctrl+C in the command window to stop")

if __name__ == "__main__":
    create_streamlit_launcher()


