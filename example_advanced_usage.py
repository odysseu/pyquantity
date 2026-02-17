"""
Advanced usage examples for pyquantity with enhanced unit systems and contextual measurements.

This example demonstrates the new features including:
1. Expanded unit systems with many more dimensions
2. Prefix units (kilo, mega, milli, micro, etc.)
3. Derived units (speed, acceleration, force, etc.)
4. Contextual measurements and real-world objects
5. Natural language parsing for units and measurements
"""

from pyquantity import (
    MeasurementDatabase,
    Quantity,
    extract_quantities,
    find_units_in_text,
    get_measurement,
    parse_quantity,
)


def demonstrate_expanded_units() -> None:
    """Demonstrate the expanded unit systems and derived units."""
    print("=== Expanded Unit Systems ===")

    # Basic derived units
    print("\n1. Basic Derived Units:")
    speed = Quantity(25.0, "meter/second")
    print(f"Speed: {speed}")

    acceleration = Quantity(9.81, "meter/second_squared")
    print(f"Acceleration: {acceleration}")

    force = Quantity(100.0, "newton")
    print(f"Force: {force}")

    pressure = Quantity(101325.0, "pascal")
    print(f"Pressure: {pressure}")

    energy = Quantity(1000.0, "joule")
    print(f"Energy: {energy}")

    power = Quantity(100.0, "watt")
    print(f"Power: {power}")

    # Electrical units
    print("\n2. Electrical Units:")
    voltage = Quantity(230.0, "volt")
    current = Quantity(10.0, "ampere")
    resistance = Quantity(470.0, "ohm")
    capacitance = Quantity(100.0, "microfarad")

    print(f"Voltage: {voltage}")
    print(f"Current: {current}")
    print(f"Resistance: {resistance}")
    print(f"Capacitance: {capacitance}")

    # Power calculation
    electrical_power = voltage * current
    print(f"Electrical Power (V*A): {electrical_power}")
    print(f"Electrical Power in watts: {electrical_power.convert('watt')}")

    # Prefix units
    print("\n3. Prefix Units:")
    distance_mm = Quantity(1000.0, "millimeter")
    distance_m = distance_mm.convert("meter")
    print(f"1000 mm = {distance_m}")

    time_ms = Quantity(500.0, "millisecond")
    time_s = time_ms.convert("second")
    print(f"500 ms = {time_s}")

    voltage_mv = Quantity(5000.0, "millivolt")
    voltage_v = voltage_mv.convert("volt")
    print(f"5000 mV = {voltage_v}")

    # Large prefix units
    distance_km = Quantity(1.5, "kilometer")
    distance_m = distance_km.convert("meter")
    print(f"1.5 km = {distance_m}")

    power_kw = Quantity(2.5, "kilowatt")
    power_w = power_kw.convert("watt")
    print(f"2.5 kW = {power_w}")

    # Very small units
    capacitance_pf = Quantity(100.0, "picofarad")
    capacitance_f = capacitance_pf.convert("farad")
    print(f"100 pF = {capacitance_f}")

    # Complex derived units
    print("\n4. Complex Derived Units:")

    # Area
    area = Quantity(25.0, "square_meter")
    print(f"Area: {area}")

    # Volume
    volume = Quantity(3.5, "cubic_meter")
    volume_liters = volume.convert("liter")
    print(f"Volume: {volume} = {volume_liters}")

    # Volume flow rate
    flow_rate = Quantity(2.5, "liter/second")
    print(f"Flow rate: {flow_rate}")

    # Density
    density = Quantity(1000.0, "kilogram/cubic_meter")
    print(f"Density of water: {density}")

    # Temperature conversions
    print("\n5. Temperature Conversions:")
    temp_c = Quantity(25.0, "celsius")
    print(f"Room temperature: {temp_c}")

    # Note: Temperature unit conversions would need special handling
    # as they involve offset calculations, not just scaling


