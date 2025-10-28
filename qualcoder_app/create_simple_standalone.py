"""
Simple Standalone App Creator for QualCoder Pro
Creates a self-contained web application package without emoji characters
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path
import zipfile

class SimpleStandaloneCreator:
    def __init__(self):
        self.app_name = "QualCoderPro"
        self.version = "1.0.0"
        self.dist_folder = Path("dist_standalone")
        self.app_folder = self.dist_folder / self.app_name
        
    def create_directory_structure(self):
        """Create the directory structure for the standalone app"""
        print("Creating directory structure...")
        
        # Remove existing dist folder
        if self.dist_folder.exists():
            shutil.rmtree(self.dist_folder)
        
        # Create main directories
        self.app_folder.mkdir(parents=True, exist_ok=True)
        (self.app_folder / "assets").mkdir(exist_ok=True)
        (self.app_folder / "outputs").mkdir(exist_ok=True)
        (self.app_folder / "examples").mkdir(exist_ok=True)
        
        print(f"Created directory structure at: {self.app_folder}")
    
    def copy_application_files(self):
        """Copy all necessary application files"""
        print("Copying application files...")
        
        files_to_copy = [
            "app.py",
            "qualcoder_core.py", 
            "requirements.txt",
            "codebook.json",
            "README.md"
        ]
        
        for file in files_to_copy:
            if Path(file).exists():
                shutil.copy2(file, self.app_folder)
                print(f"  Copied {file}")
            else:
                print(f"  {file} not found, skipping")
        
        # Copy example files
        if Path("examples").exists():
            shutil.copytree("examples", self.app_folder / "examples", dirs_exist_ok=True)
            print("  Copied examples folder")
        
        # Copy image if exists
        if Path("Tayyab.png").exists():
            shutil.copy2("Tayyab.png", self.app_folder)
            print("  Copied Tayyab.png")
    
    def create_launcher_scripts(self):
        """Create launcher scripts for different platforms"""
        print("Creating launcher scripts...")
        
        # Windows batch file
        windows_bat = self.app_folder / "run_app.bat"
        with open(windows_bat, 'w') as f:
            f.write(f'''@echo off
echo ========================================
echo    {self.app_name} v{self.version}
echo ========================================
echo.

cd /d "%~dp0"

REM Check if the main script exists
if not exist "app.py" (
    echo ERROR: app.py not found in current directory
    echo Please make sure you're running this from the correct folder
    echo Current directory: %CD%
    echo.
    pause
    exit /b 1
)

REM Try different Python executables
echo Checking for Python installation...

REM Try python
python --version >nul 2>&1
if not errorlevel 1 (
    echo Found: python
    set PYTHON_CMD=python
    goto :run_app
)

REM Try python3
python3 --version >nul 2>&1
if not errorlevel 1 (
    echo Found: python3
    set PYTHON_CMD=python3
    goto :run_app
)

REM Try py (Python Launcher for Windows)
py --version >nul 2>&1
if not errorlevel 1 (
    echo Found: py
    set PYTHON_CMD=py
    goto :run_app
)

REM If no Python found
echo.
echo ERROR: Python is not installed or not in PATH
echo.
echo Please install Python from: https://www.python.org/downloads/
echo Make sure to check "Add Python to PATH" during installation
echo.
echo After installing Python, run this file again.
echo.
pause
exit /b 1

:run_app
echo.
echo Starting {self.app_name}...
echo This will open your web browser automatically.
echo If it doesn't open, go to: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

REM Check if requirements are installed
echo Checking dependencies...
%PYTHON_CMD% -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    %PYTHON_CMD% -m pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install requirements
        echo Please check your internet connection and try again
        pause
        exit /b 1
    )
)

REM Run the Streamlit app
echo Starting Streamlit server...
%PYTHON_CMD% -m streamlit run app.py --server.headless true --server.port 8501

echo.
echo Application stopped.
pause
''')
        
        # Linux/Mac shell script
        linux_sh = self.app_folder / "run_app.sh"
        with open(linux_sh, 'w') as f:
            f.write(f'''#!/bin/bash
echo "========================================"
echo "    {self.app_name} v{self.version}"
echo "========================================"
echo

# Change to script directory
cd "$(dirname "$0")"

# Check if the main script exists
if [ ! -f "app.py" ]; then
    echo "ERROR: app.py not found in current directory"
    echo "Please make sure you're running this from the correct folder"
    echo "Current directory: $(pwd)"
    exit 1
fi

# Try different Python executables
echo "Checking for Python installation..."

# Try python3 first
if command -v python3 &> /dev/null; then
    echo "Found: python3"
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    echo "Found: python"
    PYTHON_CMD="python"
else
    echo "ERROR: Python is not installed or not in PATH"
    echo "Please install Python from: https://www.python.org/downloads/"
    exit 1
fi

echo
echo "Starting {self.app_name}..."
echo "This will open in your web browser at: http://localhost:8501"
echo
echo "Press Ctrl+C to stop the application"
echo

# Check if requirements are installed
echo "Checking dependencies..."
$PYTHON_CMD -c "import streamlit" &> /dev/null
if [ $? -ne 0 ]; then
    echo "Installing required packages..."
    $PYTHON_CMD -m pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to install requirements"
        echo "Please check your internet connection and try again"
        exit 1
    fi
fi

# Run the Streamlit app
echo "Starting Streamlit server..."
$PYTHON_CMD -m streamlit run app.py --server.headless true --server.port 8501
''')
        
        # Make shell script executable
        try:
            os.chmod(linux_sh, 0o755)
        except:
            pass
        
        print("  Created Windows launcher (run_app.bat)")
        print("  Created Linux/Mac launcher (run_app.sh)")
    
    def create_readme(self):
        """Create a comprehensive README for the standalone app"""
        print("Creating README...")
        
        readme_content = f'''# {self.app_name} v{self.version}

A standalone web application for qualitative coding analysis with 3-stage processing pipeline.

## Quick Start

### Prerequisites
- Python 3.7 or higher
- Internet connection (for initial package installation)

### Running the Application

#### Windows
1. Double-click `run_app.bat`
2. The app will open automatically in your web browser

#### Linux/Mac
1. Open terminal in the application folder
2. Run: `./run_app.sh`
3. The app will open automatically in your web browser

#### Manual Setup
1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   streamlit run app.py
   ```

### Accessing the Application
- The app will automatically open in your default web browser
- If it doesn't open automatically, go to: http://localhost:8501
- To stop the application, press Ctrl+C in the terminal/command prompt

## Features

- **3-Stage Qualitative Coding**: Initial coding, pattern analysis, and theme generation
- **Multiple File Formats**: Support for DOCX, PDF, and TXT files
- **NLP Keyword Suggestions**: TF-IDF based keyword extraction
- **Interactive Dashboard**: Modern Streamlit-based interface
- **Export Capabilities**: Excel files and ZIP archives
- **Offline Processing**: All analysis performed locally

## File Structure

```
{self.app_name}/
├── app.py                 # Main Streamlit application
├── qualcoder_core.py      # Core processing functions
├── requirements.txt       # Python dependencies
├── codebook.json         # Default coding framework
├── run_app.bat           # Windows launcher
├── run_app.sh            # Linux/Mac launcher
├── README.md             # This file
├── assets/               # Application assets
├── outputs/              # Generated analysis results
└── examples/             # Sample files
```

## Troubleshooting

### Python Not Found
- Install Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

### Package Installation Fails
- Check your internet connection
- Try running: `pip install --upgrade pip`
- Then run the launcher again

### Port Already in Use
- The app uses port 8501 by default
- If busy, it will automatically try port 8502, 8503, etc.
- Or manually specify: `streamlit run app.py --server.port 8502`

### Browser Doesn't Open
- Manually navigate to http://localhost:8501
- Check if your firewall is blocking the connection

## Support

For technical support or questions:
- Email: MuhammadTayyab.Ilyas@autonoma.cat
- Twitter: @tayyabcheema777
- LinkedIn: tayyabcheema777

## License

© 2024 Muhammad Tayyab Ilyas
PhD Student, Universitat Autònoma de Barcelona
'''
        
        readme_path = self.app_folder / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        print("  Created comprehensive README.md")
    
    def create_zip_package(self):
        """Create a ZIP package for easy distribution"""
        print("Creating ZIP package...")
        
        zip_path = self.dist_folder / f"{self.app_name}_v{self.version}.zip"
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(self.app_folder):
                for file in files:
                    file_path = Path(root) / file
                    arcname = file_path.relative_to(self.app_folder)
                    zipf.write(file_path, arcname)
        
        print(f"  Created ZIP package: {zip_path}")
        return zip_path
    
    def create_all(self):
        """Create the complete standalone application package"""
        print("Creating standalone web application package...")
        print("=" * 60)
        
        try:
            self.create_directory_structure()
            self.copy_application_files()
            self.create_launcher_scripts()
            self.create_readme()
            zip_path = self.create_zip_package()
            
            print("\n" + "=" * 60)
            print("Standalone application created successfully!")
            print("=" * 60)
            print(f"Application folder: {self.app_folder}")
            print(f"ZIP package: {zip_path}")
            print()
            print("To distribute:")
            print("1. Share the ZIP file with users")
            print("2. Users extract and run 'run_app.bat' (Windows) or './run_app.sh' (Linux/Mac)")
            print()
            print("The app will run locally and open in the user's web browser")
            
        except Exception as e:
            print(f"Error creating standalone app: {e}")
            return False
        
        return True

def main():
    creator = SimpleStandaloneCreator()
    creator.create_all()

if __name__ == "__main__":
    main()

