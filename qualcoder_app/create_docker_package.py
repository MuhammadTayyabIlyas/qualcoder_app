"""
Docker Package Creator for QualCoder Pro
Creates a Docker-based standalone web application
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path
import zipfile

class DockerPackageCreator:
    def __init__(self):
        self.app_name = "QualCoderPro-Docker"
        self.version = "1.0.0"
        self.docker_folder = Path("dist_docker")
        self.package_folder = self.docker_folder / self.app_name
        
    def create_docker_package(self):
        """Create a complete Docker package"""
        print("🐳 Creating Docker package...")
        
        # Create directory structure
        if self.docker_folder.exists():
            shutil.rmtree(self.docker_folder)
        
        self.package_folder.mkdir(parents=True, exist_ok=True)
        
        # Copy necessary files
        files_to_copy = [
            "app.py",
            "qualcoder_core.py",
            "requirements.txt",
            "codebook.json",
            "README.md",
            "Dockerfile",
            "docker-compose.yml"
        ]
        
        for file in files_to_copy:
            if Path(file).exists():
                shutil.copy2(file, self.package_folder)
                print(f"  ✅ Copied {file}")
        
        # Copy image if exists
        if Path("Tayyab.png").exists():
            shutil.copy2("Tayyab.png", self.package_folder)
            print("  ✅ Copied Tayyab.png")
        
        # Create directories
        (self.package_folder / "outputs").mkdir(exist_ok=True)
        (self.package_folder / "examples").mkdir(exist_ok=True)
        
        # Create Docker run scripts
        self.create_docker_scripts()
        
        # Create comprehensive README
        self.create_docker_readme()
        
        # Create ZIP package
        zip_path = self.create_zip_package()
        
        print(f"\n✅ Docker package created: {zip_path}")
        return zip_path
    
    def create_docker_scripts(self):
        """Create scripts to run Docker container"""
        
        # Windows batch file
        windows_bat = self.package_folder / "run_docker.bat"
        with open(windows_bat, 'w') as f:
            f.write(f'''@echo off
echo ========================================
echo    {self.app_name} v{self.version} - Docker
echo ========================================
echo.

cd /d "%~dp0"

REM Check if Docker is installed
docker --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Docker is not installed
    echo.
    echo Please install Docker Desktop from: https://www.docker.com/products/docker-desktop
    echo After installation, restart your computer and try again.
    echo.
    pause
    exit /b 1
)

echo Building Docker image...
docker build -t qualcoder-pro .

if errorlevel 1 (
    echo ERROR: Failed to build Docker image
    pause
    exit /b 1
)

echo.
echo Starting QualCoder Pro...
echo The application will be available at: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

docker run -p 8501:8501 -v "%CD%\\outputs:/app/outputs" -v "%CD%\\examples:/app/examples" qualcoder-pro

pause
''')
        
        # Linux/Mac shell script
        linux_sh = self.package_folder / "run_docker.sh"
        with open(linux_sh, 'w') as f:
            f.write(f'''#!/bin/bash
echo "========================================"
echo "    {self.app_name} v{self.version} - Docker"
echo "========================================"
echo

# Change to script directory
cd "$(dirname "$0")"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "ERROR: Docker is not installed"
    echo "Please install Docker from: https://www.docker.com/products/docker-desktop"
    exit 1
fi

echo "Building Docker image..."
docker build -t qualcoder-pro .

if [ $? -ne 0 ]; then
    echo "ERROR: Failed to build Docker image"
    exit 1
fi

echo
echo "Starting QualCoder Pro..."
echo "The application will be available at: http://localhost:8501"
echo
echo "Press Ctrl+C to stop the application"
echo

docker run -p 8501:8501 -v "$(pwd)/outputs:/app/outputs" -v "$(pwd)/examples:/app/examples" qualcoder-pro
''')
        
        # Make shell script executable
        try:
            os.chmod(linux_sh, 0o755)
        except:
            pass
        
        # Docker Compose script
        compose_bat = self.package_folder / "run_docker_compose.bat"
        with open(compose_bat, 'w') as f:
            f.write(f'''@echo off
echo ========================================
echo    {self.app_name} v{self.version} - Docker Compose
echo ========================================
echo.

cd /d "%~dp0"

REM Check if Docker Compose is available
docker-compose --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Docker Compose is not available
    echo Please make sure Docker Desktop is installed and running
    echo.
    pause
    exit /b 1
)

echo Starting QualCoder Pro with Docker Compose...
echo The application will be available at: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

docker-compose up --build

pause
''')
        
        print("  ✅ Created Docker run scripts")
    
    def create_docker_readme(self):
        """Create comprehensive README for Docker package"""
        
        readme_content = f'''# {self.app_name} v{self.version} - Docker Edition

A containerized web application for qualitative coding analysis with 3-stage processing pipeline.

## 🐳 Docker Quick Start

### Prerequisites
- Docker Desktop installed and running
- Internet connection (for initial image build)

### Running the Application

#### Option 1: Docker Run (Recommended)
1. **Windows**: Double-click `run_docker.bat`
2. **Linux/Mac**: Run `./run_docker.sh` in terminal

#### Option 2: Docker Compose
1. **Windows**: Double-click `run_docker_compose.bat`
2. **Linux/Mac**: Run `docker-compose up --build`

#### Option 3: Manual Docker Commands
```bash
# Build the image
docker build -t qualcoder-pro .

# Run the container
docker run -p 8501:8501 -v "$(pwd)/outputs:/app/outputs" qualcoder-pro
```

### 🌐 Accessing the Application
- The app will be available at: http://localhost:8501
- Output files will be saved to the `outputs` folder
- To stop the application, press `Ctrl+C` in the terminal

## 📋 Features

- **Fully Containerized**: No Python installation required
- **Cross-Platform**: Works on Windows, Mac, and Linux
- **Isolated Environment**: All dependencies contained within the container
- **Persistent Storage**: Output files saved to host machine
- **Easy Updates**: Just rebuild the Docker image

## 🔧 Docker Commands

### Build Image
```bash
docker build -t qualcoder-pro .
```

### Run Container
```bash
docker run -p 8501:8501 qualcoder-pro
```

### Run with Volume Mounting
```bash
docker run -p 8501:8501 -v "$(pwd)/outputs:/app/outputs" qualcoder-pro
```

### Stop Container
```bash
docker stop $(docker ps -q --filter ancestor=qualcoder-pro)
```

### Remove Container
```bash
docker rm $(docker ps -aq --filter ancestor=qualcoder-pro)
```

### Remove Image
```bash
docker rmi qualcoder-pro
```

## 📁 File Structure

```
{self.app_name}/
├── app.py                 # Main Streamlit application
├── qualcoder_core.py      # Core processing functions
├── requirements.txt       # Python dependencies
├── codebook.json         # Default coding framework
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── run_docker.bat        # Windows Docker launcher
├── run_docker.sh         # Linux/Mac Docker launcher
├── run_docker_compose.bat # Windows Docker Compose launcher
├── README.md             # This file
├── outputs/              # Generated analysis results (mounted)
└── examples/             # Sample files
```

## 🔧 Troubleshooting

### Docker Not Found
- Install Docker Desktop from https://www.docker.com/products/docker-desktop
- Restart your computer after installation
- Make sure Docker Desktop is running

### Port Already in Use
- The app uses port 8501 by default
- Change the port in the run scripts: `-p 8502:8501`

### Permission Issues (Linux/Mac)
- Make scripts executable: `chmod +x run_docker.sh`
- Add your user to docker group: `sudo usermod -aG docker $USER`

### Container Won't Start
- Check Docker logs: `docker logs $(docker ps -aq --filter ancestor=qualcoder-pro)`
- Rebuild the image: `docker build --no-cache -t qualcoder-pro .`

## 🚀 Advantages of Docker Version

1. **No Python Installation**: Users don't need Python or any dependencies
2. **Consistent Environment**: Same behavior across all platforms
3. **Easy Distribution**: Single package with everything included
4. **Isolation**: Won't interfere with other Python applications
5. **Easy Updates**: Just rebuild the Docker image

## 📞 Support

For technical support or questions:
- Email: MuhammadTayyab.Ilyas@autonoma.cat
- Twitter: @tayyabcheema777
- LinkedIn: tayyabcheema777

## 📄 License

© 2024 Muhammad Tayyab Ilyas
PhD Student, Universitat Autònoma de Barcelona
'''
        
        readme_path = self.package_folder / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        print("  ✅ Created Docker README.md")
    
    def create_zip_package(self):
        """Create ZIP package for distribution"""
        zip_path = self.docker_folder / f"{self.app_name}_v{self.version}.zip"
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(self.package_folder):
                for file in files:
                    file_path = Path(root) / file
                    arcname = file_path.relative_to(self.package_folder)
                    zipf.write(file_path, arcname)
        
        return zip_path

def main():
    creator = DockerPackageCreator()
    creator.create_docker_package()

if __name__ == "__main__":
    main()
