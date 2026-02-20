# PyQuantity Usage Guide

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [Unit Conversion](#unit-conversion)
- [Arithmetic Operations](#arithmetic-operations)
- [Comparison Operations](#comparison-operations)
- [Natural Language Parsing](#natural-language-parsing)
- [Supported Units](#supported-units)
- [Advanced Features](#advanced-features)
- [Error Handling](#error-handling)
- [API Reference](#api-reference)

## Introduction

PyQuantity is a modern Python package for working with physical quantities, units, and dimensional analysis. It provides type-safe quantity representations with proper unit handling, automatic unit conversion, and comprehensive support for electrical engineering and scientific units.

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

### Development Builds (CI Artifacts)

For the latest development builds:

1. Go to the [GitHub Actions](https://github.com/odysseu/pyquantity/actions) tab
2. Click on the latest successful workflow run
3. Download the "python-package-distributions" artifact
4. Extract and install the wheel file

## Basic Usage

### Creating Quantities

```python
from pyquantity import Quantity

# Create a quantity with value and unit
length = Quantity(5.0, "meter")
width = Quantity(3.0, "meter")

# String representation
print(length)  # "5.0 meter"
print(repr(length))  # "Quantity(5.0, 'meter')"
```

### Supported Unit Formats

```python
# Various ways to specify units
Quantity(1.0, "meter")      # Base unit
Quantity(1.0, "m")          # Abbreviation
Quantity(1000.0, "mm")     # Millimeter
Quantity(1.5, "kilometer")  # Kilometer
Quantity(1.5, "km")         # Kilometer abbreviation
```

## Unit Conversion

### Basic Conversion

```python
length = Quantity(1.0, "meter")
length_cm = length.convert("centimeter")  # 100.0 centimeter
length_mm = length.convert("millimeter")  # 1000.0 millimeter
```

### Electrical Units Conversion

```python
# Voltage conversion
voltage = Quantity(230.0, "volt")
voltage_kv = voltage.convert("kilovolt")  # 0.23 kilovolt

# Current conversion
current = Quantity(500.0, "milliampere")
current_a = current.convert("ampere")  # 0.5 ampere

# Power conversion
power = Quantity(2300.0, "watt")
power_kw = power.convert("kilowatt")  # 2.3 kilowatt
```

### Temperature Units

```python
temp_c = Quantity(25.0, "celsius")
temp_f = Quantity(77.0, "fahrenheit")
temp_k = Quantity(298.15, "kelvin")
```

## Arithmetic Operations

### Basic Arithmetic

```python
# Addition and subtraction (requires compatible units)
length1 = Quantity(5.0, "meter")
length2 = Quantity(3.0, "meter")
total = length1 + length2  # 8.0 meter
difference = length1 - length2  # 2.0 meter

# Multiplication and division
area = length1 * length2  # 15.0 meter*meter
ratio = length1 / length2  # 1.666... meter/meter
```

### Scalar Operations

```python
# Multiply/divide by scalars
scaled = length1 * 2.5  # 12.5 meter
half = length1 / 2.0    # 2.5 meter

# Reverse operations
also_scaled = 2.5 * length1  # 12.5 meter
reverse_div = 10.0 / length1  # 2.0 1/meter
```

### Electrical Engineering Calculations

```python
# Ohm's Law: V = I * R
voltage = Quantity(230.0, "volt")
current = Quantity(10.0, "ampere")
resistance = voltage / current  # 23.0 volt/ampere (ohm)

# Power calculation: P = V * I
power = voltage * current  # 2300.0 volt*ampere (watt)
power_kw = power.convert("kilowatt")  # 2.3 kilowatt

# Energy calculation: E = P * t
power = Quantity(1000.0, "watt")
time = Quantity(3600.0, "second")
energy = power * time  # 3600000.0 watt*second (joule)
```

## Comparison Operations

```python
# Equality comparison
distance1 = Quantity(1.0, "meter")
distance2 = Quantity(100.0, "centimeter")
print(distance1 == distance2)  # True

# Inequality comparisons
print(distance1 > Quantity(0.5, "meter"))  # True
print(distance1 < Quantity(2.0, "meter"))  # True
print(distance1 >= Quantity(1.0, "meter"))  # True
print(distance1 <= Quantity(1.0, "meter"))  # True
```

## Natural Language Parsing

### Basic Parsing

```python
from pyquantity.parser import parse_quantities

text = "The voltage is 230V and the current is 10A"
quantities = parse_quantities(text, format='list')

# Result:
# [
#     {'object': 'voltage', 'value': 230.0, 'unit': 'volt', 'original_text': '230V'},
#     {'object': 'current', 'value': 10.0, 'unit': 'ampere', 'original_text': '10A'}
# ]
```

### Output Formats

```python
# List format (default)
list_result = parse_quantities(text, format='list')

# JSON format
json_result = parse_quantities(text, format='json')

# Full objects format (includes Quantity objects)
objects_result = parse_quantities(text, format='objects')
```

### Advanced Parsing Examples

```python
# Complex electrical specifications
complex_text = """
The circuit has:
- Voltage: 230V AC
- Current: 10A DC
- Power: 2.3kW
- Resistance: 47kΩ
- Capacitance: 100nF
- Frequency: 50Hz
- Temperature: 25°C
"""

quantities = parse_quantities(complex_text, format='list')
for q in quantities:
    print(f"{q['object']}: {q['value']} {q['unit']}")
```

### Enterprise Example: Industrial Equipment Specification

```python
# Enterprise-level example with comprehensive equipment specifications
enterprise_text = """
The HVAC system specifications are as follows:

1. Main Compressor Unit:
   - Rated Power: 75 kW
   - Voltage: 480 V AC, 3-phase
   - Current: 120 A per phase
   - Efficiency: 92%
   - Operating Temperature Range: -20°C to 50°C
   - Maximum Pressure: 35 bar
   - Cooling Capacity: 250 kW at 35°C ambient

2. Air Handling Unit:
   - Airflow Rate: 12,500 m³/h
   - Static Pressure: 450 Pa
   - Fan Power: 15 kW
   - Filtration Efficiency: 95% at 0.3 µm particles
   - Noise Level: 65 dB at 3 meters

3. Refrigerant Circuit:
   - Refrigerant Type: R-410A
   - Charge Volume: 45 kg
   - Operating Pressure (High Side): 28 bar
   - Operating Pressure (Low Side): 8 bar
   - Subcooling: 5 K
   - Superheat: 8 K

4. Control System:
   - Supply Voltage: 24 V DC
   - Control Current: 100 mA
   - Response Time: < 500 ms
   - Accuracy: ±0.5°C for temperature control
   - Communication Protocol: Modbus RTU at 9600 baud

5. Safety Features:
   - Maximum Current Protection: 150 A
   - Overpressure Protection: 40 bar
   - Overtemperature Protection: 60°C
   - Emergency Stop Response Time: < 100 ms
"""

# Parse the comprehensive specifications
spec_quantities = parse_quantities(enterprise_text, format='list')

# Organize by category
categories = {}
for q in spec_quantities:
    category = q.get('object', 'general')
    if category not in categories:
        categories[category] = []
    categories[category].append(q)

# Display organized results
for category, items in categories.items():
    print(f"\n{category.upper()}:")
    for item in items:
        print(f"  - {item['value']} {item['unit']} ({item.get('original_text', '')})")

# Example output analysis
print(f"\nTotal quantities found: {len(spec_quantities)}")
print(f"Categories identified: {len(categories)}")

# Convert to structured data for enterprise integration
structured_data = []
for q in spec_quantities:
    structured_data.append({
        'parameter': q.get('object', 'unknown'),
        'value': q['value'],
        'unit': q['unit'],
        'source_text': q.get('original_text', ''),
        'quantity_object': str(q.get('quantity', ''))
    })

# This structured data can be integrated with enterprise systems
# such as ERP, PLM, or IoT platforms
```

**Note:** The object type detection (voltage, current, pressure, etc.) is based on contextual analysis and may not always be perfect. In enterprise applications, you may want to:
- Post-process the results to refine object types
- Use the raw quantities and apply business rules for classification
- Integrate with domain-specific ontologies for better categorization

### Scientific Notation
=======

### Scientific Notation

```python
scientific_text = "Capacitance is 1e-6F and resistance is 4.7e3Ω"
quantities = parse_quantities(scientific_text)
# Parses as 1e-6 farad and 4700.0 ohm
```

### Special Symbols

```python
# Ω symbol support
resistance_text = "Resistance is 47kΩ"
quantities = parse_quantities(resistance_text)
# Parses as 47.0 kiloohm
```

## Supported Units

### Base Units

| Category | Units |
|----------|-------|
| Length | meter, kilometer, centimeter, millimeter, micrometer, nanometer |
| Mass | kilogram, gram, milligram |
| Time | second, millisecond, microsecond, nanosecond |
| Electric Current | ampere, milliampere, microampere, kiloampere |
| Temperature | kelvin, celsius, fahrenheit |
| Amount | mole |
| Luminous Intensity | candela |

### Derived Units

| Category | Units |
|----------|-------|
| **Electrical** | volt, ohm, farad, henry, siemens, weber, tesla, hertz |
| **Power** | watt, kilowatt |
| **Capacitance** | farad, microfarad, nanofarad, millifarad, picofarad |
| **Resistance** | ohm, kiloohm, megaohm, milliohm |
| **Frequency** | hertz, kilohertz, megahertz, gigahertz |
| **Pressure** | pascal |
| **Energy** | joule, kilojoule |
| **Force** | newton, kilonewton |
| **Magnetic** | weber, tesla |
| **Conductance** | siemens, millisiemens |

### Unit Abbreviations

| Full Name | Abbreviations |
|-----------|--------------|
| meter | m |
| kilogram | kg |
| second | s, sec |
| ampere | A, amp |
| volt | V |
| ohm | Ω, ohm |
| farad | F |
| henry | H |
| hertz | Hz |
| watt | W |
| kelvin | K |
| celsius | °C |
| fahrenheit | °F |

## Advanced Features

### Dimensional Analysis

```python
# This will raise ValueError - incompatible dimensions
length = Quantity(5.0, "meter")
time = Quantity(10.0, "second")

try:
    result = length + time  # ValueError: incompatible dimensions
except ValueError as e:
    print(f"Error: {e}")
```

### Compound Units

```python
# Create compound units through arithmetic
voltage = Quantity(230.0, "volt")
current = Quantity(10.0, "ampere")
power = voltage * current  # volt*ampere unit

# Convert compound units
power_watt = power.convert("watt")  # Works because volt*ampere ≡ watt
power_kw = power.convert("kilowatt")  # Also works
```

### Context-Aware Parsing

```python
# The parser detects quantity types from context
context_text = "The voltage across the resistor is 5V"
quantities = parse_quantities(context_text)
# Automatically detects this as 'voltage' type

# Different context
current_text = "The current through the circuit is 2A"
quantities = parse_quantities(current_text)
# Automatically detects this as 'current' type
```

## Error Handling

### Invalid Unit Conversion

```python
try:
    length = Quantity(5.0, "meter")
    invalid = length.convert("unknown_unit")
except ValueError as e:
    print(f"Conversion error: {e}")
```

### Incompatible Operations

```python
try:
    length = Quantity(5.0, "meter")
    time = Quantity(10.0, "second")
    result = length + time  # Incompatible dimensions
except ValueError as e:
    print(f"Operation error: {e}")
```

### Invalid Unit Creation

```python
try:
    invalid = Quantity(5.0, "invalid_unit")
except ValueError as e:
    print(f"Unit error: {e}")
```

## API Reference

### Quantity Class

```python
Quantity(value, unit)
```

**Methods:**
- `convert(target_unit)` - Convert to different unit
- `__add__(other)` - Add quantities
- `__sub__(other)` - Subtract quantities  
- `__mul__(other)` - Multiply quantities or scalars
- `__truediv__(other)` - Divide quantities or scalars
- `__eq__(other)` - Equality comparison
- `__lt__(other)`, `__le__(other)`, `__gt__(other)`, `__ge__(other)` - Comparison operators
- `__neg__()` - Negation
- `__abs__()` - Absolute value

### Parser Functions

```python
parse_quantities(text, format='list')
```

**Parameters:**
- `text` (str): Input text to parse
- `format` (str): Output format ('list', 'json', or 'objects')

**Returns:**
- List of dictionaries (format='list')
- JSON string (format='json')
- List with Quantity objects (format='objects')

### QuantityParser Class

```python
parser = QuantityParser()
quantities = parser.extract_quantities(text)
json_output = parser.extract_to_json(text)
list_output = parser.extract_to_list(text)
```

## Examples by Domain

### Electrical Engineering

```python
# Circuit analysis
voltage = Quantity(230.0, "volt")
current = Quantity(10.0, "ampere")
resistance = Quantity(100.0, "ohm")

# Ohm's Law verification
calculated_voltage = current * resistance
print(f"V = I * R: {calculated_voltage}")

# Power calculations
power = voltage * current
power_kw = power.convert("kilowatt")
print(f"Power: {power_kw}")

# Parse circuit specifications
specs = "Voltage: 230V, Current: 10A, Resistance: 100Ω"
components = parse_quantities(specs)
```

### Physics

```python
# Kinematic equations
 distance = Quantity(100.0, "meter")
 time = Quantity(10.0, "second")
 speed = distance / time  # 10.0 meter/second

# Energy calculations
 mass = Quantity(2.0, "kilogram")
 velocity = Quantity(5.0, "meter/second")
 kinetic_energy = 0.5 * mass * (velocity ** 2)  # 25.0 kilogram*meter²/second²
```

### Temperature Measurements

```python
# Temperature conversions (note: PyQuantity handles the values)
room_temp = Quantity(25.0, "celsius")
body_temp = Quantity(37.0, "celsius")
freezing = Quantity(0.0, "celsius")

# Compare temperatures
print(f"Room temperature: {room_temp}")
print(f"Is room temp comfortable? {room_temp < Quantity(30.0, 'celsius')}")
```

## Best Practices

1. **Use Standard Units**: Prefer base units (meter, kilogram, second) for calculations
2. **Convert Early**: Convert to desired units before complex calculations
3. **Handle Exceptions**: Always catch ValueError for invalid operations
4. **Use Context**: Provide context in text for better parsing accuracy
5. **Check Dimensions**: Verify dimensional compatibility before operations

## Performance Considerations

- Quantity creation is fast and lightweight
- Unit conversion involves dimensional analysis which is O(n) where n is number of dimensions
- Parsing performance depends on text length and quantity density
- For bulk operations, consider caching Quantity objects

## Contributing

Contributions are welcome! Please see the GitHub repository for contribution guidelines.

## License

MIT License - See LICENSE file for details.