"""
Test cases for the contextual measurements and natural language parsing functionality.
"""

from pyquantity.context import (
    MeasurementDatabase,
    UnitParser,
    extract_quantities,
    find_units_in_text,
    parse_quantity,
)
from pyquantity.core import Quantity


def test_measurement_database():
    """Test the MeasurementDatabase functionality."""
    db = MeasurementDatabase()

    # Test getting known measurements
    bath = db.get_measurement("normal bath")
    assert bath is not None
    assert bath.value == 150.0
    assert bath.unit == "liter"

    cup = db.get_measurement("cup")
    assert cup is not None
    assert cup.value == 250.0
    assert cup.unit == "milliliter"

    # Test getting unknown measurement
    unknown = db.get_measurement("unknown object")
    assert unknown is None

    # Test adding a new measurement
    new_measurement = Quantity(300.0, "milliliter")
    db.add_measurement("my custom cup", new_measurement)

    retrieved = db.get_measurement("my custom cup")
    assert retrieved is not None
    assert retrieved.value == 300.0
    assert retrieved.unit == "milliliter"

    # Test case insensitivity
    bath_lower = db.get_measurement("NORMAL BATH")
    assert bath_lower is not None
    assert bath_lower.value == 150.0


def test_measurement_search():
    """Test the measurement search functionality."""
    db = MeasurementDatabase()

    # Test finding measurements containing "bath"
    bath_results = db.find_measurements("bath")
    assert len(bath_results) >= 2  # Should find "bathtub" and "normal bath"

    for name, qty in bath_results:
        assert "bath" in name.lower()
        assert qty is not None

    # Test finding measurements containing "cup"
    cup_results = db.find_measurements("cup")
    assert len(cup_results) >= 1  # Should find "cup"

    # Test finding non-existent term
    unknown_results = db.find_measurements("xyz123")
    assert len(unknown_results) == 0


def test_unit_parser_basic():
    """Test basic unit parsing functionality."""
    parser = UnitParser()

    # Test parsing simple quantities
    qty1 = parser.parse_quantity("5 meters")
    assert qty1 is not None
    assert qty1.value == 5.0
    assert qty1.unit == "meters"  # Note: unit gets normalized

    qty2 = parser.parse_quantity("100 km/h")
    assert qty2 is not None
    assert qty2.value == 100.0
    assert qty2.unit == "km/h"

    qty3 = parser.parse_quantity("2.5 kilograms")
    assert qty3 is not None
    assert qty3.value == 2.5
    assert qty3.unit == "kilograms"

    # Test parsing with spaces
    qty4 = parser.parse_quantity("15  liters")
    assert qty4 is not None
    assert qty4.value == 15.0
    assert qty4.unit == "liters"

    # Test parsing invalid quantity
    qty5 = parser.parse_quantity("invalid text")
    assert qty5 is None


def test_parse_quantity_function():
    """Test the convenience parse_quantity function."""
    # Test valid quantities
    qty1 = parse_quantity("10 meters")
    assert qty1 is not None
    assert qty1.value == 10.0

    qty2 = parse_quantity("3.14159 seconds")
    assert qty2 is not None
    assert abs(qty2.value - 3.14159) < 1e-5

    # Test invalid quantity
    qty3 = parse_quantity("no units here")
    assert qty3 is None


def test_extract_quantities():
    """Test extracting multiple quantities from text."""
    text = "A car traveling at 120 km/h for 2.5 hours consumes 30 liters of fuel."
    quantities = extract_quantities(text)

    assert len(quantities) == 3

    # Check the extracted quantities
    speed_found = False
    time_found = False
    volume_found = False

    for qty in quantities:
        if abs(qty.value - 120.0) < 0.1 and "km/h" in qty.unit:
            speed_found = True
        elif abs(qty.value - 2.5) < 0.1 and "hour" in qty.unit:
            time_found = True
        elif abs(qty.value - 30.0) < 0.1 and "liter" in qty.unit:
            volume_found = True

    assert speed_found
    assert time_found
    assert volume_found


