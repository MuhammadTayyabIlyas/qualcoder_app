@echo off
echo ========================================
echo    QualCoder Pro - Streamlit Launcher
echo ========================================
echo.

REM Change to the directory where this bat file is located
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
echo Starting QualCoder Pro...
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


