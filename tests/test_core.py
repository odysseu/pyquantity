"""
Test cases for the core functionality of pyquantity.
"""

import pytest
from pyquantity.core import Quantity, Dimension, UnitSystem


def test_quantity_creation():
    """Test that Quantity objects can be created correctly."""
    q = Quantity(5.0, "meter")
    assert q.value == 5.0
    assert q.unit == "meter"


def test_quantity_repr():
    """Test the string representation of Quantity objects."""
    q = Quantity(5.0, "meter")
    assert repr(q) == "Quantity(5.0, 'meter')"
    assert str(q) == "5.0 meter"


def test_quantity_conversion():
    """Test unit conversion functionality."""
    # Test meter to centimeter conversion
    q1 = Quantity(1.0, "meter")
    q1_cm = q1.convert("centimeter")
    assert q1_cm.value == 100.0
    assert q1_cm.unit == "centimeter"
    
    # Test centimeter to meter conversion
    q2 = Quantity(100.0, "centimeter")
    q2_m = q2.convert("meter")
    assert q2_m.value == 1.0
    assert q2_m.unit == "meter"
    
    # Test same unit conversion (should just copy)
    q3 = Quantity(5.0, "kilogram")
    q3_kg = q3.convert("kilogram")
    assert q3_kg.value == 5.0
    assert q3_kg.unit == "kilogram"
    
    # Test prefix conversions
    q4 = Quantity(1.0, "kilometer")
    q4_m = q4.convert("meter")
    assert q4_m.value == 1000.0
    assert q4_m.unit == "meter"
    
    q5 = Quantity(1000.0, "millimeter")
    q5_m = q5.convert("meter")
    assert q5_m.value == 1.0
    assert q5_m.unit == "meter"


def test_quantity_equality():
    """Test equality comparison for Quantity objects."""
    q1 = Quantity(5.0, "meter")
    q2 = Quantity(5.0, "meter")
    q3 = Quantity(10.0, "meter")
    q4 = Quantity(500.0, "centimeter")  # Same as 5.0 meter
    
    assert q1 == q2
    assert q1 != q3
    assert q1 == q4  # Different units but same value
    assert not (q1 == "not a quantity")


def test_quantity_arithmetic():
    """Test arithmetic operations between quantities."""
    # Test addition
    q1 = Quantity(5.0, "meter")
    q2 = Quantity(3.0, "meter")
    q3 = q1 + q2
    assert q3.value == 8.0
    assert q3.unit == "meter"
    
    # Test subtraction
    q4 = Quantity(10.0, "meter")
    q5 = Quantity(4.0, "meter")
    q6 = q4 - q5
    assert q6.value == 6.0
    assert q6.unit == "meter"
    
    # Test multiplication by scalar
    q7 = Quantity(2.0, "meter")
    q8 = q7 * 3.0
    assert q8.value == 6.0
    assert q8.unit == "meter"
    
    # Test division by scalar
    q9 = Quantity(6.0, "meter")
    q10 = q9 / 2.0
    assert q10.value == 3.0
    assert q10.unit == "meter"
    
    # Test multiplication of quantities
    q11 = Quantity(2.0, "meter")
    q12 = Quantity(3.0, "meter")
    q13 = q11 * q12
    assert q13.value == 6.0
    assert q13.unit == "meter*meter"
    
    # Test division of quantities
    q14 = Quantity(6.0, "meter")
    q15 = Quantity(2.0, "meter")
    q16 = q14 / q15
    assert q16.value == 3.0
    assert q16.unit == "meter/meter"


def test_quantity_comparison():
    """Test comparison operators for Quantity objects."""
    q1 = Quantity(5.0, "meter")
    q2 = Quantity(3.0, "meter")
    q3 = Quantity(5.0, "meter")
    q4 = Quantity(500.0, "centimeter")  # Same as 5.0 meter
    
    assert q1 > q2
    assert q1 >= q2
    assert q2 < q1
    assert q2 <= q1
    assert q1 >= q3
    assert q1 <= q3
    assert q1 == q4
    assert q1 >= q4
    assert q4 <= q1


def test_dimensional_analysis():
    """Test dimensional analysis and compatibility checking."""
    # Test that incompatible units cannot be added
    q1 = Quantity(5.0, "meter")
    q2 = Quantity(3.0, "second")
    
    with pytest.raises(ValueError):
        q1 + q2
    
    with pytest.raises(ValueError):
        q1 - q2
    
    with pytest.raises(ValueError):
        _ = q1 == q2
    
    with pytest.raises(ValueError):
        _ = q1 < q2
    
    # Test that incompatible units cannot be converted
    with pytest.raises(ValueError):
        q1.convert("second")


def test_electrical_units():
    """Test electrical units and conversions."""
    # Test voltage and current
    voltage = Quantity(230.0, "volt")
    current = Quantity(10.0, "ampere")
    
    # Power = Voltage * Current (results in watt)
    power = voltage * current
    assert power.value == 2300.0
    assert power.unit == "volt*ampere"  # This should be watt, but our system handles the multiplication
    
    # Test resistance
    resistance = Quantity(100.0, "ohm")
    
    # V = I * R
    voltage_calculated = current * resistance
    assert voltage_calculated.value == 1000.0
    assert voltage_calculated.unit == "ampere*ohm"


