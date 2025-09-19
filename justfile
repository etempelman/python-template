# Default target: show available commands
default:
    @just --list

# 🐍 Environment setup
install:
    pip install -e .[dev]

# 🧪 Testing
test:
    pytest

coverage:
    coverage run -m pytest
    coverage report -m
    coverage html
    @echo "Open htmlcov/index.html in your browser for detailed coverage report."

# 🧹 Linting & Formatting
lint:
    ruff check src tests

lint-fix:
    ruff check --fix src tests
    black src tests

format:
    black src tests
    isort src tests

# 🏗 Build & Publish
build:
    hatch build

publish:
    hatch publish

# 🧼 Clean up
clean:
    rm -rf build dist *.egg-info .pytest_cache .mypy_cache .ruff_cache htmlcov
