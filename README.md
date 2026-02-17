# PyQuantity

[![CI](https://github.com/odysseu/pyquantity/actions/workflows/ci.yml/badge.svg)](https://github.com/odysseu/pyquantity/actions/workflows/ci.yml)
![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)
![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)
![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)
![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)
![Python 3.14](https://img.shields.io/badge/python-3.14-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A modern Python package for quantity calculations with comprehensive unit support, dimensional analysis, and contextual measurements.

**Test Coverage**: ![Coverage](coverage_badge.svg) (Local coverage reporting with pytest-cov)

## Features

### 🔢 Comprehensive Unit Systems
- **60+ base dimensions** including length, mass, time, temperature, electrical, mechanical, thermal, optical, and more
- **1000+ derived units** including speed, acceleration, force, pressure, energy, power, and specialized engineering units
- **Full SI prefix support** from yocto (10⁻²⁴) to yotta (10²⁴)
- **Real-world unit conversions** (mph to m/s, psi to Pa, gallons to liters, etc.)

### 📊 Contextual Measurements
- **Built-in measurement database** with 100+ real-world objects
- **Standard measurements** for common objects (cups, baths, cars, etc.)
- **Custom measurement support** - add your own objects and measurements
- **Search and discovery** - find measurements by name or category

### 🗣️ Natural Language Processing
- **Smart quantity parsing** from natural language text
- **Multiple quantity extraction** from complex sentences
- **Unit detection** - identify units mentioned in text
- **Contextual object recognition** - detect real-world objects in text

### ⚙️ Advanced Calculations
- **Physics engine** - kinematics, dynamics, thermodynamics
- **Electrical engineering** - Ohm's Law, power calculations, circuit analysis
- **Dimensional analysis** - type-safe quantity operations
- **Automatic unit conversion** - seamless compatibility between units

### 🔧 Developer Friendly
- **Type hints** and comprehensive documentation
- **Extensive test coverage** with 50+ test cases
- **Modular architecture** - easy to extend
- **CI/CD ready** with GitHub Actions workflow

## Installation

```bash
pip install pyquantity
```

**Requirements:**
- Python 3.10 or higher (following [Python's version support policy](https://devguide.python.org/versions/))
- No additional system dependencies required

## Quick Start

```python
from pyquantity import Quantity, get_measurement, parse_quantity

# Basic quantity operations
length = Quantity(5.0, "meter")
width = Quantity(3.0, "meter")
area = length * width
print(f"Area: {area}")  # 15.0 meter*meter

# Unit conversion with prefixes
distance = Quantity(1.5, "kilometer")
distance_m = distance.convert("meter")
print(f"1.5 km = {distance_m}")  # 1500.0 meter

# Electrical engineering
voltage = Quantity(230.0, "volt")
current = Quantity(10.0, "ampere")
power = voltage * current
power_kw = power.convert("kilowatt")
print(f"Power: {power_kw}")  # 2.3 kilowatt

# Contextual measurements
bath = get_measurement("normal bath")
cup = get_measurement("cup")
cups_in_bath = bath / cup
print(f"Cups in a bath: {cups_in_bath:.1f}")  # ~600.0

# Natural language parsing
text = "A car traveling at 120 km/h for 2.5 hours"
quantities = parse_quantity(text)
print(f"Found quantities: {quantities}")
```

## Documentation

- [Usage Guide](docs/usage_guide.md) - Basic usage and examples
- [Advanced Features](docs/advanced_features.md) - Enhanced unit systems, contextual measurements, and NLP
- [API Reference](docs/api_reference.md) - Complete API documentation
- [Examples](example_usage.py) - Basic examples
- [Advanced Examples](example_advanced_usage.py) - Comprehensive demonstrations

## Enhanced Unit Systems

### Mechanical Units
```python
# Speed and acceleration
speed = Quantity(25.0, "meter/second")
acceleration = Quantity(9.81, "meter/second_squared")

# Area and volume
area = Quantity(25.0, "square_meter")
volume = Quantity(1.0, "cubic_meter")

# Pressure and energy
pressure = Quantity(101325.0, "pascal")
energy = Quantity(1000.0, "joule")
```

### Electrical Units
```python
# Voltage, current, resistance
voltage = Quantity(230.0, "volt")
current = Quantity(10.0, "ampere")
resistance = Quantity(470.0, "ohm")

# Capacitance and inductance
capacitance = Quantity(100.0, "microfarad")
inductance = Quantity(10.0, "millihenry")

# Power and frequency
power = Quantity(100.0, "watt")
frequency = Quantity(50.0, "hertz")
```

### Thermal Units
```python
# Temperature
temp_c = Quantity(25.0, "celsius")
temp_f = Quantity(77.0, "fahrenheit")

# Specific heat and conductivity
specific_heat = Quantity(4186.0, "joule/kilogram/kelvin")
conductivity = Quantity(0.6, "watt/meter/kelvin")
```

## Contextual Measurements

### Real-World Objects
```python
from pyquantity import MeasurementDatabase

db = MeasurementDatabase()

# Volume measurements
bath = db.get_measurement("normal bath")  # 150 L
cup = db.get_measurement("cup")          # 250 mL

# Mass measurements
person = db.get_measurement("average person")  # 70 kg
car = db.get_measurement("car mass")        # 1500 kg

# Speed measurements
speed_of_light = db.get_measurement("speed of light")  # 299,792,458 m/s
```

### Custom Measurements
```python
# Add your own measurements
db.add_measurement("my coffee mug", Quantity(350.0, "milliliter"))
db.add_measurement("my commute", Quantity(15.0, "kilometer"))

# Search for measurements
results = db.find_measurements("bath")
for name, qty in results:
    print(f"{name}: {qty}")
```

## Natural Language Parsing

### Parse Quantities
```python
from pyquantity import parse_quantity, extract_quantities, find_units_in_text

# Parse individual quantities
qty1 = parse_quantity("5 meters")
qty2 = parse_quantity("100 km/h")

# Extract multiple quantities from text
text = "A car traveling at 120 km/h for 2.5 hours consumes 30 liters of fuel."
quantities = extract_quantities(text)

# Find units in text
units = find_units_in_text("The pressure is 1013 hPa and temperature is 25°C")
```

## Advanced Physics Calculations

### Kinematics
```python
# distance = speed × time
speed = Quantity(25.0, "meter/second")
time = Quantity(10.0, "second")
distance = speed * time

# force = mass × acceleration
mass = Quantity(10.0, "kilogram")
acceleration = Quantity(9.81, "meter/second_squared")
force = mass * acceleration
```

### Electrical Engineering
```python
# Ohm's Law: V = I × R
current = Quantity(2.0, "ampere")
resistance = Quantity(50.0, "ohm")
voltage = current * resistance

# Power: P = V × I
power = voltage * current
```

## Practical Applications

### Cooking
```python
# Convert recipe measurements
flour_cups = Quantity(2.5, "cup")
flour_ml = flour_cups.convert("milliliter")

# Calculate ingredient ratios
cup = get_measurement("cup")
tablespoon = get_measurement("tablespoon")
tbsp_per_cup = cup / tablespoon
```

### Travel
```python
# Convert speed limits
speed_mph = Quantity(65.0, "mile/hour")
speed_kmh = speed_mph.convert("kilometer/hour")

# Calculate travel time
distance = Quantity(300.0, "kilometer")
average_speed = Quantity(100.0, "kilometer/hour")
travel_time = distance / average_speed
```

### Energy Usage
```python
# Calculate appliance energy consumption
light_bulb = get_measurement("light bulb")  # 60 W
hours_per_day = Quantity(6.0, "hour")
annual_energy = light_bulb * hours_per_day * 365
annual_energy_kwh = annual_energy.convert("kilowatt_hour")
```

## Supported Units

### Base Dimensions (60+)
- **Length**: meter, kilometer, centimeter, millimeter, micrometer, nanometer, picometer, etc.
- **Mass**: kilogram, gram, milligram, microgram, tonne, etc.
- **Time**: second, millisecond, microsecond, nanosecond, minute, hour, day, week, year
- **Electric Current**: ampere, milliampere, microampere, kiloampere
- **Temperature**: kelvin, celsius, fahrenheit
- **Angle**: radian, degree, arcminute, arcsecond
- **And many more...**

### Derived Units (1000+)
- **Mechanical**: newton, pascal, joule, watt, horsepower
- **Electrical**: volt, ohm, farad, henry, siemens, coulomb, weber, tesla
- **Thermal**: calorie, british thermal unit, specific heat, thermal conductivity
- **Optical**: lumen, lux
- **Fluid**: poise, stokes, pressure units (bar, atm, torr, psi)
- **Volume**: liter, milliliter, gallon, cubic meter
- **Speed**: kilometer/hour, mile/hour, knot
- **And many more...**

### SI Prefixes (Full Range)
- **Large**: kilo (k), mega (M), giga (G), tera (T), peta (P), exa (E), zetta (Z), yotta (Y)
- **Small**: deci (d), centi (c), milli (m), micro (µ), nano (n), pico (p), femto (f), atto (a), zepto (z), yocto (y)

## Error Handling

```python
try:
    # Incompatible unit addition
    Quantity(5.0, "meter") + Quantity(3.0, "second")
except ValueError as e:
    print(f"Dimensional error: {e}")

try:
    # Invalid unit conversion
    Quantity(5.0, "meter").convert("unknown_unit")
except ValueError as e:
    print(f"Conversion error: {e}")

try:
    # Unknown unit creation
    Quantity(5.0, "invalid_unit")
except ValueError as e:
    print(f"Unit error: {e}")
```

## Performance

- **Quantity creation**: O(1) - fast and lightweight
- **Unit conversion**: O(n) where n is number of dimensions (typically < 10)
- **Parsing**: O(n) where n is text length
- **Database lookups**: O(1) - dictionary-based

## License

MIT License - See [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome! Please see the GitHub repository for contribution guidelines.

## Roadmap

### Future Enhancements
- ✅ Enhanced unit systems with 60+ dimensions
- ✅ Contextual measurements database
- ✅ Natural language parsing
- ✅ Advanced physics calculations
- 🔜 Temperature unit conversions with offset handling
- 🔜 Currency support with exchange rates
- 🔜 Custom unit system definitions
- 🔜 Enhanced NLP with machine learning
- 🔜 Visualization integration

## Support

For issues, questions, or feature requests:
- GitHub Issues: [https://github.com/odysseu/pyquantity/issues](https://github.com/odysseu/pyquantity/issues)
- Documentation: [https://github.com/odysseu/pyquantity/docs](https://github.com/odysseu/pyquantity/docs)
- Email: uboucherie1@gmail.com

## Examples

See the [examples directory](examples/) for comprehensive usage examples:
- [Basic Usage](example_usage.py)
- [Advanced Usage](example_advanced_usage.py)

## CI/CD

This project includes a comprehensive CI workflow:
- **Automatic testing** on multiple Python versions (3.10-3.14)
- **Linting** with ruff
- **Type checking** with mypy
- **Local test coverage** with pytest-cov (70% threshold)
- **Documentation building** with Sphinx
- **Package building** and artifact upload

**Local Coverage Reporting**: Test coverage is checked locally during CI runs with a minimum threshold of 70%. See the [CI workflow](.github/workflows/ci.yml) for implementation details.

**Python Version Support Policy**

Following [Python's official version support policy](https://devguide.python.org/versions/), this project supports Python versions that are either:
- In the "Feature" release phase (currently 3.14)
- In the "Bugfix" release phase (currently 3.10-3.13)
- Not in the "Security" phase only (3.9 and earlier are no longer supported)

This ensures users get the best balance of stability, security, and modern language features.

See [.github/workflows/ci.yml](.github/workflows/ci.yml) for details.

## 📦 Package Distribution

### GitHub Releases

Pre-built wheel files are automatically created and uploaded to GitHub Releases when version tags are pushed:

```bash
# To create a new release
git tag v1.0.0
git push origin v1.0.0
```

### Downloading Wheel Files

**From GitHub Releases:**
1. Go to the [Releases page](https://github.com/your-username/pyquantity/releases)
2. Download the appropriate wheel file for your platform
3. Install using pip:
   ```bash
   pip install pyquantity-1.0.0-py3-none-any.whl
   ```

**From CI Artifacts (Development Builds):**
1. Go to the [GitHub Actions](https://github.com/your-username/pyquantity/actions) tab
2. Click on the latest successful workflow run
3. Download the "python-package-distributions" artifact
4. Extract and install the wheel file

**From PyPI (Coming Soon):**
```bash
pip install pyquantity
```

### Development Installation

To install the latest development version:

```bash
# Clone the repository
git clone https://github.com/your-username/pyquantity.git
cd pyquantity

# Install in development mode
pip install -e ".[dev]"
```