def test_find_units_in_text():
    """Test finding unit references in text."""
    text = "The pressure is 1013 hPa and temperature is 25°C with humidity at 60%."
    units = find_units_in_text(text)

    # Should find at least hectopascal (hPa) and celsius (C)
    assert len(units) >= 2

    # Check that we find expected units
    found_hpa = any("pascal" in unit.lower() for unit in units)
    found_celsius = any("celsius" in unit.lower() for unit in units)

    assert found_hpa
    assert found_celsius


def test_contextual_object_recognition():
    """Test recognition of real-world objects in text."""
    db = MeasurementDatabase()

    # Test text mentioning known objects
    text = "I filled the bathtub with water and it took 15 minutes to fill."

    # Find objects in text
    objects_found = []
    for object_name, quantity in db.measurements.items():
        if object_name in text.lower():
            objects_found.append((object_name, quantity))

    # Should find bathtub
    assert len(objects_found) >= 1

    bathtub_found = False
    for name, qty in objects_found:
        if "bathtub" in name:
            bathtub_found = True
            assert qty.value == 150.0
            assert qty.unit == "liter"

    assert bathtub_found


def test_complex_parsing_scenarios():
    """Test complex parsing scenarios."""
    # Test with multiple units in one phrase
    text = "5 meters per second squared"
    qty = parse_quantity(text)
    assert qty is not None
    assert qty.value == 5.0
    # Unit parsing may vary, but should contain the key components
    assert "meter" in qty.unit.lower()
    assert "second" in qty.unit.lower()

    # Test with fractional values
    text2 = "1.5 kilograms"
    qty2 = parse_quantity(text2)
    assert qty2 is not None
    assert qty2.value == 1.5
    assert "kilogram" in qty2.unit.lower()

    # Test with scientific notation
    text3 = "2.5e3 watts"
    qty3 = parse_quantity(text3)
    assert qty3 is not None
    assert qty3.value == 2500.0
    assert "watt" in qty3.unit.lower()


def test_measurement_calculations():
    """Test calculations using contextual measurements."""
    db = MeasurementDatabase()

    # Get measurements
    bath = db.get_measurement("normal bath")
    cup = db.get_measurement("cup")

    assert bath is not None
    assert cup is not None

    # Calculate how many cups in a bath
    cups_per_bath = bath / cup
    assert cups_per_bath.value > 500  # Should be around 600
    assert cups_per_bath.value < 700

    # Test with mass measurements
    person = db.get_measurement("average person")
    car = db.get_measurement("car mass")

    assert person is not None
    assert car is not None

    # Calculate ratio
    ratio = car / person
    assert ratio.value > 10  # Car is much heavier than a person
    assert ratio.value < 30


def test_unit_parser_with_custom_db():
    """Test UnitParser with custom measurement database."""
    # Create custom database
    custom_db = MeasurementDatabase()
    custom_db.add_measurement("my unit", Quantity(42.0, "meter"))

    # Create parser with custom database
    parser = UnitParser(custom_db)

    # Test parsing with custom object
    qty = parser.parse_quantity("the my unit object")
    assert qty is not None
    assert qty.value == 42.0
    assert qty.unit == "meter"

    # Test that standard parsing still works
    qty2 = parser.parse_quantity("100 meters")
    assert qty2 is not None
    assert qty2.value == 100.0
    assert qty2.unit == "meters"


def test_edge_cases():
    """Test edge cases and error handling."""
    # Test empty string
    qty1 = parse_quantity("")
    assert qty1 is None

    # Test string with no numbers
    qty2 = parse_quantity("meters")
    assert qty2 is None

    # Test string with no units
    qty3 = parse_quantity("100")
    assert qty3 is None  # Should fail because no unit specified

    # Test very large numbers
    qty4 = parse_quantity("1e10 meters")
    assert qty4 is not None
    assert qty4.value == 1e10

    # Test very small numbers
    qty5 = parse_quantity("1e-10 seconds")
    assert qty5 is not None
    assert qty5.value == 1e-10
