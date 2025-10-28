# QualCoder Pro - Troubleshooting Guide

This guide helps you resolve common issues when running the standalone QualCoder Pro application.

## 🚨 Common Error Messages and Solutions

### 1. "Python was not found" or "Python is not installed"

**Error Message:**
```
Python was not found; run without arguments to install from the Microsoft Store
```

**Solution:**
1. Install Python from https://www.python.org/downloads/
2. **IMPORTANT**: Check "Add Python to PATH" during installation
3. Restart your computer after installation
4. Try running the app again

**Alternative Solution:**
- If you have Python installed but it's not in PATH, try running:
  ```cmd
  py run_app.bat
  ```
  or
  ```cmd
  python3 run_app.bat
  ```

### 2. "Module not found" or "No module named 'streamlit'"

**Error Message:**
```
ModuleNotFoundError: No module named 'streamlit'
```

**Solution:**
1. Open Command Prompt as Administrator
2. Navigate to the app folder: `cd path\to\QualCoderPro`
3. Install requirements: `pip install -r requirements.txt`
4. Try running the app again

**Alternative Solution:**
```cmd
pip install streamlit pandas openpyxl python-docx PyPDF2 scikit-learn Pillow
```

### 3. "Port already in use" or "Address already in use"

**Error Message:**
```
OSError: [Errno 98] Address already in use
```

**Solution:**
1. Close any other Streamlit apps or web servers
2. The app will automatically try ports 8502, 8503, etc.
3. Or manually specify a different port:
   ```cmd
   streamlit run app.py --server.port 8502
   ```

### 4. "Permission denied" (Linux/Mac)

**Error Message:**
```
Permission denied: './run_app.sh'
```

**Solution:**
```bash
chmod +x run_app.sh
./run_app.sh
```

### 5. "File not found" or "app.py not found"

**Error Message:**
```
ERROR: app.py not found in current directory
```

**Solution:**
1. Make sure you're in the correct folder
2. The folder should contain: `app.py`, `qualcoder_core.py`, `run_app.bat`
3. Navigate to the correct folder first:
   ```cmd
   cd path\to\QualCoderPro
   run_app.bat
   ```

### 6. "Failed to install requirements"

**Error Message:**
```
ERROR: Failed to install requirements
```

**Solution:**
1. Check your internet connection
2. Update pip first:
   ```cmd
   python -m pip install --upgrade pip
   ```
3. Try installing packages one by one:
   ```cmd
   pip install streamlit
   pip install pandas
   pip install openpyxl
   pip install python-docx
   pip install PyPDF2
   pip install scikit-learn
   pip install Pillow
   ```

### 7. Browser doesn't open automatically

**Solution:**
1. Manually open your web browser
2. Go to: http://localhost:8501
3. If that doesn't work, try: http://127.0.0.1:8501

### 8. "Access denied" or "Firewall blocking"

**Solution:**
1. Allow Python/Streamlit through Windows Firewall
2. Or temporarily disable firewall to test
3. Add exception for port 8501

## 🔧 Diagnostic Steps

### Step 1: Run the Diagnostic Tool
1. Open Command Prompt in the app folder
2. Run: `python diagnose.py`
3. This will check all requirements and show what's missing

### Step 2: Manual Checks

#### Check Python Installation:
```cmd
python --version
```
Should show Python 3.7 or higher.

#### Check if all files are present:
```cmd
dir
```
Should show: `app.py`, `qualcoder_core.py`, `requirements.txt`, `run_app.bat`

#### Check if packages are installed:
```cmd
python -c "import streamlit; print('Streamlit OK')"
```

### Step 3: Test Individual Components

#### Test Streamlit:
```cmd
streamlit hello
```
This should open a demo app in your browser.

#### Test the main app:
```cmd
streamlit run app.py
```

## 🆘 Advanced Troubleshooting

### If nothing works:

1. **Fresh Python Installation:**
   - Uninstall Python completely
   - Download fresh Python from python.org
   - Install with "Add to PATH" checked
   - Restart computer

2. **Use Virtual Environment:**
   ```cmd
   python -m venv qualcoder_env
   qualcoder_env\Scripts\activate
   pip install -r requirements.txt
   streamlit run app.py
   ```

3. **Use Docker (if available):**
   - Install Docker Desktop
   - Use the Docker version of the app

### Check System Requirements:
- **Windows**: Windows 10 or later
- **Python**: 3.7 or higher
- **RAM**: At least 4GB (8GB recommended)
- **Disk Space**: At least 1GB free
- **Internet**: Required for initial package installation

## 📞 Getting Help

If you're still having issues:

1. **Run the diagnostic tool** and share the output
2. **Take a screenshot** of the error message
3. **Note your system details**:
   - Windows version
   - Python version
   - Error message
   - What you were doing when the error occurred

**Contact Support:**
- Email: MuhammadTayyab.Ilyas@autonoma.cat
- Twitter: @tayyabcheema777
- LinkedIn: tayyabcheema777

## ✅ Success Indicators

Your app is working correctly when:
- ✅ No error messages in the console
- ✅ Browser opens automatically
- ✅ You see the QualCoder Pro interface
- ✅ You can upload files
- ✅ Analysis runs successfully
- ✅ Results are generated

---

**Remember**: Most issues are related to Python installation or missing packages. The diagnostic tool will help identify the exact problem!

