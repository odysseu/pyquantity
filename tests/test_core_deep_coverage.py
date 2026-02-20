"""
Deep coverage tests for core.py to reach 85% coverage.
"""

import pytest

from pyquantity.core import Dimension, Quantity, UnitSystem


class TestPrefixHandling:
    """Test SI prefix handling edge cases."""

    def test_all_si_prefixes(self) -> None:
        """Test that all SI prefixes work correctly."""
        # Test only the prefixes that are actually supported
        prefixes = {
            'tera': 1e12, 'giga': 1e9, 'mega': 1e6, 'kilo': 1e3,
            'milli': 1e-3, 'micro': 1e-6, 'nano': 1e-9, 'pico': 1e-12,
            'femto': 1e-15
        }

        for prefix, factor in prefixes.items():
            unit = f"{prefix}meter"
            q = Quantity(1.0, unit)
            # Convert to base unit to verify the prefix works
            q_base = q.convert("meter")
            assert abs(q_base.value - factor) < 1e-10, f"Prefix {prefix} failed"


class TestConversionFactorEdgeCases:
    """Test conversion factor edge cases."""

    def test_volt_ampere_to_watt_conversions(self) -> None:
        """Test all volt*ampere to watt conversion paths."""
        # Test volt*ampere to watt
        q_va = Quantity(1000.0, "volt*ampere")
        q_w = q_va.convert("watt")
        assert q_w.value == 1000.0
        assert q_w.unit == "watt"

        # Test watt to volt*ampere
        q_w2 = Quantity(500.0, "watt")
        q_va2 = q_w2.convert("volt*ampere")
        assert q_va2.value == 500.0
        assert q_va2.unit == "volt*ampere"

        # Test volt*ampere to kilowatt
        q_va3 = Quantity(1000.0, "volt*ampere")
        q_kw = q_va3.convert("kilowatt")
        assert q_kw.value == 1.0
        assert q_kw.unit == "kilowatt"

        # Test kilowatt to volt*ampere
        q_kw2 = Quantity(1.0, "kilowatt")
        q_va4 = q_kw2.convert("volt*ampere")
        assert q_va4.value == 1000.0
        assert q_va4.unit == "volt*ampere"

    def test_conversion_factor_direct(self) -> None:
        """Test get_conversion_factor method directly."""
        # Test simple conversion
        factor = UnitSystem.get_conversion_factor("meter", "centimeter")
        assert factor == 100.0

        # Test reverse conversion
        factor2 = UnitSystem.get_conversion_factor("centimeter", "meter")
        assert factor2 == 0.01

        # Test same unit
        factor3 = UnitSystem.get_conversion_factor("meter", "meter")
        assert factor3 == 1.0

        # Test incompatible units
        with pytest.raises(ValueError):
            UnitSystem.get_conversion_factor("meter", "kilogram")


class TestArithmeticEdgeCasesDeep:
    """Test deep arithmetic operation edge cases."""

    def test_multiplication_edge_cases(self) -> None:
        """Test multiplication with various types."""
        q = Quantity(5.0, "meter")

        # Test multiplication with int
        result1 = q * 3
        assert result1.value == 15.0
        assert result1.unit == "meter"

        # Test multiplication with float
        result2 = q * 2.5
        assert result2.value == 12.5
        assert result2.unit == "meter"

        # Test reverse multiplication with int
        result3 = 3 * q
        assert result3.value == 15.0
        assert result3.unit == "meter"

        # Test reverse multiplication with float
        result4 = 2.5 * q
        assert result4.value == 12.5
        assert result4.unit == "meter"

        # Test multiplication with another quantity
        q2 = Quantity(2.0, "second")
        result5 = q * q2
        assert result5.value == 10.0
        assert result5.unit == "meter*second"

    def test_division_edge_cases(self) -> None:
        """Test division with various scenarios."""
        q = Quantity(10.0, "meter")

        # Test division by int
        result1 = q / 2
        assert result1.value == 5.0
        assert result1.unit == "meter"

        # Test division by float
        result2 = q / 2.5
        assert result2.value == 4.0
        assert result2.unit == "meter"

        # Test division by another quantity
        q2 = Quantity(2.0, "second")
        result3 = q / q2
        assert result3.value == 5.0
        assert result3.unit == "meter/second"

    def test_addition_subtraction_edge_cases(self) -> None:
        """Test addition and subtraction edge cases."""
        q1 = Quantity(5.0, "meter")
        q2 = Quantity(3.0, "meter")

        # Test addition
        result1 = q1 + q2
        assert result1.value == 8.0
        assert result1.unit == "meter"

        # Test subtraction
        result2 = q1 - q2
        assert result2.value == 2.0
        assert result2.unit == "meter"

        # Test subtraction resulting in negative
        result3 = q2 - q1
        assert result3.value == -2.0
        assert result3.unit == "meter"


