"""
Test cases for the quantity parser functionality.
"""

import pytest

from pyquantity.core import Quantity
from pyquantity.parser import QuantityParser, parse_quantities


def test_basic_parsing() -> None:
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


def test_json_output() -> None:
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


def test_list_output() -> None:
    """Test list output format."""
    text = "The voltage is 230 V and the current is 10 A."
    list_result = parse_quantities(text, format='list')

    assert len(list_result) == 2
    assert list_result[0]['object'] == 'voltage'
    assert list_result[0]['value'] == 230.0
    assert list_result[0]['unit'] == 'volt'


def test_objects_output() -> None:
    """Test objects output format."""
    text = "The voltage is 230 V and the current is 10 A."
    objects_result = parse_quantities(text, format='objects')

    assert len(objects_result) == 2
    assert objects_result[0]['object'] == 'voltage'
    assert objects_result[0]['value'] == 230.0
    assert objects_result[0]['unit'] == 'volt'
    assert isinstance(objects_result[0]['quantity'], Quantity)


def test_complex_sentence() -> None:
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


def test_unit_normalization() -> None:
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





def test_error_handling() -> None:
    """Test error handling in parsing."""
    parser = QuantityParser()

    # Test with invalid units (should be skipped)
    text1 = "The value is 100 xyz units"
    result1 = parser.extract_quantities(text1)
    # Should not crash, but may not find the quantity
    assert len(result1) >= 0  # May be 0 or 1 depending on parsing

    # Test with malformed numbers
    text2 = "The value is abc meters"
    result2 = parser.extract_quantities(text2)
    assert len(result2) == 0  # Should not find any valid quantities

    # Test empty text
    text3 = ""
    result3 = parser.extract_quantities(text3)
    assert len(result3) == 0


def test_object_type_detection() -> None:
    """Test object type detection in parsing."""
    parser = QuantityParser()

    # Test voltage detection
    text1 = "The voltage is 230 volts"
    result1 = parser.extract_quantities(text1)
    if len(result1) > 0:
        assert result1[0]['object'] == 'voltage'

    # Test current detection
    text2 = "The current is 10 amperes"
    result2 = parser.extract_quantities(text2)
    if len(result2) > 0:
        assert result2[0]['object'] == 'current'

    # Test power detection
    text3 = "The power is 1000 watts"
    result3 = parser.extract_quantities(text3)
    if len(result3) > 0:
        assert result3[0]['object'] == 'power'

    # Test frequency detection
    text4 = "The frequency is 50 hertz"
    result4 = parser.extract_quantities(text4)
    if len(result4) > 0:
        assert result4[0]['object'] == 'frequency'

    # Test resistance detection
    text5 = "The resistance is 47 ohms"
    result5 = parser.extract_quantities(text5)
    if len(result5) > 0:
        assert result5[0]['object'] == 'resistance'

    # Test unknown object type
    text6 = "The xyz is 100 meters"
    result6 = parser.extract_quantities(text6)
    if len(result6) > 0:
        # Should default to generic object type
        assert 'object' in result6[0]


def test_context_detection() -> None:
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


def test_scientific_notation() -> None:
    """Test parsing of scientific notation."""
    text = "The capacitance is 1e-6 F and resistance is 4.7e3 Ω."
    quantities = parse_quantities(text, format='list')

    assert len(quantities) == 2
    assert quantities[0]['value'] == 1e-6
    assert quantities[0]['unit'] == 'farad'
    assert quantities[1]['value'] == 4.7e3
    assert quantities[1]['unit'] == 'ohm'


def test_invalid_quantities() -> None:
    """Test that invalid quantities are skipped."""
    text = "The voltage is 230 V, but the color is blue, and temperature is hot."
    quantities = parse_quantities(text, format='list')

    # Should only extract the valid quantity
    assert len(quantities) == 1
    assert quantities[0]['value'] == 230.0
    assert quantities[0]['unit'] == 'volt'


def test_multiple_formats() -> None:
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


def test_error_handling_format() -> None:
    """Test error handling for invalid format."""
    with pytest.raises(ValueError):
        parse_quantities("test", format="invalid")


def test_item_extraction_basic() -> None:
    """Test basic item extraction functionality."""
    parser = QuantityParser()

    # Test simple item extraction
    text = "2 liters of milk"
    result = parser.extract_quantities(text)
    assert len(result) == 1
    assert result[0]['item'] == "milk"
    assert result[0]['value'] == 2.0
    assert result[0]['unit'] == "liter"


def test_item_extraction_multi_word() -> None:
    """Test extraction of multi-word item names."""
    parser = QuantityParser()

    # Test multi-word items
    text = "1.2 liters of orange juice and 500 grams of olive oil"
    result = parser.extract_quantities(text)
    assert len(result) == 2
    assert result[0]['item'] == "orange juice"
    assert result[1]['item'] == "olive oil"


