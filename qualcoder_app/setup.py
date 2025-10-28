"""
Setup script for QualCoder Pro
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="qualcoder-pro",
    version="1.0.0",
    author="Muhammad Tayyab Ilyas",
    author_email="MuhammadTayyab.Ilyas@autonoma.cat",
    description="Advanced 3-Stage Qualitative Coding Analysis Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/qualcoder-pro",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/qualcoder-pro/issues",
        "Source": "https://github.com/yourusername/qualcoder-pro",
        "Documentation": "https://github.com/yourusername/qualcoder-pro#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Framework :: Streamlit",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "isort>=5.10.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "qualcoder-pro=app:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.json", "*.md", "*.txt", "*.png", "*.jpg", "*.jpeg"],
    },
    keywords=[
        "qualitative research",
        "coding analysis",
        "text analysis",
        "research tools",
        "academic software",
        "data analysis",
        "streamlit",
        "nlp",
        "tf-idf",
        "thematic analysis",
    ],
    zip_safe=False,
)
