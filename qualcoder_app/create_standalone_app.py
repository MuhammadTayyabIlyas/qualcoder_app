"""
Standalone Web App Creator for QualCoder Pro
Creates a self-contained web application package
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path
import zipfile
import json

class StandaloneAppCreator:
    def __init__(self):
        self.app_name = "QualCoderPro"
        self.version = "1.0.0"
        self.dist_folder = Path("dist_standalone")
        self.app_folder = self.dist_folder / self.app_name
        
    def create_directory_structure(self):
        """Create the directory structure for the standalone app"""
        print("📁 Creating directory structure...")
        
        # Remove existing dist folder
        if self.dist_folder.exists():
            shutil.rmtree(self.dist_folder)
        
        # Create main directories
        self.app_folder.mkdir(parents=True, exist_ok=True)
        (self.app_folder / "assets").mkdir(exist_ok=True)
        (self.app_folder / "outputs").mkdir(exist_ok=True)
        (self.app_folder / "examples").mkdir(exist_ok=True)
        
        print(f"✅ Created directory structure at: {self.app_folder}")
    
    def copy_application_files(self):
        """Copy all necessary application files"""
        print("📋 Copying application files...")
        
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
                print(f"  ✅ Copied {file}")
            else:
                print(f"  ⚠️  {file} not found, skipping")
        
        # Copy example files
        if Path("examples").exists():
            shutil.copytree("examples", self.app_folder / "examples", dirs_exist_ok=True)
            print("  ✅ Copied examples folder")
        
        # Copy image if exists
        if Path("Tayyab.png").exists():
            shutil.copy2("Tayyab.png", self.app_folder)
            print("  ✅ Copied Tayyab.png")
    
    def create_launcher_scripts(self):
        """Create launcher scripts for different platforms"""
        print("🚀 Creating launcher scripts...")
        
        # Windows batch file
        windows_bat = self.app_folder / "run_app.bat"
        with open(windows_bat, 'w') as f:
            f.write(f'''@echo off
echo ========================================
echo    {self.app_name} v{self.version}
echo ========================================
echo.

cd /d "%~dp0"

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

REM Install requirements
echo Installing required packages...
python -m pip install -r requirements.txt --quiet

REM Run the application
echo Starting {self.app_name}...
echo This will open in your web browser at: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

python -m streamlit run app.py --server.headless true --server.port 8501

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

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "ERROR: Python is not installed or not in PATH"
        echo "Please install Python from: https://www.python.org/downloads/"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

# Install requirements
echo "Installing required packages..."
$PYTHON_CMD -m pip install -r requirements.txt --quiet

# Run the application
echo "Starting {self.app_name}..."
echo "This will open in your web browser at: http://localhost:8501"
echo
echo "Press Ctrl+C to stop the application"
echo

$PYTHON_CMD -m streamlit run app.py --server.headless true --server.port 8501
''')
        
        # Make shell script executable
        try:
            os.chmod(linux_sh, 0o755)
        except:
            pass
        
        print("  ✅ Created Windows launcher (run_app.bat)")
        print("  ✅ Created Linux/Mac launcher (run_app.sh)")
    
    def create_installer_script(self):
        """Create an installer script for easy setup"""
        print("📦 Creating installer script...")
        
        installer_content = f'''"""
{self.app_name} v{self.version} - Installer Script
This script will install all dependencies and set up the application
"""

import subprocess
import sys
import os
from pathlib import Path

def install_requirements():
    """Install all required packages"""
    print("📦 Installing required packages...")
    
    requirements = [
        "streamlit>=1.20.0",
        "pandas>=1.5",
        "openpyxl>=3.0",
        "python-docx>=0.8.11",
        "PyPDF2>=3.0.0",
        "scikit-learn>=1.2",
        "Pillow>=9.0.0"
    ]
    
    for req in requirements:
        try:
            print(f"Installing {{req}}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", req])
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install {{req}}: {{e}}")
            return False
    
    print("✅ All packages installed successfully!")
    return True

def main():
    print("=" * 50)
    print(f"  {self.app_name} v{self.version} - Installer")
    print("=" * 50)
    print()
    
    if install_requirements():
        print()
        print("🎉 Installation completed successfully!")
        print()
        print("To run the application:")
        print("  Windows: Double-click 'run_app.bat'")
        print("  Linux/Mac: Run './run_app.sh'")
        print("  Or manually: streamlit run app.py")
        print()
        print("The app will open at: http://localhost:8501")
    else:
        print("❌ Installation failed. Please check the error messages above.")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
'''
        
        installer_path = self.app_folder / "install.py"
        with open(installer_path, 'w', encoding='utf-8') as f:
            f.write(installer_content)
        
        print("  ✅ Created installer script (install.py)")
    
    def create_readme(self):
        """Create a comprehensive README for the standalone app"""
        print("📖 Creating README...")
        
        readme_content = f'''# {self.app_name} v{self.version}

A standalone web application for qualitative coding analysis with 3-stage processing pipeline.

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Internet connection (for initial package installation)

### Installation & Running

#### Option 1: Automatic Setup (Recommended)
1. **Windows**: Double-click `run_app.bat`
2. **Linux/Mac**: Run `./run_app.sh` in terminal

#### Option 2: Manual Setup
1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   streamlit run app.py
   ```

#### Option 3: Using Installer
1. Run the installer:
   ```bash
   python install.py
   ```
2. Then use Option 1 or 2 above

### 🌐 Accessing the Application
- The app will automatically open in your default web browser
- If it doesn't open automatically, go to: http://localhost:8501
- To stop the application, press `Ctrl+C` in the terminal/command prompt

## 📋 Features

- **3-Stage Qualitative Coding**: Initial coding, pattern analysis, and theme generation
- **Multiple File Formats**: Support for DOCX, PDF, and TXT files
- **NLP Keyword Suggestions**: TF-IDF based keyword extraction
- **Interactive Dashboard**: Modern Streamlit-based interface
- **Export Capabilities**: Excel files and ZIP archives
- **Offline Processing**: All analysis performed locally

## 📁 File Structure

```
{self.app_name}/
├── app.py                 # Main Streamlit application
├── qualcoder_core.py      # Core processing functions
├── requirements.txt       # Python dependencies
├── codebook.json         # Default coding framework
├── run_app.bat           # Windows launcher
├── run_app.sh            # Linux/Mac launcher
├── install.py            # Installer script
├── README.md             # This file
├── assets/               # Application assets
├── outputs/              # Generated analysis results
└── examples/             # Sample files
```

## 🔧 Troubleshooting

### Python Not Found
- Install Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

### Package Installation Fails
- Check your internet connection
- Try running: `pip install --upgrade pip`
- Then run the installer again

### Port Already in Use
- The app uses port 8501 by default
- If busy, it will automatically try port 8502, 8503, etc.
- Or manually specify: `streamlit run app.py --server.port 8502`

### Browser Doesn't Open
- Manually navigate to http://localhost:8501
- Check if your firewall is blocking the connection

## 📞 Support

For technical support or questions:
- Email: MuhammadTayyab.Ilyas@autonoma.cat
- Twitter: @tayyabcheema777
- LinkedIn: tayyabcheema777

## 📄 License

© 2024 Muhammad Tayyab Ilyas
PhD Student, Universitat Autònoma de Barcelona

## 🔄 Updates

To update the application:
1. Download the latest version
2. Replace the files in this directory
3. Run the installer again: `python install.py`
'''
        
        readme_path = self.app_folder / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        print("  ✅ Created comprehensive README.md")
    
    def create_zip_package(self):
        """Create a ZIP package for easy distribution"""
        print("📦 Creating ZIP package...")
        
        zip_path = self.dist_folder / f"{self.app_name}_v{self.version}.zip"
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(self.app_folder):
                for file in files:
                    file_path = Path(root) / file
                    arcname = file_path.relative_to(self.app_folder)
                    zipf.write(file_path, arcname)
        
        print(f"  ✅ Created ZIP package: {zip_path}")
        return zip_path
    
    def create_all(self):
        """Create the complete standalone application package"""
        print("🚀 Creating standalone web application package...")
        print("=" * 60)
        
        try:
            self.create_directory_structure()
            self.copy_application_files()
            self.create_launcher_scripts()
            self.create_installer_script()
            self.create_readme()
            zip_path = self.create_zip_package()
            
            print("\n" + "=" * 60)
            print("🎉 Standalone application created successfully!")
            print("=" * 60)
            print(f"📁 Application folder: {self.app_folder}")
            print(f"📦 ZIP package: {zip_path}")
            print()
            print("📋 To distribute:")
            print("1. Share the ZIP file with users")
            print("2. Users extract and run 'run_app.bat' (Windows) or './run_app.sh' (Linux/Mac)")
            print("3. Or users can run 'python install.py' for manual setup")
            print()
            print("🌐 The app will run locally and open in the user's web browser")
            
        except Exception as e:
            print(f"❌ Error creating standalone app: {e}")
            return False
        
        return True

def main():
    creator = StandaloneAppCreator()
    creator.create_all()

if __name__ == "__main__":
    main()
