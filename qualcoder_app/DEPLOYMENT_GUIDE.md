# QualCoder Pro - Deployment Guide

This guide explains how to export and deploy your QualCoder Pro application as a standalone web app.

## 🚀 Export Options

I've created **3 different deployment options** for maximum compatibility:

### 1. 📦 Standalone Python Package (Recommended for most users)
**Location**: `dist_standalone/QualCoderPro_v1.0.0.zip`

**What it includes**:
- Complete Python application with all dependencies
- Automatic dependency installation
- Cross-platform launcher scripts
- Comprehensive documentation

**Requirements**:
- Python 3.7+ installed on target machine
- Internet connection (for initial setup)

**How to use**:
1. Extract the ZIP file
2. **Windows**: Double-click `run_app.bat`
3. **Linux/Mac**: Run `./run_app.sh`
4. The app opens automatically in your browser at `http://localhost:8501`

### 2. 🐳 Docker Package (Best for technical users)
**Location**: `dist_docker/QualCoderPro-Docker_v1.0.0.zip`

**What it includes**:
- Complete Docker container setup
- No Python installation required on target machine
- Cross-platform compatibility
- Isolated environment

**Requirements**:
- Docker Desktop installed on target machine

**How to use**:
1. Extract the ZIP file
2. **Windows**: Double-click `run_docker.bat`
3. **Linux/Mac**: Run `./run_docker.sh`
4. The app opens automatically in your browser at `http://localhost:8501`

### 3. 🔧 Manual Deployment (For advanced users)
**Files needed**:
- `app.py`
- `qualcoder_core.py`
- `requirements.txt`
- `codebook.json`
- `Tayyab.png` (optional)

**How to use**:
1. Install Python dependencies: `pip install -r requirements.txt`
2. Run the app: `streamlit run app.py`
3. Access at `http://localhost:8501`

## 📋 Distribution Checklist

### For End Users (Non-Technical)
✅ **Recommended**: Use the **Standalone Python Package**
- Easiest to use
- Automatic setup
- Clear instructions included

### For Technical Users
✅ **Recommended**: Use the **Docker Package**
- No Python installation needed
- Consistent environment
- Easy to manage

### For Developers
✅ **Recommended**: Use **Manual Deployment**
- Full control over environment
- Easy to modify and customize

## 🌐 Web App Features

Your exported web app includes:

### Core Functionality
- **3-Stage Qualitative Coding**: Initial coding, pattern analysis, theme generation
- **Multiple File Formats**: DOCX, PDF, TXT support
- **NLP Keyword Suggestions**: TF-IDF based extraction
- **Interactive Dashboard**: Modern Streamlit interface
- **Export Capabilities**: Excel files and ZIP archives
- **Offline Processing**: All analysis performed locally

### User Interface
- **Professional Design**: Modern gradient-based UI
- **Responsive Layout**: Works on different screen sizes
- **Tabbed Interface**: Organized workflow
- **Real-time Feedback**: Progress indicators and status updates
- **Error Handling**: Clear error messages and troubleshooting

### Developer Information
- **Developer Bio**: Muhammad Tayyab Ilyas (PhD Student, UAB)
- **Contact Information**: Email, Twitter, LinkedIn
- **Version Information**: Built-in version tracking

## 🔧 Troubleshooting

### Common Issues

#### Python Not Found
**Solution**: Install Python from https://python.org and ensure "Add to PATH" is checked

#### Port Already in Use
**Solution**: The app will automatically try ports 8502, 8503, etc.

#### Dependencies Installation Fails
**Solution**: 
1. Check internet connection
2. Update pip: `python -m pip install --upgrade pip`
3. Try manual installation: `pip install -r requirements.txt`

#### Docker Issues
**Solution**:
1. Install Docker Desktop from https://docker.com
2. Restart computer after installation
3. Ensure Docker Desktop is running

### Performance Optimization

#### For Large Files
- Process files in smaller batches
- Close other applications to free memory
- Use SSD storage for better performance

#### For Multiple Users
- Each user should run their own instance
- Use different ports for multiple instances
- Consider cloud deployment for shared access

## 📊 Deployment Scenarios

### 1. Single User (Personal Use)
- Use **Standalone Python Package**
- Extract and run `run_app.bat`
- All data stored locally

### 2. Small Team (5-10 users)
- Each user gets their own **Standalone Python Package**
- Or use **Docker Package** for consistency
- Share via file sharing or cloud storage

### 3. Large Organization (10+ users)
- Deploy **Docker Package** on server
- Use reverse proxy (nginx) for multiple instances
- Consider cloud deployment (AWS, Azure, GCP)

### 4. Cloud Deployment
- Use **Docker Package** with cloud container services
- Deploy to AWS ECS, Azure Container Instances, or Google Cloud Run
- Add domain name and SSL certificate

## 🚀 Advanced Deployment

### Production Deployment
1. **Use Docker**: Most reliable for production
2. **Add Reverse Proxy**: nginx or Apache for load balancing
3. **Environment Variables**: Configure ports and settings
4. **Monitoring**: Add health checks and logging
5. **Backup**: Regular backup of outputs folder

### Security Considerations
- Run behind firewall
- Use HTTPS in production
- Regular security updates
- User authentication (if needed)

## 📞 Support

For deployment issues or questions:
- **Email**: MuhammadTayyab.Ilyas@autonoma.cat
- **Twitter**: @tayyabcheema777
- **LinkedIn**: tayyabcheema777

## 📄 Files Created

### Standalone Package
```
dist_standalone/
├── QualCoderPro_v1.0.0.zip          # Complete package
└── QualCoderPro/                     # Extracted folder
    ├── app.py                        # Main application
    ├── qualcoder_core.py             # Core functions
    ├── requirements.txt              # Dependencies
    ├── run_app.bat                   # Windows launcher
    ├── run_app.sh                    # Linux/Mac launcher
    ├── install.py                    # Installer script
    ├── README.md                     # User documentation
    └── outputs/                      # Results folder
```

### Docker Package
```
dist_docker/
├── QualCoderPro-Docker_v1.0.0.zip   # Complete package
└── QualCoderPro-Docker/              # Extracted folder
    ├── app.py                        # Main application
    ├── qualcoder_core.py             # Core functions
    ├── Dockerfile                    # Docker configuration
    ├── docker-compose.yml            # Docker Compose config
    ├── run_docker.bat                # Windows Docker launcher
    ├── run_docker.sh                 # Linux/Mac Docker launcher
    ├── README.md                     # User documentation
    └── outputs/                      # Results folder
```

## ✅ Success Indicators

Your deployment is successful when:
- ✅ App opens in web browser automatically
- ✅ No error messages in console
- ✅ Can upload and process files
- ✅ Results are generated and downloadable
- ✅ All features work as expected

---

**Created by**: Muhammad Tayyab Ilyas  
**Version**: 1.0.0  
**Date**: 2024


