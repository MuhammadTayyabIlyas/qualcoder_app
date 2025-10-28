# 🔬 QualCoder Pro

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.20%2B-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-10.1000%2Fxyz-blue.svg)](https://doi.org/10.1000/xyz)

> **Advanced 3-Stage Qualitative Coding Analysis Platform**

QualCoder Pro is a powerful, user-friendly web application designed for qualitative researchers, educators, and analysts who need to perform systematic qualitative coding analysis. Built with modern web technologies, it provides an intuitive interface for the complete qualitative coding workflow.

## ✨ Features

### 🎯 **3-Stage Qualitative Coding Pipeline**
- **Stage 1**: Initial coding with keyword-based segmentation
- **Stage 2**: Code grouping and pattern analysis  
- **Stage 3**: Thematic framework generation

### 📁 **Multi-Format File Support**
- **DOCX**: Microsoft Word documents
- **PDF**: Portable Document Format files
- **TXT**: Plain text files
- Batch processing of multiple files

### 🤖 **AI-Powered Keyword Suggestions**
- TF-IDF based keyword extraction
- Domain-specific keyword recommendations
- Manual keyword input and customization
- Smart keyword ranking and filtering

### 📊 **Interactive Dashboard**
- Modern, responsive Streamlit interface
- Real-time progress tracking
- Intuitive tabbed workflow
- Professional gradient design

### 📈 **Comprehensive Export Options**
- **Excel Files**: Multi-sheet workbooks with detailed results
- **ZIP Archives**: Complete project packages
- **Individual Files**: Separate downloads for each stage
- **Analytics**: Summary statistics and visualizations

### 🔒 **Privacy & Security**
- **Offline Processing**: All analysis performed locally
- **No Data Upload**: Files never leave your computer
- **Secure**: No external API calls or data transmission

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Internet connection (for initial setup)

### Installation

#### Option 1: Clone and Run (Recommended)
```bash
# Clone the repository
git clone https://github.com/yourusername/qualcoder-pro.git
cd qualcoder-pro

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

#### Option 2: Download Standalone Package
1. Download the latest release from [Releases](https://github.com/yourusername/qualcoder-pro/releases)
2. Extract the ZIP file
3. **Windows**: Double-click `run_app.bat`
4. **Linux/Mac**: Run `./run_app.sh`

#### Option 3: Docker (Advanced Users)
```bash
# Clone the repository
git clone https://github.com/yourusername/qualcoder-pro.git
cd qualcoder-pro

# Build and run with Docker
docker build -t qualcoder-pro .
docker run -p 8501:8501 qualcoder-pro
```

### Access the Application
- The app will automatically open in your browser
- If not, navigate to: http://localhost:8501
- Default port: 8501 (automatically tries 8502, 8503, etc. if busy)

## 📖 Usage Guide

### 1. **Data Input**
- Upload your transcript files (DOCX, PDF, or TXT)
- Choose between default or custom codebook
- Preview uploaded files

### 2. **Configuration**
- Enter your research questions
- Configure domain keywords (NLP suggestions or manual input)
- Set analysis parameters

### 3. **Analysis**
- Review your configuration
- Start the 3-stage analysis process
- Monitor progress in real-time

### 4. **Results**
- Download individual files or complete ZIP package
- View analytics and summary statistics
- Export results in multiple formats

## 🛠️ Technical Details

### Built With
- **Frontend**: Streamlit 1.20+
- **Backend**: Python 3.7+
- **Data Processing**: Pandas, NumPy
- **NLP**: scikit-learn (TF-IDF)
- **File Processing**: python-docx, PyPDF2, openpyxl
- **Visualization**: Streamlit components

### System Requirements
- **OS**: Windows 10+, macOS 10.14+, or Linux
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 1GB free space
- **Python**: 3.7 or higher
- **Browser**: Modern web browser (Chrome, Firefox, Safari, Edge)

### Dependencies
```
streamlit>=1.20.0
pandas>=1.5
openpyxl>=3.0
python-docx>=0.8.11
PyPDF2>=3.0.0
scikit-learn>=1.2
Pillow>=9.0.0
```

## 📁 Project Structure

```
qualcoder-pro/
├── app.py                    # Main Streamlit application
├── qualcoder_core.py         # Core processing functions
├── requirements.txt          # Python dependencies
├── codebook.json            # Default coding framework
├── README.md                # This file
├── LICENSE                  # MIT License
├── CONTRIBUTING.md          # Contribution guidelines
├── CHANGELOG.md             # Version history
├── .github/
│   └── workflows/
│       └── deploy.yml       # GitHub Actions
├── dist_standalone/         # Standalone packages
├── dist_docker/            # Docker packages
├── examples/               # Sample files
├── tests/                  # Test suite
└── outputs/               # Generated results
```

## 🔧 Development

### Setting Up Development Environment
```bash
# Clone the repository
git clone https://github.com/yourusername/qualcoder-pro.git
cd qualcoder-pro

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies

# Run tests
python -m pytest tests/ -v

# Run the application
streamlit run app.py
```

### Running Tests
```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_parsing.py -v

# Run with coverage
python -m pytest tests/ --cov=qualcoder_core --cov=app
```

### Code Style
- Follow PEP 8 guidelines
- Use type hints where appropriate
- Add docstrings to functions and classes
- Write tests for new features

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Ways to Contribute
- 🐛 **Bug Reports**: Report issues and bugs
- 💡 **Feature Requests**: Suggest new features
- 🔧 **Code Contributions**: Submit pull requests
- 📖 **Documentation**: Improve documentation
- 🧪 **Testing**: Add tests and improve coverage

### Development Workflow
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📊 Use Cases

### Academic Research
- **Qualitative Studies**: Systematic analysis of interview transcripts
- **Educational Research**: Analysis of student feedback and responses
- **Social Sciences**: Coding of survey responses and open-ended questions

### Professional Applications
- **Market Research**: Analysis of customer feedback and reviews
- **Content Analysis**: Systematic coding of documents and texts
- **Training Evaluation**: Analysis of training feedback and assessments

### Educational Use
- **Student Projects**: Teaching qualitative research methods
- **Course Assignments**: Structured analysis of case studies
- **Research Training**: Hands-on experience with coding techniques

## 📈 Performance

### Benchmarks
- **Small Files** (< 10 pages): < 30 seconds
- **Medium Files** (10-50 pages): 1-3 minutes
- **Large Files** (50+ pages): 3-10 minutes
- **Batch Processing**: Linear scaling with file count

### Optimization Tips
- Process files in smaller batches for large datasets
- Close other applications to free memory
- Use SSD storage for better performance
- Ensure stable internet connection for package installation

## 🔒 Privacy & Security

### Data Protection
- **Local Processing**: All analysis performed on your computer
- **No Data Upload**: Files never transmitted to external servers
- **Secure Storage**: Results saved locally in your chosen location
- **No Tracking**: No user data collection or analytics

### Best Practices
- Keep your files in secure locations
- Regular backups of important results
- Use strong passwords for shared systems
- Update the application regularly

## 🆘 Troubleshooting

### Common Issues
- **Python Not Found**: Install Python from [python.org](https://python.org)
- **Package Installation Fails**: Check internet connection and try `pip install --upgrade pip`
- **Port Already in Use**: App will automatically try other ports
- **Browser Doesn't Open**: Manually navigate to http://localhost:8501

### Getting Help
- 📖 **Documentation**: Check the [Troubleshooting Guide](TROUBLESHOOTING_GUIDE.md)
- 🐛 **Issues**: Report bugs on [GitHub Issues](https://github.com/yourusername/qualcoder-pro/issues)
- 💬 **Discussions**: Ask questions in [GitHub Discussions](https://github.com/yourusername/qualcoder-pro/discussions)
- 📧 **Email**: MuhammadTayyab.Ilyas@autonoma.cat

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍🎓 Author

**Muhammad Tayyab Ilyas**
- PhD Student, Universitat Autònoma de Barcelona
- Email: MuhammadTayyab.Ilyas@autonoma.cat
- Twitter: [@tayyabcheema777](https://twitter.com/tayyabcheema777)
- LinkedIn: [tayyabcheema777](https://www.linkedin.com/in/tayyabcheema777/)

## 🙏 Acknowledgments

- **Streamlit Team**: For the amazing web framework
- **Python Community**: For excellent libraries and tools
- **Open Source Contributors**: For inspiration and collaboration
- **Universitat Autònoma de Barcelona**: For academic support

## 📚 Citation

If you use QualCoder Pro in your research, please cite:

```bibtex
@software{ilyas2024qualcoder,
  title={QualCoder Pro: Advanced 3-Stage Qualitative Coding Analysis Platform},
  author={Ilyas, Muhammad Tayyab},
  year={2024},
  url={https://github.com/yourusername/qualcoder-pro},
  version={1.0.0}
}
```

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/qualcoder-pro&type=Date)](https://star-history.com/#yourusername/qualcoder-pro&Date)

---

**Made with ❤️ for the qualitative research community**

⭐ **Star this repository** if you find it helpful!