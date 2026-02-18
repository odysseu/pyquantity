# PyQuantity Documentation

Welcome to the PyQuantity documentation!

## Overview

PyQuantity is a modern Python package for working with physical quantities, units, and dimensional analysis. It provides a type-safe way to handle measurements and conversions in scientific and engineering applications.

## Installation

### From PyPI (Recommended)

```bash
pip install pyquantity
```

### From GitHub Releases

Pre-built wheel files are available for each release:

1. Go to the [GitHub Releases page](https://github.com/odysseu/pyquantity/releases)
2. Download the appropriate wheel file for your platform
3. Install using pip:

```bash
pip install pyquantity-1.0.0-py3-none-any.whl
```

### From Source

```bash
# Clone the repository
git clone https://github.com/odysseu/pyquantity.git
cd pyquantity

# Install in development mode
pip install -e ".[dev]"
```

## Quick Start

```python
from pyquantity import Quantity

# Create a quantity
length = Quantity(5.0, "meter")

# Convert units
length_cm = length.convert("centimeter")

# Display the quantity
print(length)  # Output: 5.0 meter
```

## Comprehensive Usage Guide

For detailed usage examples, API reference, and advanced features, see our [Usage Guide](usage_guide.md) which covers:

- **Basic Usage**: Creating quantities and basic operations
- **Unit Conversion**: Automatic conversion between compatible units
- **Arithmetic Operations**: Mathematical operations with dimensional analysis
- **Natural Language Parsing**: Extract quantities from text
- **Supported Units**: Complete list of supported units and abbreviations
- **Advanced Features**: Compound units, context-aware parsing, and more
- **Error Handling**: Best practices for handling exceptions
- **Examples by Domain**: Electrical engineering, physics, temperature measurements

## Core Concepts

### Quantity

The `Quantity` class represents a physical measurement with a value and unit:

```python
from pyquantity import Quantity

# Create quantities
mass = Quantity(10.0, "kilogram")
time = Quantity(2.5, "second")

# Access properties
print(mass.value)  # 10.0
print(mass.unit)   # "kilogram"
```

### Unit Conversion

pyquantity supports conversion between compatible units:

```python
distance = Quantity(1000.0, "meter")
distance_km = distance.convert("kilometer")  # 1.0 kilometer
```

## API Reference

### `pyquantity.Quantity`

```python
class Quantity(value: float, unit: str)
```

**Parameters:**
- `value`: The numerical value of the quantity
- `unit`: The unit of measurement as a string

**Methods:**
- `convert(target_unit: str) -> Quantity`: Convert to a different unit

**Properties:**
- `value: float`: The numerical value
- `unit: str`: The unit of measurement

## Development

To contribute to pyquantity:

1. Fork the repository
2. Create a virtual environment
3. Install development dependencies
4. Make your changes
5. Run tests and linting
6. Submit a pull request

```bash
# Clone the repository
git clone https://github.com/odysseu/pyquantity.git

# Install dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

## License

pyquantity is licensed under the MIT License.