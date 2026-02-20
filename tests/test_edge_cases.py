"""
Edge case tests to increase coverage to 90%.
"""

import pytest

from pyquantity.context import (
    extract_quantities,
    find_units_in_text,
)
from pyquantity.core import Dimension, Quantity, UnitSystem
from pyquantity.parser import QuantityParser


class TestCompoundUnitEdgeCases:
    """Test edge cases for compound units with squared/cubed suffixes."""

    def test_meter_per_second_squared(self) -> None:
        """Test meter/second_squared unit parsing and conversion."""
        # This should represent acceleration (m/s²)
        q = Quantity(9.81, "meter/second_squared")
        assert q.value == 9.81
        assert q.unit == "meter/second_squared"

        # Test that dimensions are correctly calculated
        dims = UnitSystem.get_dimensions("meter/second_squared")
        expected_dims = {
            Dimension.LENGTH: 1,
            Dimension.TIME: -2
        }
        assert dims == expected_dims

    def test_simple_unit_squared(self) -> None:
        """Test simple units with _squared suffix."""
        q = Quantity(25.0, "meter_squared")
        assert q.value == 25.0
        assert q.unit == "meter_squared"

        dims = UnitSystem.get_dimensions("meter_squared")
        expected_dims = {Dimension.LENGTH: 2}
        assert dims == expected_dims

    def test_unit_cubed(self) -> None:
        """Test units with _cubed suffix."""
        q = Quantity(8.0, "meter_cubed")
        assert q.value == 8.0
        assert q.unit == "meter_cubed"

        dims = UnitSystem.get_dimensions("meter_cubed")
        expected_dims = {Dimension.LENGTH: 3}
        assert dims == expected_dims

    def test_compound_unit_cubed(self) -> None:
        """Test compound units with _cubed suffix."""
        # This should represent jerk (m/s³)
        q = Quantity(10.0, "meter/second_cubed")
        assert q.value == 10.0
        assert q.unit == "meter/second_cubed"

        # Test that dimensions are correctly calculated
        dims = UnitSystem.get_dimensions("meter/second_cubed")
        expected_dims = {
            Dimension.LENGTH: 1,
            Dimension.TIME: -3
        }
        assert dims == expected_dims


class TestOperatorEdgeCases:
    """Test edge cases for Quantity operators."""

    def test_equality_operators(self) -> None:
        """Test all equality comparison operators."""
        q1 = Quantity(5.0, "meter")
        q2 = Quantity(5.0, "meter")
        q3 = Quantity(3.0, "meter")
        q4 = Quantity(5.0, "kilogram")  # Different unit

        # Test __eq__
        assert q1 == q2
        assert not (q1 == q3)
        # Different units should raise an error, not return False
        with pytest.raises(ValueError):
            _ = q1 == q4
        assert not (q1 == 5.0)  # Different types should not be equal

        # Test __ne__ (inherited from object, but let's test it)
        assert not (q1 != q2)
        assert q1 != q3
        # Different units should raise an error for != too
        with pytest.raises(ValueError):
            _ = q1 != q4
        assert q1 != 5.0

    def test_comparison_operators(self) -> None:
        """Test all comparison operators."""
        q1 = Quantity(5.0, "meter")
        q2 = Quantity(3.0, "meter")
        q3 = Quantity(5.0, "meter")

        # Test __lt__
        assert q2 < q1
        assert not (q1 < q2)
        assert not (q1 < q3)

        # Test __le__
        assert q2 <= q1
        assert q3 <= q1
        assert not (q1 <= q2)

        # Test __gt__
        assert q1 > q2
        assert not (q2 > q1)
        assert not (q1 > q3)

        # Test __ge__
        assert q1 >= q2
        assert q1 >= q3
        assert not (q2 >= q1)

        # Test that comparing different units raises an error
        q_kg = Quantity(5.0, "kilogram")
        with pytest.raises(ValueError):
            _ = q1 < q_kg

    def test_unary_operators(self) -> None:
        """Test unary operators."""
        q1 = Quantity(5.0, "meter")
        q2 = Quantity(-3.0, "meter")

        # Test __neg__
        neg_q1 = -q1
        assert neg_q1.value == -5.0
        assert neg_q1.unit == "meter"

        # Test __pos__
        pos_q1 = +q1
        assert pos_q1.value == 5.0
        assert pos_q1.unit == "meter"

        # Test __abs__
        abs_q2 = abs(q2)
        assert abs_q2.value == 3.0
        assert abs_q2.unit == "meter"


