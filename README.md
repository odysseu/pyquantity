# PyQuantity

[![CI](https://github.com/odysseu/pyquantity/actions/workflows/ci.yml/badge.svg)](https://github.com/odysseu/pyquantity/actions/workflows/ci.yml)
![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)
![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)
![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)
![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)
![Python 3.14](https://img.shields.io/badge/python-3.14-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python package for quantity calculations with unit support and dimensional analysis.

**Test Coverage**: ![Coverage](coverage_badge.svg)

## Features

- Comprehensive unit systems with 60+ base dimensions
- 1000+ derived units including mechanical, electrical, and thermal units
- Full SI prefix support from yocto to yotta
- Contextual measurements with built-in database
- Natural language parsing for quantity extraction
- Advanced physics calculations
- Type hints and comprehensive documentation

## Installation

```bash
pip install pyquantity
```

**Requirements:**
- Python 3.10 or higher (following [Python's version support policy, mostly](https://devguide.python.org/versions/))

**For Developers:**
```bash
pip install -e ".[dev]"
python test_with_coverage.py
```

## Quick Start

```python
from pyquantity import Quantity, get_measurement, parse_quantity

# Basic quantity operations
length = Quantity(5.0, "meter")
width = Quantity(3.0, "meter")
area = length * width

# Unit conversion
distance = Quantity(1.5, "kilometer")
distance_m = distance.convert("meter")

# Contextual measurements
bath = get_measurement("normal bath")
cup = get_measurement("cup")
cups_in_bath = bath / cup

# Natural language parsing
text = "A car traveling at 120 km/h for 2.5 hours"
quantities = parse_quantity(text)
```

## Documentation

- [Usage Guide](docs/usage_guide.md)
- [Advanced Features](docs/advanced_features.md)
- [API Reference](docs/api_reference.md)
- [Examples](example_usage.py)

## License

MIT License - See [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome!
