"""
pyquantity - A modern Python package for quantity calculations.

This package provides tools for working with physical quantities, units,
and dimensional analysis.
"""

__version__ = "0.1.8"
__author__ = "odysseu"
__email__ = "uboucherie1@gmail.com"
__license__ = "MIT"

from .context import (
    MeasurementDatabase,
    UnitParser,
    extract_quantities,
    find_units_in_text,
    get_measurement,
    parse_quantity,
)
from .core import Dimension, Quantity, UnitSystem
from .parser import QuantityParser, parse_quantities

__all__ = [
    "Quantity", "Dimension", "UnitSystem",
    "QuantityParser", "parse_quantities",
    "MeasurementDatabase", "UnitParser",
    "get_measurement", "parse_quantity", "extract_quantities", "find_units_in_text"
]
