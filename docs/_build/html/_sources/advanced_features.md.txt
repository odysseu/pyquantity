# Advanced Features Guide

This guide covers the enhanced features of PyQuantity, including expanded unit systems, contextual measurements, and natural language parsing.

## Table of Contents

- [Enhanced Unit Systems](#enhanced-unit-systems)
- [Contextual Measurements](#contextual-measurements)
- [Natural Language Parsing](#natural-language-parsing)
- [Advanced Physics Calculations](#advanced-physics-calculations)
- [Practical Applications](#practical-applications)

## Enhanced Unit Systems

PyQuantity now supports a comprehensive set of units and dimensions beyond the basic SI units.

### Expanded Base Dimensions

```python
from pyquantity import Dimension

# All available dimensions:
Dimension.LENGTH          # Length
Dimension.MASS            # Mass
Dimension.TIME            # Time
Dimension.ELECTRIC_CURRENT # Electric current
Dimension.TEMPERATURE     # Temperature
Dimension.AMOUNT_OF_SUBSTANCE # Amount of substance
Dimension.LUMINOUS_INTENSITY # Luminous intensity
Dimension.ANGLE           # Plane angle
Dimension.SOLID_ANGLE     # Solid angle
Dimension.FREQUENCY       # Frequency
Dimension.FORCE           # Force
Dimension.PRESSURE        # Pressure
Dimension.ENERGY          # Energy
Dimension.POWER           # Power
Dimension.ELECTRIC_CHARGE # Electric charge
Dimension.ELECTRIC_POTENTIAL # Electric potential
Dimension.CAPACITANCE     # Capacitance
Dimension.RESISTANCE      # Resistance
Dimension.CONDUCTANCE     # Conductance
Dimension.MAGNETIC_FLUX   # Magnetic flux
Dimension.MAGNETIC_FLUX_DENSITY # Magnetic flux density
Dimension.INDUCTANCE      # Inductance
Dimension.LUMINOUS_FLUX   # Luminous flux
Dimension.ILLUMINANCE      # Illuminance
Dimension.RADIOACTIVITY    # Radioactivity
Dimension.ABSORBED_DOSE    # Absorbed dose
Dimension.EQUIVALENT_DOSE  # Equivalent dose
Dimension.CATALYTIC_ACTIVITY # Catalytic activity
```

### Comprehensive Derived Units

#### Mechanical Units

```python
# Speed and velocity
speed = Quantity(25.0, "meter/second")
speed_kmh = speed.convert("kilometer/hour")  # ~90 km/h

# Acceleration
acceleration = Quantity(9.81, "meter/second_squared")  # Gravity

# Area
area = Quantity(25.0, "square_meter")

# Volume
volume = Quantity(1.0, "cubic_meter")
volume_liters = volume.convert("liter")  # 1000 liters

# Pressure
pressure = Quantity(101325.0, "pascal")
pressure_atm = pressure.convert("atmosphere")  # 1 atm

# Energy
energy = Quantity(1000.0, "joule")
energy_cal = energy.convert("calorie")  # ~239 cal

# Power
power = Quantity(100.0, "watt")
power_hp = power.convert("horsepower")  # ~0.134 hp
```

#### Electrical Units

```python
# Voltage
voltage = Quantity(230.0, "volt")
voltage_mv = voltage.convert("millivolt")  # 230000 mV

# Current
current = Quantity(10.0, "ampere")
current_ma = current.convert("milliampere")  # 10000 mA

# Resistance
resistance = Quantity(470.0, "ohm")
resistance_kohm = resistance.convert("kiloohm")  # 0.47 kΩ

# Capacitance
capacitance = Quantity(100.0, "microfarad")
capacitance_f = capacitance.convert("farad")  # 0.0001 F

# Inductance
inductance = Quantity(10.0, "millihenry")
inductance_h = inductance.convert("henry")  # 0.01 H

# Frequency
frequency = Quantity(50.0, "hertz")
frequency_khz = frequency.convert("kilohertz")  # 0.05 kHz
```

#### Thermal Units

```python
# Temperature
temp_c = Quantity(25.0, "celsius")
temp_f = Quantity(77.0, "fahrenheit")
temp_k = Quantity(298.15, "kelvin")

# Specific heat
specific_heat = Quantity(4186.0, "joule/kilogram/kelvin")  # Water

# Thermal conductivity
conductivity = Quantity(0.6, "watt/meter/kelvin")  # Typical insulator
```

#### Optical Units

```python
# Luminous flux
luminous_flux = Quantity(1000.0, "lumen")

# Illuminance
illuminance = Quantity(500.0, "lux")
```

### SI Prefixes

PyQuantity supports the full range of SI prefixes from yocto (10^-24) to yotta (10^24):

```python
# Large prefixes
distance = Quantity(1.0, "kilometer")     # 10^3 meters
distance = Quantity(1.0, "megameter")     # 10^6 meters
distance = Quantity(1.0, "gigameter")     # 10^9 meters
distance = Quantity(1.0, "terameter")     # 10^12 meters
distance = Quantity(1.0, "petameter")     # 10^15 meters

# Small prefixes
distance = Quantity(1.0, "millimeter")    # 10^-3 meters
distance = Quantity(1.0, "micrometer")    # 10^-6 meters
distance = Quantity(1.0, "nanometer")     # 10^-9 meters
distance = Quantity(1.0, "picometer")     # 10^-12 meters
distance = Quantity(1.0, "femtometer")    # 10^-15 meters
distance = Quantity(1.0, "attometer")     # 10^-18 meters

# Electrical prefixes
voltage = Quantity(1.0, "millivolt")      # 10^-3 volts
voltage = Quantity(1.0, "microvolt")      # 10^-6 volts
voltage = Quantity(1.0, "nanovolt")       # 10^-9 volts

current = Quantity(1.0, "microampere")    # 10^-6 amperes
current = Quantity(1.0, "nanoampere")     # 10^-9 amperes

resistance = Quantity(1.0, "kiloohm")      # 10^3 ohms
resistance = Quantity(1.0, "megaohm")      # 10^6 ohms
```

### Unit Conversion Examples

```python
# Speed conversions
speed_mph = Quantity(60.0, "mile/hour")
speed_mps = speed_mph.convert("meter/second")  # ~26.82 m/s
speed_kmh = speed_mph.convert("kilometer/hour")  # ~96.56 km/h

# Pressure conversions
pressure_psi = Quantity(14.7, "psi")
pressure_pa = pressure_psi.convert("pascal")  # ~101325 Pa
pressure_bar = pressure_psi.convert("bar")    # ~1.01325 bar

# Volume conversions
volume_gal = Quantity(1.0, "gallon")
volume_l = volume_gal.convert("liter")      # ~3.785 L
volume_ml = volume_gal.convert("milliliter")  # ~3785 mL

# Energy conversions
energy_kwh = Quantity(1.0, "kilowatt_hour")
energy_j = energy_kwh.convert("joule")      # 3,600,000 J
energy_cal = energy_kwh.convert("kilocalorie")  # ~860 kcal
```

## Contextual Measurements

PyQuantity includes a database of real-world objects with standard measurements.

### Using the Measurement Database

```python
from pyquantity import MeasurementDatabase, get_measurement

# Create database instance
db = MeasurementDatabase()

# Get standard measurements
bath = db.get_measurement("normal bath")
print(f"Normal bath: {bath}")  # 150.0 liter

cup = db.get_measurement("cup")
print(f"Standard cup: {cup}")  # 250.0 milliliter

# Calculate how many cups in a bath
cups_in_bath = bath / cup
print(f"Cups in a bath: {cups_in_bath:.1f}")  # ~600.0
```

### Available Measurement Categories

#### Volume Measurements

```python
# Small volumes
teaspoon = get_measurement("teaspoon")        # 5 mL
tablespoon = get_measurement("tablespoon")    # 15 mL
cup = get_measurement("cup")                  # 250 mL
glass = get_measurement("glass")              # 200 mL

# Medium volumes
bottle = get_measurement("bottle")          # 500 mL
can = get_measurement("can")                  # 330 mL
jug = get_measurement("jug")                  # 1 L
bucket = get_measurement("bucket")            # 10 L

# Large volumes
bathtub = get_measurement("bathtub")          # 150 L
normal_bath = get_measurement("normal bath")    # 150 L
swimming_pool = get_measurement("swimming pool") # 50,000 L
ocean = get_measurement("ocean")              # 1.332e21 L
```

#### Mass Measurements

```python
grain_of_salt = get_measurement("grain of salt")  # 0.06 mg
paperclip = get_measurement("paperclip")        # 1 g
apple = get_measurement("apple")                # 150 g
loaf_of_bread = get_measurement("loaf of bread") # 500 g
bag_of_sugar = get_measurement("bag of sugar")   # 1 kg

average_person = get_measurement("average person") # 70 kg
car = get_measurement("car mass")              # 1500 kg
elephant = get_measurement("elephant")          # 5000 kg
blue_whale = get_measurement("blue whale")      # 150,000 kg
```

#### Length Measurements

```python
grain_of_sand = get_measurement("grain of sand")  # 0.5 mm
credit_card = get_measurement("credit card")    # 85.6 mm
smartphone = get_measurement("smartphone")      # 150 mm
pizza = get_measurement("pizza")                # 30 cm
door = get_measurement("door")                  # 2 m
room = get_measurement("room")                  # 5 m

football_field = get_measurement("football field length") # 100 m
marathon = get_measurement("marathon")         # 42.195 km
mount_everest = get_measurement("mount everest") # 8848 m
```

#### Speed Measurements

```python
snail = get_measurement("snail")                  # 0.05 m/s
walking = get_measurement("walking")            # 1.4 m/s
running = get_measurement("running")            # 5.0 m/s
cycling = get_measurement("cycling")            # 7.0 m/s
car = get_measurement("car speed")             # 25.0 m/s

high_speed_train = get_measurement("high speed train") # 83.0 m/s
airplane = get_measurement("airplane")          # 250.0 m/s
speed_of_sound = get_measurement("speed of sound") # 343.0 m/s
speed_of_light = get_measurement("speed of light") # 299,792,458 m/s
```

### Custom Measurements

```python
# Create custom database
db = MeasurementDatabase()

# Add custom measurements
db.add_measurement("my coffee mug", Quantity(350.0, "milliliter"))
db.add_measurement("my commute", Quantity(15.0, "kilometer"))
db.add_measurement("my workspace", Quantity(10.0, "square_meter"))

# Retrieve custom measurements
mug = db.get_measurement("my coffee mug")
commute = db.get_measurement("my commute")
workspace = db.get_measurement("my workspace")

print(f"My coffee mug: {mug}")
print(f"My commute distance: {commute}")
print(f"My workspace area: {workspace}")
```

### Searching Measurements

```python
# Search for measurements containing specific terms
bath_results = db.find_measurements("bath")
print("Measurements containing 'bath':")
for name, quantity in bath_results:
    print(f"  {name}: {quantity}")

# Search for speed-related measurements
speed_results = db.find_measurements("speed")
print("Speed-related measurements:")
for name, quantity in speed_results:
    print(f"  {name}: {quantity}")
```

## Natural Language Parsing

PyQuantity can extract quantities and units from natural language text.

### Parsing Individual Quantities

```python
from pyquantity import parse_quantity

# Parse simple quantities
qty1 = parse_quantity("5 meters")
print(qty1)  # 5.0 meter

qty2 = parse_quantity("100 km/h")
print(qty2)  # 100.0 kilometer/hour

qty3 = parse_quantity("2.5 kilograms")
print(qty3)  # 2.5 kilogram

qty4 = parse_quantity("150 liters")
print(qty4)  # 150.0 liter
```

### Extracting Multiple Quantities

```python
from pyquantity import extract_quantities

text = "A car traveling at 120 km/h for 2.5 hours consumes 30 liters of fuel."
quantities = extract_quantities(text)

print(f"Found {len(quantities)} quantities:")
for i, qty in enumerate(quantities, 1):
    print(f"  {i}. {qty}")
```

### Finding Units in Text

```python
from pyquantity import find_units_in_text

text = "The pressure is 1013 hPa and temperature is 25°C with humidity at 60%."
units = find_units_in_text(text)

print(f"Found {len(units)} units:")
for unit in units:
    print(f"  - {unit}")
```

### Contextual Object Recognition

```python
text = "I filled the bathtub and it took 15 minutes to fill."
# The parser can recognize "bathtub" as a known object with standard volume

# Find objects in text
objects_found = []
for object_name, quantity in db.measurements.items():
    if object_name in text.lower():
        objects_found.append((object_name, quantity))

print("Recognized objects:")
for name, qty in objects_found:
    print(f"  {name}: {qty}")
```

### Advanced Parsing Examples

```python
# Complex units
complex_text = "The acceleration is 9.81 m/s² and pressure is 101.325 kPa"
quantities = extract_quantities(complex_text)

# Scientific notation
scientific_text = "The capacitance is 1e-6 F and resistance is 4.7e3 Ω"
quantities = extract_quantities(scientific_text)

# Mixed units
mixed_text = "Speed: 60 mph, Distance: 100 km, Time: 2.5 hours"
quantities = extract_quantities(mixed_text)
```

## Advanced Physics Calculations

### Kinematics

```python
# distance = speed × time
speed = Quantity(25.0, "meter/second")
time = Quantity(10.0, "second")
distance = speed * time
print(f"Distance: {distance}")  # 250.0 meter/second*second

# acceleration = (final_velocity - initial_velocity) / time
initial_velocity = Quantity(0.0, "meter/second")
final_velocity = Quantity(10.0, "meter/second")
time = Quantity(5.0, "second")
acceleration = (final_velocity - initial_velocity) / time
print(f"Acceleration: {acceleration}")  # 2.0 meter/second/second
```

### Dynamics

```python
# force = mass × acceleration
mass = Quantity(10.0, "kilogram")
acceleration = Quantity(9.81, "meter/second_squared")
force = mass * acceleration
print(f"Force: {force}")  # 98.1 kilogram*meter/second_squared (newton)

# power = force × velocity
velocity = Quantity(5.0, "meter/second")
power = force * velocity
print(f"Power: {power}")  # 490.5 kilogram*meter²/second³ (watt)

# work = force × distance
work = force * distance
print(f"Work: {work}")  # 2452.5 kilogram*meter²/second² (joule)
```

### Energy Calculations

```python
# kinetic energy = 0.5 × mass × velocity²
mass = Quantity(1000.0, "kilogram")  # 1000 kg car
velocity = Quantity(25.0, "meter/second")  # ~90 km/h
kinetic_energy = 0.5 * mass * (velocity ** 2)
print(f"Kinetic energy: {kinetic_energy}")  # 312500.0 kilogram*meter²/second²

# Convert to kilowatt-hours
energy_kwh = kinetic_energy.convert("kilowatt_hour")
print(f"Energy in kWh: {energy_kwh}")  # ~0.0868 kWh

# potential energy = mass × gravity × height
height = Quantity(10.0, "meter")
gravity = Quantity(9.81, "meter/second_squared")
potential_energy = mass * gravity * height
print(f"Potential energy: {potential_energy}")  # 98100.0 kilogram*meter²/second²
```

### Electrical Engineering

```python
# Ohm's Law: V = I × R
current = Quantity(2.0, "ampere")
resistance = Quantity(50.0, "ohm")
voltage = current * resistance
print(f"Voltage: {voltage}")  # 100.0 ampere*ohm (volt)

# Power: P = V × I
power = voltage * current
print(f"Power: {power}")  # 200.0 ampere*ohm*ampere (watt)

# Energy: E = P × t
energy = power * Quantity(10.0, "second")
print(f"Energy: {energy}")  # 2000.0 ampere*ohm*ampere*second (joule)

# RC time constant: τ = R × C
resistance = Quantity(1000.0, "ohm")
capacitance = Quantity(100.0, "microfarad")
time_constant = resistance * capacitance
print(f"Time constant: {time_constant}")  # 0.1 ohm*farad (second)
```

### Thermodynamics

```python
# Heat transfer: Q = m × c × ΔT
mass = Quantity(1.0, "kilogram")  # 1 kg water
specific_heat = Quantity(4186.0, "joule/kilogram/kelvin")
temp_change = Quantity(10.0, "kelvin")
heat_energy = mass * specific_heat * temp_change
print(f"Heat energy: {heat_energy}")  # 41860.0 joule

# Heat transfer rate: Q/t
heat_power = heat_energy / Quantity(60.0, "second")
print(f"Heat power: {heat_power}")  # ~697.67 watt
```

## Practical Applications

### Cooking and Recipes

```python
# Convert recipe measurements
flour_cups = Quantity(2.5, "cup")
flour_ml = flour_cups.convert("milliliter")
print(f"2.5 cups of flour = {flour_ml}")  # 625.0 milliliter

# How many tablespoons in a cup?
cup = get_measurement("cup")
tablespoon = get_measurement("tablespoon")
tbsp_per_cup = cup / tablespoon
print(f"Tablespoons per cup: {tbsp_per_cup}")  # 16.666...

# Calculate total recipe volume
sugar = Quantity(1.0, "cup")
flour = Quantity(2.5, "cup")
butter = Quantity(0.5, "cup")
total_volume = sugar + flour + butter
print(f"Total volume: {total_volume}")  # 4.0 cup
```

### Travel and Navigation

```python
# Convert speed limits
speed_limit_mph = Quantity(65.0, "mile/hour")
speed_limit_kmh = speed_limit_mph.convert("kilometer/hour")
print(f"65 mph = {speed_limit_kmh}")  # ~104.6 km/h

# Calculate travel time
distance = Quantity(300.0, "kilometer")
average_speed = Quantity(100.0, "kilometer/hour")
travel_time = distance / average_speed
print(f"Travel time: {travel_time}")  # 3.0 hour

# Calculate fuel consumption
fuel_efficiency = Quantity(15.0, "kilometer/liter")  # 15 km/L
total_fuel = distance / fuel_efficiency
print(f"Fuel needed: {total_fuel}")  # 20.0 liter
```

### Home Energy Usage

```python
# Calculate appliance energy consumption
light_bulb = get_measurement("light bulb")  # 60 W
hours_per_day = Quantity(6.0, "hour")
days_per_year = 365
daily_energy = light_bulb * hours_per_day
annual_energy = daily_energy * days_per_year
annual_energy_kwh = annual_energy.convert("kilowatt_hour")
print(f"Annual energy for one light bulb: {annual_energy_kwh}")  # ~131.4 kWh

# Calculate cost
energy_price = Quantity(0.15, "dollar/kilowatt_hour")
annual_cost = annual_energy_kwh * energy_price
print(f"Annual cost: {annual_cost}")  # ~19.71 dollar
```

### Fitness and Health

```python
# Calculate calorie expenditure
running_speed = get_measurement("running")  # ~5 m/s
# Approximate MET calculation
met_value = 8.0  # Running MET value
person_mass = get_measurement("average person")  # 70 kg
time = Quantity(1.0, "hour")
calories_burned = (met_value * person_mass.value * time.value) * Quantity(1.0, "kilocalorie")
print(f"Calories burned running for 1 hour: {calories_burned}")  # ~560 kcal

# Calculate running distance
distance = running_speed * time
distance_km = distance.convert("kilometer")
print(f"Distance run: {distance_km}")  # ~18 km
```

### Engineering Applications

```python
# Structural engineering - stress calculation
force = Quantity(10000.0, "newton")
area = Quantity(0.1, "square_meter")
stress = force / area
stress_pa = stress.convert("pascal")
print(f"Stress: {stress_pa}")  # 100000.0 pascal

# Fluid dynamics - flow rate
volume = Quantity(100.0, "liter")
time = Quantity(10.0, "second")
flow_rate = volume / time
flow_rate_lps = flow_rate.convert("liter/second")
print(f"Flow rate: {flow_rate_lps}")  # 10.0 liter/second

# Electrical engineering - circuit power
voltage = Quantity(230.0, "volt")
current = Quantity(5.0, "ampere")
power = voltage * current
power_kw = power.convert("kilowatt")
print(f"Circuit power: {power_kw}")  # 1.15 kilowatt
```

## Best Practices

1. **Use Standard Units**: Prefer base units (meter, kilogram, second) for calculations
2. **Convert Early**: Convert to desired units before complex calculations
3. **Handle Exceptions**: Always catch ValueError for invalid operations
4. **Use Context**: Provide context in text for better parsing accuracy
5. **Check Dimensions**: Verify dimensional compatibility before operations
6. **Leverage Contextual Data**: Use the measurement database for real-world comparisons
7. **Parse Strategically**: Use natural language parsing for user input, direct Quantity creation for code

## Performance Considerations

- Quantity creation is fast and lightweight
- Unit conversion involves dimensional analysis which is O(n) where n is number of dimensions
- Parsing performance depends on text length and quantity density
- For bulk operations, consider caching Quantity objects
- The measurement database uses dictionary lookups for O(1) access

## Development and Release Process

### Creating Releases

PyQuantity uses GitHub Releases to distribute pre-built wheel files. Here's how to create a new release:

```bash
# 1. Update the version in pyproject.toml
# 2. Commit your changes
git add .
git commit -m "Prepare release v1.0.0"

# 3. Create an annotated tag
git tag -a v1.0.0 -m "Release v1.0.0"

# 4. Push the tag to trigger the release workflow
git push origin v1.0.0
```

The GitHub Actions release workflow will automatically:
- Build the source distribution and wheel files
- Create a GitHub Release with the tag name
- Upload the wheel and source files as release assets

### Accessing Release Artifacts

**From GitHub Releases:**
```bash
# Download from the releases page
wget https://github.com/your-username/pyquantity/releases/download/v1.0.0/pyquantity-1.0.0-py3-none-any.whl
pip install pyquantity-1.0.0-py3-none-any.whl
```

**From CI Artifacts (for development builds):**
```bash
# Download the latest CI artifact
# Go to: https://github.com/your-username/pyquantity/actions
# Download "python-package-distributions" artifact from the latest successful run
unzip python-package-distributions.zip
pip install *.whl
```

## Future Enhancements

The following features are planned for future releases:

1. **Temperature Unit Conversions**: Full support for Celsius, Fahrenheit, Kelvin conversions
2. **Currency Support**: Integration with exchange rate APIs
3. **Custom Unit Systems**: User-defined unit systems and conversions
4. **Enhanced NLP**: More sophisticated natural language understanding
5. **Unit Inference**: Automatic unit detection from context
6. **Measurement Learning**: System that learns new object measurements from usage
7. **Contextual Calculations**: Automatic calculation of derived quantities from text
8. **Visualization**: Integration with plotting libraries for quantity visualization