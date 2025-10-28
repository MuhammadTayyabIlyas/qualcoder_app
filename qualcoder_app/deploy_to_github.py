"""
GitHub Deployment Script for QualCoder Pro
This script helps prepare and deploy the project to GitHub
"""

import os
import subprocess
import sys
from pathlib import Path
import shutil

class GitHubDeployer:
    def __init__(self):
        self.repo_name = "qualcoder-pro"
        self.github_username = input("Enter your GitHub username: ").strip()
        self.github_repo_url = f"https://github.com/{self.github_username}/{self.repo_name}.git"
        
    def check_git_installed(self):
        """Check if Git is installed"""
        try:
            subprocess.run(["git", "--version"], check=True, capture_output=True)
            print("✓ Git is installed")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("✗ Git is not installed. Please install Git first.")
            return False
    
    def initialize_git_repo(self):
        """Initialize Git repository if not already initialized"""
        if Path(".git").exists():
            print("✓ Git repository already initialized")
            return True
        
        try:
            subprocess.run(["git", "init"], check=True)
            print("✓ Git repository initialized")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to initialize Git repository: {e}")
            return False
    
    def create_github_repo(self):
        """Create GitHub repository using GitHub CLI or provide instructions"""
        print("\n" + "="*60)
        print("CREATING GITHUB REPOSITORY")
        print("="*60)
        
        # Check if GitHub CLI is installed
        try:
            subprocess.run(["gh", "--version"], check=True, capture_output=True)
            print("✓ GitHub CLI found")
            
            # Create repository using GitHub CLI
            try:
                subprocess.run([
                    "gh", "repo", "create", self.repo_name,
                    "--public",
                    "--description", "Advanced 3-Stage Qualitative Coding Analysis Platform",
                    "--add-readme"
                ], check=True)
                print(f"✓ GitHub repository created: {self.github_repo_url}")
                return True
            except subprocess.CalledProcessError as e:
                print(f"✗ Failed to create repository with GitHub CLI: {e}")
                return False
                
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("✗ GitHub CLI not found")
            print("\nPlease create the repository manually:")
            print(f"1. Go to https://github.com/new")
            print(f"2. Repository name: {self.repo_name}")
            print(f"3. Description: Advanced 3-Stage Qualitative Coding Analysis Platform")
            print(f"4. Make it public")
            print(f"5. Don't initialize with README (we have our own)")
            print(f"6. Click 'Create repository'")
            
            input("\nPress Enter after creating the repository...")
            return True
    
    def add_files_to_git(self):
        """Add all files to Git"""
        try:
            # Add all files
            subprocess.run(["git", "add", "."], check=True)
            print("✓ Files added to Git")
            
            # Check if there are changes to commit
            result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
            if not result.stdout.strip():
                print("✓ No changes to commit")
                return True
            
            # Commit changes
            subprocess.run([
                "git", "commit", "-m", 
                "Initial commit: QualCoder Pro v1.0.0\n\n- 3-stage qualitative coding pipeline\n- Multi-format file support\n- NLP keyword suggestions\n- Interactive Streamlit dashboard\n- Comprehensive export options\n- Standalone deployment packages"
            ], check=True)
            print("✓ Changes committed")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to add files to Git: {e}")
            return False
    
    def push_to_github(self):
        """Push to GitHub repository"""
        try:
            # Add remote origin
            subprocess.run(["git", "remote", "add", "origin", self.github_repo_url], check=True)
            print("✓ Remote origin added")
            
            # Push to GitHub
            subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
            print("✓ Code pushed to GitHub")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to push to GitHub: {e}")
            print("You may need to push manually:")
            print(f"git remote add origin {self.github_repo_url}")
            print("git push -u origin main")
            return False
    
    def create_release(self):
        """Create a GitHub release"""
        print("\n" + "="*60)
        print("CREATING GITHUB RELEASE")
        print("="*60)
        
        try:
            # Check if GitHub CLI is available
            subprocess.run(["gh", "--version"], check=True, capture_output=True)
            
            # Create release
            subprocess.run([
                "gh", "release", "create", "v1.0.0",
                "--title", "QualCoder Pro v1.0.0 - Initial Release",
                "--notes", """
## 🎉 QualCoder Pro v1.0.0 - Initial Release

### ✨ Features
- **3-Stage Qualitative Coding Pipeline**: Initial coding, pattern analysis, and theme generation
- **Multi-Format File Support**: DOCX, PDF, and TXT files
- **AI-Powered Keyword Suggestions**: TF-IDF based keyword extraction
- **Interactive Dashboard**: Modern Streamlit interface
- **Comprehensive Export Options**: Excel files and ZIP archives
- **Standalone Deployment**: Easy distribution packages

### 🚀 Quick Start
1. Download the standalone package
2. Extract and run `run_app.bat` (Windows) or `./run_app.sh` (Linux/Mac)
3. Open your browser to http://localhost:8501

### 📦 Downloads
- **Standalone Package**: Complete Python application
- **Docker Package**: Containerized deployment
- **Source Code**: Full source code and documentation

### 🔧 Requirements
- Python 3.7 or higher
- Modern web browser
- Internet connection (for initial setup)

### 📖 Documentation
- [Installation Guide](README.md#installation)
- [Usage Guide](README.md#usage-guide)
- [Troubleshooting](TROUBLESHOOTING_GUIDE.md)
- [Contributing](CONTRIBUTING.md)

### 👨‍🎓 Author
**Muhammad Tayyab Ilyas** - PhD Student, Universitat Autònoma de Barcelona
- Email: MuhammadTayyab.Ilyas@autonoma.cat
- Twitter: @tayyabcheema777
- LinkedIn: tayyabcheema777

---
*Made with ❤️ for the qualitative research community*
                """,
                "dist_standalone/QualCoderPro_v1.0.0.zip",
                "dist_docker/QualCoderPro-Docker_v1.0.0.zip"
            ], check=True)
            print("✓ GitHub release created")
            return True
            
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("✗ GitHub CLI not available for release creation")
            print("Please create a release manually:")
            print(f"1. Go to {self.github_repo_url}/releases")
            print("2. Click 'Create a new release'")
            print("3. Tag version: v1.0.0")
            print("4. Release title: QualCoder Pro v1.0.0 - Initial Release")
            print("5. Upload the ZIP files from dist_standalone/ and dist_docker/")
            return False
    
    def setup_github_pages(self):
        """Setup GitHub Pages for documentation"""
        print("\n" + "="*60)
        print("SETTING UP GITHUB PAGES")
        print("="*60)
        
        print("To enable GitHub Pages:")
        print(f"1. Go to {self.github_repo_url}/settings/pages")
        print("2. Source: Deploy from a branch")
        print("3. Branch: main")
        print("4. Folder: / (root)")
        print("5. Click 'Save'")
        print(f"6. Your site will be available at: https://{self.github_username}.github.io/{self.repo_name}")
    
    def deploy(self):
        """Main deployment process"""
        print("🚀 QualCoder Pro - GitHub Deployment")
        print("="*60)
        
        # Check prerequisites
        if not self.check_git_installed():
            return False
        
        # Initialize Git repository
        if not self.initialize_git_repo():
            return False
        
        # Create GitHub repository
        if not self.create_github_repo():
            return False
        
        # Add files to Git
        if not self.add_files_to_git():
            return False
        
        # Push to GitHub
        if not self.push_to_github():
            return False
        
        # Create release
        self.create_release()
        
        # Setup GitHub Pages
        self.setup_github_pages()
        
        print("\n" + "="*60)
        print("🎉 DEPLOYMENT COMPLETE!")
        print("="*60)
        print(f"Repository: {self.github_repo_url}")
        print(f"Releases: {self.github_repo_url}/releases")
        print(f"Pages: https://{self.github_username}.github.io/{self.repo_name}")
        print("\nNext steps:")
        print("1. Share your repository with others")
        print("2. Encourage contributions and stars")
        print("3. Monitor issues and pull requests")
        print("4. Keep the project updated")
        
        return True

def main():
    """Main function"""
    deployer = GitHubDeployer()
    deployer.deploy()

if __name__ == "__main__":
    main()
