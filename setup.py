#!/usr/bin/env python
"""
Setup script for PyQuantity package.

This setup.py file is provided for backward compatibility and to support
certain build tools that still expect it. The primary configuration is
in pyproject.toml following PEP 621.
"""

import re
from setuptools import setup

# Read the long description from README.md
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

# Read version from __init__.py to avoid duplication
def get_version():
    with open("src/pyquantity/__init__.py", "r", encoding="utf-8") as f:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    # Basic package information (also defined in pyproject.toml for PEP 621)
    name="pyquantity",
    version=get_version(),
    description="A modern Python package for quantity calculations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Odysseu",
    author_email="uboucherie1@gmail.com",
    url="https://github.com/odysseu/pyquantity",

    # Package structure
    package_dir={"": "src"},
    packages=["pyquantity"],
    python_requires=">=3.10",

    # Classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],

    # Project URLs
    project_urls={
        "Homepage": "https://github.com/odysseu/pyquantity",
        "Documentation": "https://github.com/odysseu/pyquantity#readme",
        "Repository": "https://github.com/odysseu/pyquantity.git",
        "Issues": "https://github.com/odysseu/pyquantity/issues",
    },
)