def test_prefix_handling():
    """Test SI prefix handling."""
    # Test various prefixes
    q1 = Quantity(1.0, "kilometer")
    q2 = Quantity(1000.0, "meter")
    assert q1 == q2
    
    q3 = Quantity(1.0, "megavolt")
    q4 = Quantity(1000000.0, "volt")
    assert q3 == q4
    
    q5 = Quantity(1.0, "millisecond")
    q6 = Quantity(0.001, "second")
    assert q5 == q6
    
    q7 = Quantity(1.0, "microampere")
    q8 = Quantity(0.000001, "ampere")
    assert q7 == q8
    
    # Test new prefix units
    q9 = Quantity(1.0, "gigawatt")
    q10 = Quantity(1e9, "watt")
    assert q9 == q10
    
    q11 = Quantity(1.0, "nanosecond")
    q12 = Quantity(1e-9, "second")
    assert q11 == q12
    
    q13 = Quantity(1.0, "picofarad")
    q14 = Quantity(1e-12, "farad")
    assert q13 == q14


def test_negation_and_abs():
    """Test negation and absolute value operations."""
    q1 = Quantity(5.0, "meter")
    q2 = -q1
    assert q2.value == -5.0
    assert q2.unit == "meter"
    
    q3 = Quantity(-3.0, "meter")
    q4 = abs(q3)
    assert q4.value == 3.0
    assert q4.unit == "meter"
    
    q5 = Quantity(4.0, "meter")
    q6 = +q5
    assert q6.value == 4.0
    assert q6.unit == "meter"


def test_invalid_conversions():
    """Test that invalid conversions raise appropriate errors."""
    q1 = Quantity(5.0, "meter")
    
    with pytest.raises(ValueError):
        q1.convert("unknown_unit")
    
    with pytest.raises(ValueError):
        q1.convert("second")  # Incompatible dimensions


def test_new_derived_units():
    """Test the new derived units."""
    # Test speed units
    speed1 = Quantity(25.0, "meter/second")
    speed2 = Quantity(90.0, "kilometer/hour")  # 25 m/s ≈ 90 km/h
    assert abs(speed1.value - speed2.convert("meter/second").value) < 0.1
    
    # Test acceleration
    acceleration = Quantity(9.81, "meter/second_squared")
    assert acceleration.unit == "meter/second_squared"
    
    # Test area
    area = Quantity(25.0, "square_meter")
    assert area.unit == "square_meter"
    
    # Test volume
    volume = Quantity(1.0, "cubic_meter")
    volume_liters = volume.convert("liter")
    assert abs(volume_liters.value - 1000.0) < 0.1
    
    # Test pressure
    pressure = Quantity(101325.0, "pascal")
    pressure_atm = pressure.convert("atmosphere")
    assert abs(pressure_atm.value - 1.0) < 0.01
    
    # Test energy
    energy = Quantity(1000.0, "joule")
    energy_cal = energy.convert("calorie")
    assert abs(energy_cal.value - 239.0) < 0.1  # 1000 J ≈ 239 cal


def test_complex_conversions():
    """Test complex unit conversions."""
    # Test speed conversion: mph to m/s
    speed_mph = Quantity(60.0, "mile/hour")
    speed_mps = speed_mph.convert("meter/second")
    assert abs(speed_mps.value - 26.8224) < 0.01  # 60 mph ≈ 26.8224 m/s
    
    # Test pressure conversion: psi to pascal
    pressure_psi = Quantity(14.7, "psi")
    pressure_pa = pressure_psi.convert("pascal")
    assert abs(pressure_pa.value - 101352.0) < 1.0  # 14.7 psi ≈ 101352 Pa
    
    # Test volume conversion: gallons to liters
    volume_gal = Quantity(1.0, "gallon")
    volume_l = volume_gal.convert("liter")
    assert abs(volume_l.value - 3.78541) < 0.0001  # 1 gal ≈ 3.78541 L


def test_physics_calculations():
    """Test physics calculations with derived units."""
    # Kinematic equation: distance = speed × time
    speed = Quantity(10.0, "meter/second")
    time = Quantity(5.0, "second")
    distance = speed * time
    assert distance.value == 50.0
    assert distance.unit == "meter/second*second"
    
    # Force = mass × acceleration
    mass = Quantity(5.0, "kilogram")
    acceleration = Quantity(9.81, "meter/second_squared")
    force = mass * acceleration
    assert abs(force.value - 49.05) < 0.01
    
    # Power = force × velocity
    velocity = Quantity(2.0, "meter/second")
    power = force * velocity
    assert abs(power.value - 98.1) < 0.1


def test_electrical_calculations():
    """Test electrical engineering calculations."""
    # Ohm's Law: V = I × R
    current = Quantity(2.0, "ampere")
    resistance = Quantity(50.0, "ohm")
    voltage = current * resistance
    assert voltage.value == 100.0
    assert voltage.unit == "ampere*ohm"
    
    # Power: P = V × I
    power = voltage * current
    assert power.value == 200.0
    assert power.unit == "ampere*ohm*ampere"
    
    # Energy: E = P × t
    time = Quantity(10.0, "second")
    energy = power * time
    assert energy.value == 2000.0
    assert energy.unit == "ampere*ohm*ampere*second"


def test_unit_system_dimensions():
    """Test the UnitSystem dimension analysis."""
    # Test base units
    meter_dims = UnitSystem.get_dimensions("meter")
    assert meter_dims == {Dimension.LENGTH: 1}
    
    # Test derived units
    speed_dims = UnitSystem.get_dimensions("meter/second")
    assert speed_dims == {Dimension.LENGTH: 1, Dimension.TIME: -1}
    
    acceleration_dims = UnitSystem.get_dimensions("meter/second_squared")
    assert acceleration_dims == {Dimension.LENGTH: 1, Dimension.TIME: -2}
    
    force_dims = UnitSystem.get_dimensions("newton")
    assert force_dims == {Dimension.LENGTH: 1, Dimension.MASS: 1, Dimension.TIME: -2}
    
    # Test that incompatible units have different dimensions
    meter_dims = UnitSystem.get_dimensions("meter")
    second_dims = UnitSystem.get_dimensions("second")
    assert meter_dims != second_dims