def demonstrate_contextual_measurements() -> None:
    """Demonstrate contextual measurements and real-world objects."""
    print("\n=== Contextual Measurements ===")

    # Using the measurement database
    print("\n1. Real-world Object Measurements:")

    db = MeasurementDatabase()

    # Volume measurements
    bath = db.get_measurement("normal bath")
    print(f"Normal bath volume: {bath}")

    cup = db.get_measurement("cup")
    print(f"Standard cup volume: {cup}")

    # How many cups in a bath?
    if bath and cup:
        cups_in_bath = bath / cup
        print(f"Cups in a normal bath: {cups_in_bath.value:.1f} {cups_in_bath.unit}")

    # Mass measurements
    person = db.get_measurement("average person")
    print(f"Average person mass: {person}")

    car = db.get_measurement("car mass")
    print(f"Average car mass: {car}")

    if person and car:
        car_to_person_ratio = car / person
        print(f"Car mass / person mass ratio: {car_to_person_ratio.value:.1f} {car_to_person_ratio.unit}")

    # Speed measurements
    speed_of_light = db.get_measurement("speed of light")
    print(f"Speed of light: {speed_of_light}")

    airplane_speed = db.get_measurement("airplane")
    print(f"Airplane speed: {airplane_speed}")

    if speed_of_light and airplane_speed:
        speed_ratio = speed_of_light / airplane_speed
        print(f"Speed of light / airplane speed ratio: {speed_ratio.value:.0f} {speed_ratio.unit}")

    # Energy measurements
    atomic_bomb = db.get_measurement("atomic bomb")
    print(f"Atomic bomb energy: {atomic_bomb}")

    # Search for measurements
    print("\n2. Searching for Measurements:")
    bath_results = db.find_measurements("bath")
    print("Measurements containing 'bath':")
    for name, qty in bath_results:
        print(f"  {name}: {qty}")


def demonstrate_natural_language_parsing() -> None:
    """Demonstrate natural language parsing capabilities."""
    print("\n=== Natural Language Parsing ===")

    from src.pyquantity.context import MeasurementDatabase
    db = MeasurementDatabase()

    print("\n1. Parsing Individual Quantities:")

    # Simple quantity parsing
    qty1 = parse_quantity("5 meters")
    print(f"'5 meters' -> {qty1}")

    qty2 = parse_quantity("100 km/h")
    print(f"'100 km/h' -> {qty2}")

    qty3 = parse_quantity("2.5 kilograms")
    print(f"'2.5 kilograms' -> {qty3}")

    qty4 = parse_quantity("150 liters")
    print(f"'150 liters' -> {qty4}")

    print("\n2. Extracting Quantities from Text:")

    text = "A car traveling at 120 km/h for 2.5 hours consumes 30 liters of fuel."
    quantities = extract_quantities(text)

    print(f"Text: '{text}'")
    print("Extracted quantities:")
    for i, qty in enumerate(quantities, 1):
        print(f"  {i}. {qty}")

    print("\n3. Finding Units in Text:")

    text2 = "The pressure is 1013 hPa and temperature is 25°C with humidity at 60%."
    units = find_units_in_text(text2)

    print(f"Text: '{text2}'")
    print("Found units:")
    for unit in units:
        print(f"  - {unit}")

    print("\n4. Contextual Object Recognition:")

    # Text mentioning real-world objects
    text3 = "I filled the bathtub and it took 15 minutes."
    objects_found = []

    for object_name, quantity in db.measurements.items():
        if object_name in text3.lower():
            objects_found.append((object_name, quantity))

    print(f"Text: '{text3}'")
    print("Recognized objects:")
    for name, qty in objects_found:
        print(f"  {name}: {qty}")