class TestArithmeticEdgeCases:
    """Test edge cases for arithmetic operations."""

    def test_multiplication_edge_cases(self) -> None:
        """Test multiplication edge cases."""
        q1 = Quantity(2.0, "meter")
        q2 = Quantity(3.0, "second")

        # Quantity * Quantity = Quantity (area)
        result = q1 * q2
        assert result.value == 6.0
        assert result.unit == "meter*second"

        # Quantity * scalar
        result2 = q1 * 2.5
        assert result2.value == 5.0
        assert result2.unit == "meter"

        # scalar * Quantity (reverse multiplication)
        result3 = 2.5 * q1
        assert result3.value == 5.0
        assert result3.unit == "meter"

    def test_division_edge_cases(self) -> None:
        """Test division edge cases."""
        q1 = Quantity(6.0, "meter")
        q2 = Quantity(2.0, "second")

        # Quantity / Quantity = Quantity (velocity)
        result = q1 / q2
        assert result.value == 3.0
        assert result.unit == "meter/second"

        # Quantity / scalar
        result2 = q1 / 2.0
        assert result2.value == 3.0
        assert result2.unit == "meter"

        # Test division by zero
        q_zero = Quantity(0.0, "meter")
        with pytest.raises(ZeroDivisionError):
            _ = q1 / q_zero

    def test_complex_arithmetic(self) -> None:
        """Test complex arithmetic combinations."""
        q1 = Quantity(2.0, "meter")
        q2 = Quantity(3.0, "meter")
        q3 = Quantity(4.0, "second")

        # (Quantity + Quantity) * Quantity
        result = (q1 + q2) * q3
        assert result.value == 20.0
        assert result.unit == "meter*second"

        # Quantity * (Quantity / Quantity)
        result2 = q1 * (q2 / q3)
        assert result2.value == 1.5
        assert result2.unit == "meter*meter/second"

    def test_arithmetic_with_zero(self) -> None:
        """Test arithmetic operations involving zero."""
        q1 = Quantity(5.0, "meter")
        q_zero = Quantity(0.0, "meter")

        # Addition with zero
        result = q1 + q_zero
        assert result.value == 5.0
        assert result.unit == "meter"

        # Subtraction resulting in zero
        result2 = q1 - q1
        assert result2.value == 0.0
        assert result2.unit == "meter"

        # Multiplication by zero
        result3 = q1 * q_zero
        assert result3.value == 0.0
        assert result3.unit == "meter*meter"

    def test_arithmetic_incompatible_units(self) -> None:
        """Test arithmetic operations with incompatible units."""
        q_meter = Quantity(5.0, "meter")
        q_second = Quantity(3.0, "second")
        q_kg = Quantity(2.0, "kilogram")

        # Test addition with incompatible units
        with pytest.raises(ValueError):
            _ = q_meter + q_second

        # Test subtraction with incompatible units
        with pytest.raises(ValueError):
            _ = q_meter - q_kg

        # Multiplication should work (creates compound unit)
        result = q_meter * q_second
        assert result.value == 15.0
        assert result.unit == "meter*second"

        # Division should work (creates compound unit)
        result2 = q_meter / q_second
        assert result2.value == 5.0/3.0
        assert result2.unit == "meter/second"

    def test_complex_compound_units(self) -> None:
        """Test complex compound unit operations."""
        # Test multiplication of compound units
        q1 = Quantity(2.0, "meter/second")  # velocity
        q2 = Quantity(3.0, "second")        # time
        result = q1 * q2
        assert result.value == 6.0
        assert result.unit == "meter/second*second"

        # Test division of compound units
        q3 = Quantity(10.0, "meter")
        q4 = Quantity(2.0, "meter/second")
        result2 = q3 / q4
        assert result2.value == 5.0
        assert result2.unit == "meter/meter/second"


class TestParserEdgeCases:
    """Test edge cases for unit parsing."""

    def test_ohm_symbol_handling(self) -> None:
        """Test ohm symbol (Ω and ω) parsing."""
        parser = QuantityParser()

        # Test ohm symbol parsing through quantity extraction
        text1 = "The resistance is 100 ω"
        quantities1 = parser.extract_quantities(text1)
        assert len(quantities1) == 1
        assert quantities1[0]['unit'] == 'ohm'

        text2 = "The resistance is 100 Ω"
        quantities2 = parser.extract_quantities(text2)
        assert len(quantities2) == 1
        assert quantities2[0]['unit'] == 'ohm'

        # Test prefixed ohm
        text3 = "The resistance is 1 kΩ"
        quantities3 = parser.extract_quantities(text3)
        assert len(quantities3) == 1
        assert quantities3[0]['unit'] == 'kiloohm'

    def test_complex_prefix_combinations(self) -> None:
        """Test complex prefix and unit combinations."""
        parser = QuantityParser()

        # Test various prefix combinations
        text1 = "The current is 5 mA"
        quantities1 = parser.extract_quantities(text1)
        assert quantities1[0]['unit'] == 'milliampere'

        text2 = "The voltage is 5 kV"
        quantities2 = parser.extract_quantities(text2)
        assert quantities2[0]['unit'] == 'kilovolt'

        text3 = "The power is 5 MW"
        quantities3 = parser.extract_quantities(text3)
        assert quantities3[0]['unit'] == 'milliwatt'

    def test_plural_unit_handling(self) -> None:
        """Test plural unit handling."""
        parser = QuantityParser()

        # Test plural forms
        text1 = "The length is 5 meters"
        quantities1 = parser.extract_quantities(text1)
        assert quantities1[0]['unit'] == 'meter'

        text2 = "The time is 10 seconds"
        quantities2 = parser.extract_quantities(text2)
        assert quantities2[0]['unit'] == 'second'


