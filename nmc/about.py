from importlib.metadata import version, PackageNotFoundError
import platform

def show_version():
    try:
        VERSION = version("nodemodulescleaner")
    except PackageNotFoundError:
        VERSION = f'dev-{version("nodemodulescleaner")}'
    
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