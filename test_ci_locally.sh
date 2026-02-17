#!/bin/bash

# Test CI workflow locally
set -e

echo "=== Testing CI workflow locally ==="

echo "1. Installing dependencies..."
pip install -e ".[dev]"

echo "2. Running linter..."
ruff check .

echo "3. Running type checker..."
mypy src/pyquantity

echo "4. Running tests with coverage..."
pytest

# Generate coverage badge
echo "5. Generating coverage badge..."
python generate_coverage_badge.py

echo "5. Building documentation..."
cd docs
pip install -r requirements.txt
make html
cd ..

echo "6. Building package..."
python -m build --sdist --wheel

echo "=== CI workflow completed successfully! ==="
