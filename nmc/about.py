import platform

def show_version():
    VERSION = "1.0.0.2"
    PYTHON_VERSION = platform.python_version()

    banner = rf"""
**********************************************************************
** NodeModulesCleaner
** Automatic cleanup of forgotten node_modules directories.
**********************************************************************
** nmc v{VERSION}
** Python {PYTHON_VERSION}
** Copyright (c) 2026 Bisneto Inc.
**********************************************************************
""".strip("\n")
    
    print(banner)