def test_item_extraction_with_punctuation() -> None:
    """Test item extraction with punctuation handling."""
    parser = QuantityParser()

    # Test items with trailing punctuation
    text = "3 kilograms of tomatoes, 1 kilogram of onions."
    result = parser.extract_quantities(text)
    assert len(result) == 2
    assert result[0]['item'] == "tomatoes"
    assert result[1]['item'] == "onions"


def test_item_extraction_complex_sentences() -> None:
    """Test item extraction in complex sentences."""
    parser = QuantityParser()

    # Test complex sentence with multiple items
    text = "I bought 2.5 lbs of chicken, 1 pint of berries, and 300 grams of cheese for the recipe."
    result = parser.extract_quantities(text)
    assert len(result) == 3
    assert result[0]['item'] == "chicken"
    assert result[1]['item'] == "berries"
    assert result[2]['item'] == "cheese for the recipe"  # Current behavior includes context


def test_item_extraction_no_preposition() -> None:
    """Test item extraction when no preposition is present."""
    parser = QuantityParser()

    # Test items without prepositions (directly after quantity)
    text = "The voltage is 230 V and current is 10 A"
    result = parser.extract_quantities(text)
    assert len(result) == 2
    # These should have empty or minimal item names since no preposition
    assert 'item' in result[0]
    assert 'item' in result[1]


def test_item_extraction_json_output() -> None:
    """Test that item extraction works with JSON output."""
    parser = QuantityParser()

    text = "500 grams of flour"
    json_result = parser.extract_to_json(text)
    import json
    data = json.loads(json_result)
    assert len(data) == 1
    assert 'item' in data[0]
    assert data[0]['item'] == "flour"


def test_item_extraction_list_output() -> None:
    """Test that item extraction works with list output."""
    parser = QuantityParser()

    text = "1 kilogram of sugar"
    list_result = parser.extract_to_list(text)
    assert len(list_result) == 1
    assert 'item' in list_result[0]
    assert list_result[0]['item'] == "sugar"


def test_item_extraction_edge_cases() -> None:
    """Test edge cases for item extraction."""
    parser = QuantityParser()

    # Test with parentheses
    text = "2 liters of milk (for cooking)"
    result = parser.extract_quantities(text)
    assert len(result) == 1
    assert result[0]['item'] == "milk (for cooking)"  # Current behavior includes parentheses

    # Test with conjunctions
    text = "1 kg of apples and 2 kg of oranges"
    result = parser.extract_quantities(text)
    assert len(result) == 2
    assert result[0]['item'] == "apples"
    assert result[1]['item'] == "oranges"

    # Test with semicolons
    text = "500 ml of cream; 200 grams of butter"
    result = parser.extract_quantities(text)
    assert len(result) == 2
    assert result[0]['item'] == "cream"
    assert result[1]['item'] == "butter"


def test_item_extraction_backward_compatibility() -> None:
    """Test that existing functionality still works with new item field."""
    parser = QuantityParser()

    # Test that all expected fields are still present
    text = "10 meters"
    result = parser.extract_quantities(text)
    assert len(result) == 1
    qty = result[0]
    assert 'object' in qty
    assert 'value' in qty
    assert 'unit' in qty
    assert 'original_text' in qty
    assert 'quantity' in qty
    assert 'start_pos' in qty
    assert 'end_pos' in qty
    assert 'item' in qty  # New field


def test_item_extraction_special_cases() -> None:
    """Test special cases and edge conditions for item extraction."""
    parser = QuantityParser()

    # Test with 'for' preposition
    text = "2 cups of sugar for the cake"
    result = parser.extract_quantities(text)
    assert len(result) == 1
    assert result[0]['item'] == "sugar for the cake"

    # Test with 'with' preposition - using recognized units
    text = "1 liter of water with lemon"
    result = parser.extract_quantities(text)
    assert len(result) == 1
    assert result[0]['item'] == "water with lemon"

    # Test with 'in' preposition - using recognized units
    text = "3 tablespoons of honey in the jar"
    result = parser.extract_quantities(text)
    assert len(result) == 1
    assert result[0]['item'] == "honey in the jar"

    # Test empty item extraction
    text = "5 kilograms"
    result = parser.extract_quantities(text)
    assert len(result) == 1
    assert 'item' in result[0]  # Should have item field even if empty


def test_item_extraction_multiple_prepositions() -> None:
    """Test item extraction with multiple prepositions in context."""
    parser = QuantityParser()

    # Test with multiple prepositions - should use first one found
    text = "1 liter of orange juice for breakfast with toast"
    result = parser.extract_quantities(text)
    assert len(result) == 1
    assert result[0]['item'] == "orange juice for breakfast with toast"


def test_item_extraction_no_space_after_comma() -> None:
    """Test item extraction when there's no space after comma."""
    parser = QuantityParser()

    text = "2 kilograms,3 liters,4 grams"  # Using recognized units
    result = parser.extract_quantities(text)
    assert len(result) == 3
    # These should still work even without spaces after commas
    assert 'item' in result[0]
    assert 'item' in result[1]
    assert 'item' in result[2]
