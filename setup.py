#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# setup.py
# NodeModulesCleaner
# © 2026 Heitor Bisneto
#

from setuptools import setup, find_packages
import pathlib

# Base Directory
HERE = pathlib.Path(__file__).parent

# Long description from README
LONG_DESC = (HERE / "README.md").read_text(encoding="utf-8")

# Project metadata and configuration
setup(
    name="nodemodulescleaner",                          # Public name of the package
    version="1.0.0.1",                                    # Version number
    author="Heitor Bisneto",
    author_email="heitor.bardemaker@live.com",
    description="Automatic cleanup of forgotten node_modules directories",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    url="https://github.com/hbisneto/NodeModulesCleaner",   # Homepage URL
    project_urls={
        "Homepage": "https://github.com/hbisneto/NodeModulesCleaner",
        "Repository": "https://github.com/hbisneto/NodeModulesCleaner.git",
        "Issues": "https://github.com/hbisneto/NodeModulesCleaner/issues",
    },
    # Python package discovery
    packages=find_packages(where="."),

    # Scripts / Entrypoints
    entry_points={
        "console_scripts": [
            "nmc = nmc.cli:main",   # Generates the "nmc" command for CLI usage
        ],
    },

    # Requirements
    install_requires=[
        # If the project depends on external packages, list them here with version specifiers.
        # "tqdm>=4.0.0", "click>=8.0.0"
        "filesystempro==3.0.0.0",
    ],

    # Extra requirements (tests, dev etc.)
    extras_require={
        "dev": ["pytest>=7.0.0"],   # Development dependencies
    },

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],

    python_requires=">=3.10",   # Require Python >= 3.10

    keywords=[
        "node_modules", "cleanup", "filesystem", "CLI", "disk-space",
        "automation", "python-tool", "directory-management"
    ],
    # Automatically include extra files on sdist/wheel
    include_package_data=True,
)