# Makefile for pyquantity development

.PHONY: install test lint format check clean

# Default target
all: check

# Install the package in development mode
install:
	pip install -e ".[dev]"

# Run tests
test:
	pytest --cov=pyquantity --cov-report=term-missing

# Run linter
lint:
	ruff check .

# Format code
format:
	black .
	isort .

# Run type checker
type:
	mypy .

# Run all checks
check: lint type test

# Clean up
clean:
	rm -rf build/ dist/ .pytest_cache/ .mypy_cache/ .ruff_cache/ htmlcov/ .coverage

# Show help
help:
	@echo "Available targets:"
	@echo "  install   - Install package in development mode"
	@echo "  test      - Run tests with coverage"
	@echo "  lint      - Run linter"
	@echo "  format    - Format code"
	@echo "  type      - Run type checker"
	@echo "  check     - Run all checks (lint, type, test)"
	@echo "  clean     - Clean up build artifacts"
	@echo "  help      - Show this help message"