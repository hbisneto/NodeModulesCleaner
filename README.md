# 🧹 NodeModulesCleaner (nmc)

![CI](https://github.com/hbisneto/NodeModulesCleaner/actions/workflows/tests.yml/badge.svg)
![License](https://img.shields.io/github/license/hbisneto/NodeModulesCleaner)

![Python](https://img.shields.io/pypi/pyversions/NodeModulesCleaner)
![PyPI](https://img.shields.io/pypi/v/NodeModulesCleaner)
![Downloads](https://img.shields.io/pypi/dm/NodeModulesCleaner)

![Issues](https://img.shields.io/github/issues/hbisneto/NodeModulesCleaner)
![Stars](https://img.shields.io/github/stars/hbisneto/NodeModulesCleaner?style=social)

[![codecov](https://codecov.io/github/hbisneto/NodeModulesCleaner/graph/badge.svg?token=TPY9K1INYE)](https://codecov.io/github/hbisneto/NodeModulesCleaner)


> Automatic cleanup of forgotten `node_modules` directories.

**NodeModulesCleaner** is a fast, safe, and practical CLI tool that helps you free up disk space by detecting and removing old and unused `node_modules` folders from your system.

It recursively scans your filesystem, identifies abandoned `node_modules` directories based on access time and size, and optionally deletes them — safely and efficiently.

---

## ✨ Features

* 🔍 Recursive directory scanning
* 🕒 Filter by last access time (`--days`)
* 📦 Filter by minimum directory size (`--min-size`)
* 🔎 Dry-run mode (preview before deleting)
* 🤖 Non-interactive automation mode (`--yes`)
* ⚡ Very fast (no heavy indexing or hashing)
* 🧪 Fully testable architecture (core separated from CLI)
* 🧩 Clean, maintainable and extensible design

---

## 📦 Why does this exist?

JavaScript projects often accumulate **hundreds of megabytes or even gigabytes** inside `node_modules`.

Over time, many of these folders become **abandoned**, consuming large amounts of disk space and slowing down backups, indexing, and file searches.

This tool helps you:

* Clean forgotten dependencies
* Reclaim disk space
* Keep your development environment tidy
* Automate periodic cleanup (cron jobs, CI pipelines, scripts)

---

## 🚀 Installation

### Using pip (recommended)

```bash
pip install nodemodulescleaner
```

---

## ⚡ Quick Usage

Scan your home directory:

```bash
nmc ~
```

Preview what would be deleted:

```bash
nmc ~ --dry-run
```

Delete folders not accessed in the last 30 days and larger than 200 MB:

```bash
nmc ~ --days 30 --min-size 200
```

Fully automated cleanup (no confirmation prompt):

```bash
nmc ~ --days 60 --min-size 100 -y
```

---

## ⚙️ CLI Options

```text
usage: nmc [path] [options]

positional arguments:
  path                Directory to scan (default: current directory)

options:
  --days N            Ignore node_modules accessed within the last N days (default: 30)
  --min-size MB       Minimum size in MB (default: 0)
  --dry-run           Simulate the cleanup without deleting anything
  -y, --yes           Automatically confirm deletion (non-interactive mode)
```

---

## 🛡️ Safety First

Before deleting anything, the tool:

* Lists all matching directories
* Shows total recoverable disk space
* Requires explicit confirmation (unless `-y` is used)

Always test first:

```bash
nmc <path> --dry-run
```

---

# 🧑‍💻 Developer Guide (Dev)

This section is for contributors and developers who want to **run, test, or extend** the project.

---

## 📁 Project Structure

```text
nmc/
 ├── core.py     # Business logic (scan + filters + cleanup)
 ├── cli.py      # CLI interface (argparse + UX)
 └── __init__.py
```

This separation ensures:

* High testability
* Clean architecture
* Easy extensibility
* Stable CLI behavior

---

## 🔧 Local Development Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/hbisneto/NodeModulesCleaner.git
cd NodeModulesCleaner
```

---

### 2️⃣ Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install in editable mode

```bash
pip install -e .
```

This allows immediate reflection of local code changes.

---

## ▶ Running Locally

```bash
nmc ~/projects --dry-run
```

or:

```bash
python -m nmc.cli ~/projects --dry-run
```

---

## 🧪 Running Tests

```bash
pytest -v
```

The architecture guarantees:

* No interactive input during tests
* No filesystem pollution
* Fully deterministic execution

---

## 🏗 Architecture Overview

### Core Logic → `nmc/core.py`

Handles:

* Directory scanning
* Filtering logic
* Cleanup execution

No user interaction. No printing.

---

### CLI Interface → `nmc/cli.py`

Handles:

* Argument parsing
* User prompts
* Output formatting
* UX flow

This separation enables:

* Stable CI pipelines
* Easy automation
* Reliable testing
* Low bug surface

---

## 🤝 Contributing

Contributions are very welcome!

If you'd like to help improve **NodeModulesCleaner**, please check out the open issues on GitHub:

👉 https://github.com/hbisneto/NodeModulesCleaner/issues

There you will find:

- 🐛 Bug reports
- 🚀 Feature requests
- 🧩 Planned enhancements
- 🏗 Architecture improvements
- 🧪 Testing and CI ideas

If you have a new idea, feel free to open a new issue or start a discussion.

Every contribution — from code to documentation, testing, or ideas — is highly appreciated! ❤️

---

## 📜 License

MIT License — feel free to use, modify, and distribute.

---

## ⭐ Support

If this tool helped you, please leave a ⭐ on GitHub — it really helps!