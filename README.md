# python-template
This repository provides a flexible and opinionated Python project template designed to help you start new projects quickly while following best practices. It includes a recommended directory structure, default configuration files, and tooling integrations for packaging, testing, linting, documentation, and reproducibility.

# Getting Started

Follow these steps to set up the project for development.

## 1. Clone the repository
```bash
$ git clone https://github.com/etempelman/python-template.git
$ cd project-name
```
## 2. Create a virtual environment
```bash
$ python3 -m venv .venv
$ source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```
## 3. Install dependencies

Install runtime dependencies:
```bash
$ make install
```
Install development dependencies (for testing, linting, and coverage):
```bash
$ make install-dev
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

## 6. Update `setup.cfg` if necessary

- Add new runtime dependencies under `[options] install_requires`.
- Add new development dependencies under `[options.extras_require] dev`.
- Your Makefile and pip installation commands will automatically pick them up.

## 7. Run the project and tests

- Run tests:
```bash
$ make test
```
- Run app:
```bash
$ make run
```
- Run coverage report:
```bash
$ make coverage
```
- Run Ruff linting:
```bash
$ make lint
```
- Automatically fix lint issues:
```bash
$ make lint-fix
```
- Clean cache and build artifacts:
```bash
$ make clean
```
## Notes

- Using a virtual environment ensures that dependencies are isolated from your system Python.
- The Makefile centralizes common tasks to keep development consistent.
- VS Code extensions for Ruff, Black, and mypy will automatically integrate with your workflow.

## Makefile

This project includes a `Makefile` to simplify common development tasks. All commands should be run from the **root of the repository**.

### Install dependencies

Install runtime dependencies:

```bash
make install
```

Install development dependencies (including pytest, Ruff, and coverage):

```bash
make install-dev
```

### Run tests

Run all unit tests with pytest:

```bash
make test
```

Run tests and generate a coverage report (both console and HTML):

```bash
make coverage
```

The HTML coverage report will be generated in the htmlcov/ directory.

### Linting

Check code with Ruff:

```bash
make lint
```

Automatically fix issues where possible:

```bash
make lint-fix
```

### Cleaning

Remove Python cache, build artifacts, and coverage reports:

```bash
make clean
```