def demonstrate_advanced_calculations() -> None:
    """Demonstrate advanced calculations with the new units."""
    print("\n=== Advanced Calculations ===")

    print("\n1. Physics Calculations:")

    # Kinematic equation: distance = speed × time
    speed = Quantity(25.0, "meter/second")
    time = Quantity(10.0, "second")
    distance = speed * time
    print(f"Distance = {speed} × {time} = {distance}")

    # Force = mass × acceleration
    mass = Quantity(10.0, "kilogram")
    acceleration = Quantity(9.81, "meter/second_squared")
    force = mass * acceleration
    print(f"Force = {mass} × {acceleration} = {force}")

    # Power = force × velocity
    velocity = Quantity(5.0, "meter/second")
    power = force * velocity
    print(f"Power = {force} × {velocity} = {power}")

    print("\n2. Unit Conversion Chains:")

    # Convert from miles per hour to meters per second
    speed_mph = Quantity(60.0, "mile/hour")
    speed_mps = speed_mph.convert("meter/second")
    print(f"60 mph = {speed_mps}")

    # Convert from pounds per square inch to pascals
    pressure_psi = Quantity(14.7, "psi")
    pressure_pa = pressure_psi.convert("pascal")
    print(f"14.7 psi = {pressure_pa}")

    print("\n3. Energy Calculations:")

    # Kinetic energy = 0.5 × mass × velocity²
    mass_kg = Quantity(1000.0, "kilogram")  # 1000 kg car
    kinetic_energy = 0.5 * mass_kg * velocity * velocity
    print(f"Kinetic energy of car: {kinetic_energy}")

    # Convert to kilowatt-hours
#     energy_kwh = kinetic_energy.convert("kilowatt_hour")
#     print(f"Same energy in kWh: {energy_kwh}")

    print("\n4. Electrical Engineering:")

    # Ohm's Law: V = I × R
    voltage = Quantity(230.0, "volt")
    current = Quantity(5.0, "ampere")
    resistance = voltage / current
    print(f"Resistance = {voltage} / {current} = {resistance}")

    # Power: P = V × I
    power = voltage * current
    print(f"Power = {voltage} × {current} = {power}")

    # Energy: E = P × t
    time_h = Quantity(2.0, "hour")
    energy = power * time_h
    print(f"Energy = {power} × {time_h} = {energy}")


def demonstrate_practical_applications() -> None:
    """Demonstrate practical real-world applications."""
    print("\n=== Practical Applications ===")

    print("\n1. Cooking and Recipes:")

    # Convert recipe measurements
    flour_cups = Quantity(2.5, "cup")
    flour_ml = flour_cups.convert("milliliter")
    print(f"2.5 cups of flour = {flour_ml}")

    # How many tablespoons in a cup?
    cup = get_measurement("cup")
    tablespoon = get_measurement("tablespoon")
    if cup and tablespoon:
        tbsp_per_cup = cup / tablespoon
        print(f"Tablespoons per cup: {tbsp_per_cup}")

    print("\n2. Travel and Navigation:")

    # Convert speed limits
    speed_limit_mph = Quantity(65.0, "mile/hour")
    speed_limit_kmh = speed_limit_mph.convert("kilometer/hour")
    print(f"65 mph = {speed_limit_kmh}")

    # Calculate travel time
    distance_km = Quantity(300.0, "kilometer")
    average_speed = Quantity(100.0, "kilometer/hour")
    travel_time_h = distance_km / average_speed
    print(f"Travel time for {distance_km} at {average_speed}: {travel_time_h}")

    print("\n3. Home Energy Usage:")

    # Calculate energy consumption
    light_bulb_power = get_measurement("light bulb")
    if light_bulb_power:
        hours_per_day = Quantity(6.0, "hour")
        days_per_year = Quantity(365.0, "")  # Dimensionless
        annual_energy = light_bulb_power * hours_per_day * days_per_year
        annual_energy_kwh = annual_energy.convert("kilowatt_hour")
        print(f"Annual energy for one light bulb: {annual_energy_kwh}")

    print("\n4. Fitness and Health:")

    # Calculate calorie burn
    running_speed = get_measurement("running")
    if running_speed:
        # Approximate: 1 MET = 1 kcal/kg/hour for running
        # 1 MET ≈ 3.5 ml O2/kg/min, running ≈ 8 METs
        met_value = 8.0
        person_mass = get_measurement("average person")
        if person_mass:
            time_h = Quantity(1.0, "hour")
            calories_burned = (met_value * person_mass.value * time_h.value) * Quantity(1.0, "kilocalorie")
            print(f"Calories burned running for 1 hour: {calories_burned}")


if __name__ == "__main__":
    print("PyQuantity Advanced Usage Examples")
    print("=" * 50)

    demonstrate_expanded_units()
    demonstrate_contextual_measurements()
    demonstrate_natural_language_parsing()
    demonstrate_advanced_calculations()
    demonstrate_practical_applications()

    print("\n" + "=" * 50)
    print("Examples completed!")