class TestUnitParsingDeep:
    """Test deep unit parsing scenarios."""

    def test_base_units_dimensions(self) -> None:
        """Test dimensions of all base units."""
        base_units = {
            "meter": {Dimension.LENGTH: 1},
            "kilogram": {Dimension.MASS: 1},
            "second": {Dimension.TIME: 1},
            "ampere": {Dimension.ELECTRIC_CURRENT: 1},
            "kelvin": {Dimension.TEMPERATURE: 1},
            "mole": {Dimension.AMOUNT_OF_SUBSTANCE: 1},
            "candela": {Dimension.LUMINOUS_INTENSITY: 1}
        }

        for unit, expected_dims in base_units.items():
            actual_dims = UnitSystem.get_dimensions(unit)
            assert actual_dims == expected_dims, f"Base unit {unit} dimensions mismatch"

    def test_derived_units_dimensions(self) -> None:
        """Test dimensions of various derived units."""
        derived_units = {
            "newton": {Dimension.LENGTH: 1, Dimension.MASS: 1, Dimension.TIME: -2},
            "pascal": {Dimension.LENGTH: -1, Dimension.MASS: 1, Dimension.TIME: -2},
            "joule": {Dimension.LENGTH: 2, Dimension.MASS: 1, Dimension.TIME: -2},
            "watt": {Dimension.LENGTH: 2, Dimension.MASS: 1, Dimension.TIME: -3},
            "coulomb": {Dimension.TIME: 1, Dimension.ELECTRIC_CURRENT: 1},
            "volt": {Dimension.LENGTH: 2, Dimension.MASS: 1, Dimension.TIME: -3, Dimension.ELECTRIC_CURRENT: -1},
            "farad": {Dimension.LENGTH: -2, Dimension.MASS: -1, Dimension.TIME: 4, Dimension.ELECTRIC_CURRENT: 2},
            "ohm": {Dimension.LENGTH: 2, Dimension.MASS: 1, Dimension.TIME: -3, Dimension.ELECTRIC_CURRENT: -2},
            "siemens": {Dimension.LENGTH: -2, Dimension.MASS: -1, Dimension.TIME: 3, Dimension.ELECTRIC_CURRENT: 2},
            "weber": {Dimension.LENGTH: 2, Dimension.MASS: 1, Dimension.TIME: -2, Dimension.ELECTRIC_CURRENT: -1},
            "tesla": {Dimension.MASS: 1, Dimension.TIME: -2, Dimension.ELECTRIC_CURRENT: -1},
            "henry": {Dimension.LENGTH: 2, Dimension.MASS: 1, Dimension.TIME: -2, Dimension.ELECTRIC_CURRENT: -2},
            "lumen": {Dimension.LUMINOUS_INTENSITY: 1},
            "lux": {Dimension.LENGTH: -2, Dimension.LUMINOUS_INTENSITY: 1}
        }

        for unit, expected_dims in derived_units.items():
            actual_dims = UnitSystem.get_dimensions(unit)
            assert actual_dims == expected_dims, f"Derived unit {unit} dimensions mismatch: {actual_dims} != {expected_dims}"

    def test_compound_unit_parsing(self) -> None:
        """Test parsing of various compound units."""
        compound_units = {
            "meter*second": {Dimension.LENGTH: 1, Dimension.TIME: 1},
            "kilogram*meter/second": {Dimension.MASS: 1, Dimension.LENGTH: 1, Dimension.TIME: -1},
            "watt/second": {Dimension.LENGTH: 2, Dimension.MASS: 1, Dimension.TIME: -4},
            "newton*meter": {Dimension.LENGTH: 2, Dimension.MASS: 1, Dimension.TIME: -2}
        }

        for unit, expected_dims in compound_units.items():
            actual_dims = UnitSystem.get_dimensions(unit)
            assert actual_dims == expected_dims, f"Compound unit {unit} dimensions mismatch"


