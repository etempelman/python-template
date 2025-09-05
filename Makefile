# Makefile for Python template repo

# Default environment
ENV ?= dev

# Python executable
PYTHON := py

# ---------------------------
# Install dependencies
# ---------------------------
.PHONY: install
install:
	@echo "Installing runtime dependencies..."
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e .

.PHONY: install-dev
install-dev:
	@echo "Installing development dependencies..."
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e .[dev]

# ---------------------------
# Run tests
# ---------------------------
.PHONY: test
test:
	@echo "Running tests with pytest..."
	$(PYTHON) -m pytest tests

# ---------------------------
# Run app
# ---------------------------
.PHONY: run
run:
	@echo "Running the app..."
	$(PYTHON) -m project_name.main

# ---------------------------
# Run coverage
# ---------------------------
.PHONY: coverage
coverage:
	@echo "Running tests with coverage..."
	$(PYTHON) -m coverage run -m pytest tests
	$(PYTHON) -m coverage report -m
	$(PYTHON) -m coverage html
	@echo "HTML coverage report generated in htmlcov/"

# ---------------------------
# Lint and fix code with Ruff
# ---------------------------
.PHONY: lint
lint:
	@echo "Running Ruff linter..."
	$(PYTHON) -m ruff check src tests

.PHONY: lint-fix
lint-fix:
	@echo "Running Ruff linter and fixing issues..."
	$(PYTHON) -m ruff check src tests --fix

# ---------------------------
# Clean pycache and build artifacts
# ---------------------------
.PHONY: clean
clean:
	@echo "Cleaning __pycache__ and build artifacts..."
	rm -rf __pycache__ src/**/__pycache__ tests/**/__pycache__ build/ dist/ *.egg-info htmlcov/
