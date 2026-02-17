"""
Test cases for the quantity parser functionality.
"""

import pytest
from pyquantity.parser import QuantityParser, parse_quantities
from pyquantity.core import Quantity


def test_basic_parsing():
    """Test basic quantity extraction from text."""
    parser = QuantityParser()
    
    # Test simple sentence
    text = "The voltage is 230 V and the current is 10 A."
    quantities = parser.extract_quantities(text)
    
    assert len(quantities) == 2
    
    # Check voltage
    voltage = quantities[0]
    assert voltage['value'] == 230.0
    assert voltage['unit'] == 'volt'
    assert voltage['object'] == 'voltage'
    assert isinstance(voltage['quantity'], Quantity)
    
    # Check current
    current = quantities[1]
    assert current['value'] == 10.0
    assert current['unit'] == 'ampere'
    assert current['object'] == 'current'
    assert isinstance(current['quantity'], Quantity)


def test_json_output():
    """Test JSON output format."""
    text = "The voltage is 230 V and the current is 10 A."
    json_result = parse_quantities(text, format='json')
    
    # Should be valid JSON
    import json
    data = json.loads(json_result)
    
    assert len(data) == 2
    assert data[0]['object'] == 'voltage'
    assert data[0]['value'] == 230.0
    assert data[0]['unit'] == 'volt'


def test_list_output():
    """Test list output format."""
    text = "The voltage is 230 V and the current is 10 A."
    list_result = parse_quantities(text, format='list')
    
    assert len(list_result) == 2
    assert list_result[0]['object'] == 'voltage'
    assert list_result[0]['value'] == 230.0
    assert list_result[0]['unit'] == 'volt'


def test_objects_output():
    """Test objects output format."""
    text = "The voltage is 230 V and the current is 10 A."
    objects_result = parse_quantities(text, format='objects')
    
    assert len(objects_result) == 2
    assert objects_result[0]['object'] == 'voltage'
    assert objects_result[0]['value'] == 230.0
    assert objects_result[0]['unit'] == 'volt'
    assert isinstance(objects_result[0]['quantity'], Quantity)


def test_complex_sentence():
    """Test parsing of a more complex sentence."""
    text = "The circuit has 230V voltage, 10A current, 50Hz frequency, and 100Ω resistance."
    quantities = parse_quantities(text, format='list')
    
    assert len(quantities) == 4
    
    # Check that we have the expected quantities
    units = [q['unit'] for q in quantities]
    assert 'volt' in units
    assert 'ampere' in units
    assert 'hertz' in units
    assert 'ohm' in units


def test_unit_normalization():
    """Test unit normalization."""
    parser = QuantityParser()
    
    # Test various unit formats
    test_cases = [
        ("5 meters", 5.0, "meter"),
        ("3.14 kg", 3.14, "kilogram"),
        ("2.5km", 2.5, "kilometer"),
        ("100mA", 100.0, "milliampere"),
        ("47kΩ", 47.0, "kiloohm"),
    ]
    
    for text, expected_value, expected_unit in test_cases:
        quantities = parser.extract_quantities(text)
        assert len(quantities) == 1
        q = quantities[0]
        assert q['value'] == expected_value
        assert q['unit'] == expected_unit


def test_context_detection():
    """Test context-based object type detection."""
    parser = QuantityParser()
    
    # Test voltage detection
    text1 = "The voltage across the resistor is 5V"
    quantities1 = parser.extract_quantities(text1)
    assert quantities1[0]['object'] == 'voltage'
    
    # Test current detection
    text2 = "The current through the circuit is 2A"
    quantities2 = parser.extract_quantities(text2)
    assert quantities2[0]['object'] == 'current'
    
    # Test power detection
    text3 = "The power consumption is 100W"
    quantities3 = parser.extract_quantities(text3)
    assert quantities3[0]['object'] == 'power'


def test_scientific_notation():
    """Test parsing of scientific notation."""
    text = "The capacitance is 1e-6 F and resistance is 4.7e3 Ω."
    quantities = parse_quantities(text, format='list')
    
    assert len(quantities) == 2
    assert quantities[0]['value'] == 1e-6
    assert quantities[0]['unit'] == 'farad'
    assert quantities[1]['value'] == 4.7e3
    assert quantities[1]['unit'] == 'ohm'


def test_invalid_quantities():
    """Test that invalid quantities are skipped."""
    text = "The voltage is 230 V, but the color is blue, and temperature is hot."
    quantities = parse_quantities(text, format='list')
    
    # Should only extract the valid quantity
    assert len(quantities) == 1
    assert quantities[0]['value'] == 230.0
    assert quantities[0]['unit'] == 'volt'


def test_multiple_formats():
    """Test that the convenience function works with different formats."""
    text = "230 V, 10 A"
    
    # Test list format
    list_result = parse_quantities(text, 'list')
    assert isinstance(list_result, list)
    assert len(list_result) == 2
    
    # Test JSON format
    json_result = parse_quantities(text, 'json')
    assert isinstance(json_result, str)
    import json
    data = json.loads(json_result)
    assert len(data) == 2
    
    # Test objects format
    objects_result = parse_quantities(text, 'objects')
    assert isinstance(objects_result, list)
    assert len(objects_result) == 2
    assert isinstance(objects_result[0]['quantity'], Quantity)


def test_error_handling():
    """Test error handling for invalid format."""
    with pytest.raises(ValueError):
        parse_quantities("test", format="invalid")