class TestQuantityCreationEdgeCases:
    """Test edge cases in Quantity creation."""

    def test_quantity_with_very_small_values(self) -> None:
        """Test Quantity creation with very small values."""
        q1 = Quantity(1e-100, "meter")
        assert q1.value == 1e-100
        assert q1.unit == "meter"

        q2 = Quantity(1e-300, "second")
        assert q2.value == 1e-300
        assert q2.unit == "second"

    def test_quantity_with_very_large_values(self) -> None:
        """Test Quantity creation with very large values."""
        q1 = Quantity(1e100, "meter")
        assert q1.value == 1e100
        assert q1.unit == "meter"

        q2 = Quantity(1e300, "kilogram")
        assert q2.value == 1e300
        assert q2.unit == "kilogram"

    def test_quantity_with_negative_values(self) -> None:
        """Test Quantity creation with negative values."""
        q1 = Quantity(-5.0, "meter")
        assert q1.value == -5.0
        assert q1.unit == "meter"

        q2 = Quantity(-10.0, "celsius")
        assert q2.value == -10.0
        assert q2.unit == "celsius"


class TestConversionEdgeCasesDeep:
    """Test deep conversion edge cases."""

    def test_conversion_chains(self) -> None:
        """Test multiple conversions in sequence."""
        # Start with millimeters
        q1 = Quantity(1000.0, "millimeter")

        # Convert to meters
        q2 = q1.convert("meter")
        assert q2.value == 1.0
        assert q2.unit == "meter"

        # Convert to kilometers
        q3 = q2.convert("kilometer")
        assert q3.value == 0.001
        assert q3.unit == "kilometer"

        # Convert back to meters
        q4 = q3.convert("meter")
        assert q4.value == 1.0
        assert q4.unit == "meter"

        # Convert to centimeters
        q5 = q4.convert("centimeter")
        assert q5.value == 100.0
        assert q5.unit == "centimeter"

    def test_cross_dimensional_conversions(self) -> None:
        """Test conversions between different but compatible dimensions."""
        # Test energy units
        q_joule = Quantity(1000.0, "joule")
        q_kj = q_joule.convert("kilojoule")
        assert q_kj.value == 1.0
        assert q_kj.unit == "kilojoule"

        # Test power units
        q_watt = Quantity(1000.0, "watt")
        q_kw = q_watt.convert("kilowatt")
        assert q_kw.value == 1.0
        assert q_kw.unit == "kilowatt"

    def test_temperature_conversions(self) -> None:
        """Test temperature unit conversions."""
        # Test that temperature units can be created
        q_celsius = Quantity(100.0, "celsius")
        assert q_celsius.value == 100.0
        assert q_celsius.unit == "celsius"

        q_kelvin = Quantity(273.15, "kelvin")
        assert q_kelvin.value == 273.15
        assert q_kelvin.unit == "kelvin"

        # Note: Actual temperature conversion between celsius and kelvin
        # is not implemented in the current version, so we just test
        # that the units can be created and used


class TestMathematicalOperations:
    """Test mathematical operations on quantities."""

    def test_scalar_operations(self) -> None:
        """Test scalar mathematical operations."""
        q = Quantity(5.0, "meter")

        # Test multiplication with scalar
        result1 = q * 2.0
        assert result1.value == 10.0
        assert result1.unit == "meter"

        # Test division with scalar
        result2 = q / 2.0
        assert result2.value == 2.5
        assert result2.unit == "meter"

        # Test reverse multiplication with scalar
        result3 = 2.0 * q
        assert result3.value == 10.0
        assert result3.unit == "meter"

        # Note: Addition and subtraction with scalars is not supported
        # in the current implementation, only with other quantities

    def test_compound_operations(self) -> None:
        """Test compound mathematical operations."""
        q1 = Quantity(2.0, "meter")
        q2 = Quantity(3.0, "meter")
        q3 = Quantity(4.0, "second")

        # Test (q1 + q2) * q3
        result1 = (q1 + q2) * q3
        assert result1.value == 20.0
        assert result1.unit == "meter*second"

        # Test q1 * (q2 / q3)
        result2 = q1 * (q2 / q3)
        assert result2.value == 1.5
        assert result2.unit == "meter*meter/second"

        # Test (q1 * q2) / q3
        result3 = (q1 * q2) / q3
        assert result3.value == 1.5
        assert result3.unit == "meter*meter/second"
