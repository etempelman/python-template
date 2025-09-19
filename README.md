# python-template
This repository provides a flexible and opinionated Python project template designed to help you start new projects quickly while following best practices. It includes a recommended directory structure, default configuration files, and tooling integrations for packaging, testing, linting, documentation, and reproducibility.

---

## Features
- **PEP 621** compliant `pyproject.toml` with [Hatchling](https://hatch.pypa.io/latest/)  
- Centralized tool configs (`black`, `ruff`, `isort`, `mypy`, `pytest`, `coverage`)  
- [Just](https://github.com/casey/just) for developer automation (like `make`, but simpler)  
- `src/` layout for clean package structure  
- `.env.example` for environment variable management  
- MIT-licensed

---

# Getting Started

Follow these steps to set up the project for development.

## 1. Clone the repository
```bash
$ git clone https://github.com/etempelman/python-template.git
$ cd project-name
```
Replace placeholder names:
- Update pyproject.toml → set project name, description, authors, URLs
- Rename src/project_name/ → to your actual package name
- Adjust README.md

## 2. Create a virtual environment
```bash
$ python3 -m venv .venv
$ source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```
## 3. Install dependencies

You’ll need just installed:
```bash
brew install just    # macOS (Homebrew)
sudo apt install just # Ubuntu/Debian
winget install --id Casey.Just # Windows (PowerShell)
```
Then install project dependencies:
```bash
just install
```

## 4. Configure environment variables

- Copy `.env.example` to `.env` and edit values if needed:
```bash
$ cp .env.example .env
```
- The `.env` file controls environment-specific settings such as:

APP_ENV=dev
LOG_DIR=logs
LOG_FILE=app.log

- The default environment is `dev`. You can change it to `test`, `stage`, or `prod`.

## 5. Common tasks with just
```bash
just            # list all available commands
just install    # install project + dev dependencies
just test       # run tests with pytest
just coverage   # run tests with coverage report
just lint       # check code style with ruff
just lint-fix   # auto-fix linting issues (ruff + black)
just format     # format code (black + isort)
just build      # build wheel & sdist via hatch
just publish    # publish to PyPI (requires credentials)
just clean      # remove build/test artifacts
```

---
# Project Structure
```bash
python-template/
├── data/
├── logs/
├── notebooks/
├── src/
│   └── project_name/
├── tests/
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
```
- src/project_name/ → main package placeholder
- tests/ → test suite
- data/ → optional data storage
- logs/ → log files directory
- notebooks/ → optional notebooks
- .env.example → template for environment variables
- .gitignore → git ignore rules
- LICENSE → MIT license
- README.md → project documentation
- pyproject.toml → project metadata and build configuration
