#!/usr/bin/env python
"""
Example usage of the PyQuantity package.
"""

from pyquantity.core import Quantity


def main() -> None:
    print("PyQuantity Example Usage")
    print("=" * 30)

    # Create some quantities
    length = Quantity(5.0, "meter")
    width = Quantity(3.0, "meter")

    print(f"Length: {length}")
    print(f"Width: {width}")

    # Arithmetic operations
    area = length * width
    print(f"Area: {length} * {width} = {area}")

    perimeter = 2 * (length + width)
    print(f"Perimeter: 2 * ({length} + {width}) = {perimeter}")

    # Convert units
    length_cm = length.convert("centimeter")
    print(f"Length in centimeters: {length_cm}")

    # Create another quantity and convert back
    distance = Quantity(150.0, "centimeter")
    distance_m = distance.convert("meter")
    print(f"Distance: {distance} -> {distance_m}")

    # Electrical example
    print("\nElectrical Example:")
    voltage = Quantity(230.0, "volt")
    current = Quantity(10.0, "ampere")

    # Power = Voltage * Current
    power = voltage * current
    print(f"Power: {voltage} * {current} = {power}")

    # Resistance calculation
    resistance = Quantity(100.0, "ohm")
    calculated_voltage = current * resistance
    print(f"Voltage: {current} * {resistance} = {calculated_voltage}")

    # Prefix handling
    print("\nPrefix Handling:")
    distance_km = Quantity(1.5, "kilometer")
    distance_m = distance_km.convert("meter")
    print(f"Distance: {distance_km} = {distance_m}")

    current_ma = Quantity(500.0, "milliampere")
    current_a = current_ma.convert("ampere")
    print(f"Current: {current_ma} = {current_a}")

    # Comparison operations
    print("\nComparison Operations:")
    q1 = Quantity(5.0, "meter")
    q2 = Quantity(3.0, "meter")
    q3 = Quantity(500.0, "centimeter")  # Same as 5.0 meter

    print(f"{q1} > {q2}: {q1 > q2}")
    print(f"{q1} == {q3}: {q1 == q3}")
    print(f"{q2} < {q1}: {q2 < q1}")

    print("\nExample completed successfully!")

if __name__ == "__main__":
    main()