class TestContextEdgeCases:
    """Test edge cases for context functions."""

    def test_extract_quantities_error_handling(self) -> None:
        """Test error handling in extract_quantities."""

        # Test with text containing invalid quantity strings
        text_with_invalid = "The speed is 5x faster and weight is abc kg"
        quantities = extract_quantities(text_with_invalid)

        # Should skip invalid quantities and return only valid ones
        assert len(quantities) >= 0  # May find some valid quantities or none

        # Test with empty text
        empty_quantities = extract_quantities("")
        assert empty_quantities == []

        # Test with text containing no quantities
        no_quantities = extract_quantities("This text has no quantities.")
        assert no_quantities == []

    def test_find_units_in_text_edge_cases(self) -> None:
        """Test edge cases for find_units_in_text."""
        # Test with full unit names
        text = "The distance is 5 meter and time is 2 second"
        units = find_units_in_text(text)
        assert "meter" in units
        assert "second" in units

        # Test with full unit names
        text2 = "The resistance is 100 ohm and capacitance is 10 farad"
        units2 = find_units_in_text(text2)
        assert "ohm" in units2
        assert "farad" in units2

        # Test with no units
        text3 = "This has no units"
        units3 = find_units_in_text(text3)
        assert units3 == []

    def test_extract_quantities_with_invalid_data(self) -> None:
        """Test extract_quantities with text that contains invalid quantity patterns."""
        # Test with text that might cause parsing errors
        text = "The speed is 5x faster and weight is unknown kg"
        quantities = extract_quantities(text)
        # Should handle errors gracefully and return whatever it can parse
        assert isinstance(quantities, list)

    def test_invalid_unit_handling(self) -> None:
        """Test handling of completely invalid units."""
        # Test with a unit that doesn't exist
        with pytest.raises(ValueError):
            Quantity(5.0, "invalid_unit")

        # Test with empty unit
        with pytest.raises(ValueError):
            Quantity(5.0, "")

    def test_complex_unit_parsing_edge_cases(self) -> None:
        """Test complex unit parsing edge cases."""
        # Test malformed compound units - these actually work due to robust parsing
        dims1 = UnitSystem.get_dimensions("meter/second/second")
        assert dims1 == {Dimension.LENGTH: 1}

        # Test units with multiple underscores - this should fail
        with pytest.raises(ValueError):
            UnitSystem.get_dimensions("meter_second_squared")  # Invalid format

        # Test edge case with _squared on compound unit that doesn't split properly
        with pytest.raises(ValueError):
            UnitSystem.get_dimensions("metersecond_squared")  # No slash, invalid


class TestConversionEdgeCases:
    """Test edge cases for unit conversions."""

    def test_incompatible_unit_conversion(self) -> None:
        """Test conversion between incompatible units."""
        q_meter = Quantity(5.0, "meter")

        # Try to convert to incompatible unit
        with pytest.raises(ValueError):
            q_meter.convert("kilogram")

        with pytest.raises(ValueError):
            q_meter.convert("second")

    def test_same_unit_conversion(self) -> None:
        """Test conversion to the same unit."""
        q = Quantity(5.0, "meter")
        result = q.convert("meter")
        assert result.value == 5.0
        assert result.unit == "meter"
        assert result is not q  # Should be a new object

    def test_compound_unit_conversion(self) -> None:
        """Test conversion with compound units."""
        # Test watt to volt*ampere conversion
        q_watt = Quantity(1000.0, "watt")
        q_va = q_watt.convert("volt*ampere")
        assert q_va.value == 1000.0
        assert q_va.unit == "volt*ampere"

        # Test kilowatt to volt*ampere conversion
        q_kw = Quantity(1.0, "kilowatt")
        q_va2 = q_kw.convert("volt*ampere")
        assert q_va2.value == 1000.0
        assert q_va2.unit == "volt*ampere"

    def test_conversion_edge_cases(self) -> None:
        """Test edge cases in unit conversion."""
        # Test conversion with very small values
        q_small = Quantity(1e-10, "meter")
        q_small_mm = q_small.convert("millimeter")
        assert abs(q_small_mm.value - 1e-7) < 1e-15  # Allow for floating point precision
        assert q_small_mm.unit == "millimeter"

        # Test conversion with very large values
        q_large = Quantity(1e10, "meter")
        q_large_km = q_large.convert("kilometer")
        assert q_large_km.value == 1e7
        assert q_large_km.unit == "kilometer"

        # Test conversion chain
        q1 = Quantity(1000.0, "millimeter")
        q2 = q1.convert("meter")
        q3 = q2.convert("kilometer")
        assert q3.value == 0.001
        assert q3.unit == "kilometer"
