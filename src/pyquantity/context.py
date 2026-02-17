"""
Contextual measurements and real-world object database for pyquantity.

This module provides a database of common real-world objects with their
associated measurements, as well as natural language parsing capabilities
for extracting units and measurements from text.
"""

from typing import Dict, List, Optional, Union, Tuple
import re
from .core import Quantity, Dimension, UnitSystem


class MeasurementDatabase:
    """
    Database of real-world objects and their associated measurements.
    
    This class provides a collection of common objects with standard
    measurements (e.g., "normal bath" = 150 liters, "standard cup" = 250 ml).
    """
    
    def __init__(self):
        # Initialize with standard measurements
        self.measurements = {
            # Volume measurements
            "teaspoon": Quantity(5.0, "milliliter"),
            "tablespoon": Quantity(15.0, "milliliter"),
            "cup": Quantity(250.0, "milliliter"),
            "glass": Quantity(200.0, "milliliter"),
            "bottle": Quantity(500.0, "milliliter"),
            "can": Quantity(330.0, "milliliter"),
            "jug": Quantity(1.0, "liter"),
            "bucket": Quantity(10.0, "liter"),
            "bathtub": Quantity(150.0, "liter"),
            "normal bath": Quantity(150.0, "liter"),
            "swimming pool": Quantity(50000.0, "liter"),
            "ocean": Quantity(1.332e21, "liter"),  # Approximate volume of Earth's oceans
            
            # Mass measurements
            "grain of salt": Quantity(0.06, "milligram"),
            "paperclip": Quantity(1.0, "gram"),
            "apple": Quantity(150.0, "gram"),
            "loaf of bread": Quantity(500.0, "gram"),
            "bag of sugar": Quantity(1.0, "kilogram"),
            "average person": Quantity(70.0, "kilogram"),
            "car mass": Quantity(1500.0, "kilogram"),
            "elephant": Quantity(5000.0, "kilogram"),
            "blue whale": Quantity(150000.0, "kilogram"),
            
            # Length measurements
            "grain of sand": Quantity(0.5, "millimeter"),
            "credit card": Quantity(85.6, "millimeter"),
            "smartphone": Quantity(150.0, "millimeter"),
            "pizza": Quantity(30.0, "centimeter"),
            "door": Quantity(2.0, "meter"),
            "room": Quantity(5.0, "meter"),
            "football field length": Quantity(100.0, "meter"),
            "marathon": Quantity(42.195, "kilometer"),
            "mount everest": Quantity(8848.0, "meter"),
            
            # Time measurements
            "blink": Quantity(0.3, "second"),
            "breath": Quantity(4.0, "second"),
            "minute": Quantity(60.0, "second"),
            "hour": Quantity(3600.0, "second"),
            "day": Quantity(86400.0, "second"),
            "week": Quantity(604800.0, "second"),
            "month": Quantity(2.628e6, "second"),  # Average month
            "year": Quantity(3.154e7, "second"),  # Average year
            
            # Speed measurements
            "snail": Quantity(0.05, "meter/second"),
            "walking": Quantity(1.4, "meter/second"),
            "running": Quantity(5.0, "meter/second"),
            "cycling": Quantity(7.0, "meter/second"),
            "car speed": Quantity(25.0, "meter/second"),
            "high speed train": Quantity(83.0, "meter/second"),
            "airplane": Quantity(250.0, "meter/second"),
            "speed of sound": Quantity(343.0, "meter/second"),
            "speed of light": Quantity(299792458.0, "meter/second"),
            
            # Temperature measurements
            "freezing point of water": Quantity(0.0, "celsius"),
            "room temperature": Quantity(20.0, "celsius"),
            "body temperature": Quantity(37.0, "celsius"),
            "boiling point of water": Quantity(100.0, "celsius"),
            "absolute zero": Quantity(-273.15, "celsius"),
            "surface of the sun": Quantity(5500.0, "celsius"),
            
            # Energy measurements
            "calorie": Quantity(4.184, "joule"),
            "food calorie": Quantity(4184.0, "joule"),
            "battery": Quantity(10000.0, "joule"),
            "car battery": Quantity(1.0e6, "joule"),
            "gasoline liter": Quantity(3.42e7, "joule"),
            "ton of tnt": Quantity(4.184e9, "joule"),
            "atomic bomb": Quantity(8.4e13, "joule"),  # Little Boy
            
            # Power measurements
            "light bulb": Quantity(60.0, "watt"),
            "human": Quantity(100.0, "watt"),
            "car engine": Quantity(100000.0, "watt"),
            "jet engine": Quantity(1.0e8, "watt"),
            "power plant": Quantity(1.0e9, "watt"),
            "sun": Quantity(3.828e26, "watt"),
            
            # Pressure measurements
            "atmospheric pressure": Quantity(101325.0, "pascal"),
            "car tire": Quantity(200000.0, "pascal"),
            "bicycle tire": Quantity(400000.0, "pascal"),
            "deep ocean": Quantity(1.0e7, "pascal"),
            "marianas trench": Quantity(1.1e8, "pascal"),
            
            # Area measurements
            "postage stamp": Quantity(4.0, "square_centimeter"),
            "a4 paper": Quantity(0.0625, "square_meter"),
            "parking space": Quantity(12.0, "square_meter"),
            "tennis court": Quantity(260.0, "square_meter"),
            "football field area": Quantity(7140.0, "square_meter"),
            "central park": Quantity(3.41e6, "square_meter"),
            
            # Volume flow measurements
            "faucet": Quantity(0.1, "liter/second"),
            "shower": Quantity(0.2, "liter/second"),
            "garden hose": Quantity(0.5, "liter/second"),
            "fire hose": Quantity(10.0, "liter/second"),
            "river": Quantity(1000.0, "cubic_meter/second"),  # Amazon river
            "niagara falls": Quantity(2400.0, "cubic_meter/second"),
        }
    
    def get_measurement(self, object_name: str) -> Optional[Quantity]:
        """
        Get the measurement for a given object name.
        
        Args:
            object_name: The name of the object to look up
            
        Returns:
            The Quantity object if found, None otherwise
            
        Examples:
            >>> db = MeasurementDatabase()
            >>> bath = db.get_measurement("normal bath")
            >>> print(bath)
            150.0 liter
        """
        object_name = object_name.lower().strip()
        return self.measurements.get(object_name)
    
    def add_measurement(self, object_name: str, quantity: Quantity) -> None:
        """
        Add a new measurement to the database.
        
        Args:
            object_name: The name of the object
            quantity: The Quantity object representing the measurement
            
        Examples:
            >>> db = MeasurementDatabase()
            >>> db.add_measurement("my cup", Quantity(300.0, "milliliter"))
        """
        self.measurements[object_name.lower().strip()] = quantity
    
    def find_measurements(self, search_term: str) -> List[Tuple[str, Quantity]]:
        """
        Find measurements matching a search term.
        
        Args:
            search_term: The term to search for
            
        Returns:
            List of (object_name, quantity) tuples that match the search
            
        Examples:
            >>> db = MeasurementDatabase()
            >>> results = db.find_measurements("bath")
            >>> for name, qty in results:
            ...     print(f"{name}: {qty}")
        """
        search_term = search_term.lower().strip()
        return [(name, qty) for name, qty in self.measurements.items() 
                if search_term in name]


class UnitParser:
    """
    Natural language parser for units and measurements.
    
    This class can extract units and quantities from natural language text
    and convert them to Quantity objects.
    """
    
    def __init__(self, measurement_db: Optional[MeasurementDatabase] = None):
        self.measurement_db = measurement_db or MeasurementDatabase()
        
        # Common unit patterns
        self.unit_patterns = {
            # Volume patterns
            r"liters?|l|ml|milliliters?|cl|centiliters?|dl|deciliters?|hl|hectoliters?",
            r"gallons?|gal|quarts?|pts?|pints?|cups?|tablespoons?|tbsp|teaspoons?|tsp",
            
            # Mass patterns
            r"kilograms?|kg|grams?|g|milligrams?|mg|micrograms?|µg|tonnes?|tons?",
            
            # Length patterns
            r"meters?|m|centimeters?|cm|millimeters?|mm|kilometers?|km|miles?|mi|feet|ft|inches?|in",
            
            # Time patterns
            r"seconds?|s|minutes?|min|hours?|h|days?|weeks?|months?|years?",
            
            # Temperature patterns
            r"celsius|c|fahrenheit|f|kelvin|k",
            
            # Speed patterns
            r"meters? per second|m/s|km/h|mph|knots?",
            
            # Energy patterns
            r"joules?|j|calories?|cal|kilocalories?|kcal|watt hours?|wh|kilowatt hours?|kwh",
            
            # Power patterns
            r"watts?|w|kilowatts?|kw|megawatts?|mw|horsepower|hp",
            
            # Pressure patterns
            r"pascals?|pa|bars?|atm|atmospheres?|torr|psi",
        }
    
    def parse_quantity(self, text: str) -> Optional[Quantity]:
        """
        Parse a quantity from natural language text.
        
        Args:
            text: The text to parse
            
        Returns:
            A Quantity object if a valid quantity is found, None otherwise
            
        Examples:
            >>> parser = UnitParser()
            >>> qty = parser.parse_quantity("5 meters")
            >>> print(qty)
            5.0 meter
            
            >>> qty = parser.parse_quantity("100 km/h")
            >>> print(qty)
            100.0 kilometer/hour
        """
        text = text.strip().lower()
        
        # Try to match number + unit pattern (allow spaces in unit names for compound units and scientific notation)
        quantity_pattern = r"([0-9]+\.?[0-9]*[eE][+-]?[0-9]+|[0-9]+\.?[0-9]*)\s*([a-zA-Z/°µ\s]+)"
        match = re.search(quantity_pattern, text)
        
        if match:
            value = float(match.group(1))
            unit_str = match.group(2)
            
            # Clean up the unit string - preserve slashes for compound units
            unit_str = unit_str.replace("°", " degree ")
            
            # Convert common plural units to singular and handle compound units
            unit_mapping = {
                "meters": "meter",
                "kilometers": "kilometer",
                "centimeters": "centimeter",
                "millimeters": "millimeter",
                "grams": "gram",
                "kilograms": "kilogram",
                "milligrams": "milligram",
                "seconds": "second",
                "minutes": "minute",
                "hours": "hour",
                "liters": "liter",
                "milliliters": "milliliter",
                "watts": "watt",
                "kilowatts": "kilowatt",
                "volts": "volt",
                "amperes": "ampere",
                "ohms": "ohm",
                "hertz": "hertz",
                "newtons": "newton",
                "pascals": "pascal",
                "joules": "joule",
                "coulombs": "coulomb",
                "farads": "farad",
                "henrys": "henry",
                "teslas": "tesla",
                "webers": "weber",
                "lumens": "lumen",
                "luxes": "lux",
                "becquerels": "becquerel",
                "grays": "gray",
                "sieverts": "sievert",
                "katals": "katal",
                "miles": "mile",
                "feet": "foot",
                "inches": "inch",
                "yards": "yard",
                "gallons": "gallon",
                "pounds": "pound",
                "ounces": "ounce",
                # Compound units
                "km/h": "kilometer/hour",
                "kmh": "kilometer/hour",
                "m/s": "meter/second",
                "ms": "meter/second",
                "mph": "mile/hour",
                "knots": "knot",
                "km": "kilometer",  # Handle km without /h
                "hrs": "hour",  # Alternative for hours
                "l": "liter",  # Alternative for liter
                "hr": "hour",  # Abbreviation for hour
                "meters per second squared": "meter_per_second_squared",
                "meters/second squared": "meter_per_second_squared",
                "meters per second^2": "meter_per_second_squared",
                "meters/second^2": "meter_per_second_squared",
            }
            
            # Store original unit string for display purposes
            original_unit_str = unit_str
            
            # Apply unit mapping for internal processing
            if unit_str in unit_mapping:
                unit_str = unit_mapping[unit_str]
            
            try:
                # Create quantity with singular unit for internal processing
                quantity = Quantity(value, unit_str)
                # Preserve original unit string for display
                quantity.unit = original_unit_str
                return quantity
            except ValueError:
                # Unit not recognized, try to find it in our patterns
                pass
        
        # Try to find known objects
        for object_name, quantity in self.measurement_db.measurements.items():
            if object_name in text.lower():
                return quantity
        
        return None
    
    def extract_quantities(self, text: str) -> List[Quantity]:
        """
        Extract all quantities from a text.
        
        Args:
            text: The text to analyze
            
        Returns:
            List of Quantity objects found in the text
            
        Examples:
            >>> parser = UnitParser()
            >>> quantities = parser.extract_quantities("A car traveling at 100 km/h for 2 hours")
            >>> for qty in quantities:
            ...     print(qty)
        """
        quantities = []
        
        # Use regex to find all quantity patterns in the text
        # This pattern matches numbers followed by units (with optional whitespace)
        quantity_pattern = re.compile(r'(\d+\.?\d*)\s*([a-zA-Z/]+)')
        
        for match in quantity_pattern.finditer(text):
            value_str, unit_str = match.groups()
            try:
                value = float(value_str)
                # Try to parse this specific quantity
                quantity = self.parse_quantity(f"{value} {unit_str}")
                if quantity:
                    quantities.append(quantity)
            except (ValueError, AttributeError):
                # Skip invalid quantities
                continue
        
        return quantities
    
    def find_units_in_text(self, text: str) -> List[str]:
        """
        Find all unit references in text.
        
        Args:
            text: The text to analyze
            
        Returns:
            List of unit strings found in the text
            
        Examples:
            >>> parser = UnitParser()
            >>> units = parser.find_units_in_text("The speed is 5 m/s and pressure is 1013 hPa")
            >>> print(units)
            ['meter/second', 'hectopascal']
        """
        units_found = []
        text_lower = text.lower()
        
        # Check for known units from our database
        all_units = set()
        all_units.update(UnitSystem.BASE_UNITS.keys())
        all_units.update(UnitSystem.DERIVED_UNITS.keys())
        
        # Also include common unit abbreviations
        unit_abbreviations = {
            'hpa': 'hectopascal',
            'c': 'celsius',
            'f': 'fahrenheit',
            'k': 'kelvin',
            'm': 'meter',
            's': 'second',
            'kg': 'kilogram',
            'g': 'gram',
            'l': 'liter',
            'ml': 'milliliter',
            'km': 'kilometer',
            'cm': 'centimeter',
            'mm': 'millimeter',
            'h': 'hour',
            'min': 'minute',
            'pa': 'pascal',
            'kpa': 'kilopascal',
            'mpa': 'megapascal',
            'bar': 'bar',
            'psi': 'psi',
            'atm': 'atmosphere',
            'w': 'watt',
            'kw': 'kilowatt',
            'j': 'joule',
            'kj': 'kilojoule',
            'v': 'volt',
            'a': 'ampere',
            'ohm': 'ohm',
            'hz': 'hertz',
            'khz': 'kilohertz',
            'mhz': 'megahertz',
            'ghz': 'gigahertz',
            'nm': 'nanometer',
            'um': 'micrometer',
            'mm': 'millimeter',
            'km': 'kilometer',
            'm/s': 'meter/second',
            'km/h': 'kilometer/hour',
            'mph': 'mile/hour',
            'rpm': 'revolution/minute'
        }
        
        # Check for full unit names first (using word boundaries)
        import re
        for unit in all_units:
            # Use word boundary regex to avoid substring matches
            if re.search(r'\b' + re.escape(unit) + r'\b', text_lower):
                units_found.append(unit)
        
        # Check for unit abbreviations (using word boundaries)
        for abbr, full_unit in unit_abbreviations.items():
            if re.search(r'\b' + re.escape(abbr) + r'\b', text_lower) and full_unit not in units_found:
                units_found.append(full_unit)
        
        return units_found


# Global instance for convenience
default_measurement_db = MeasurementDatabase()
default_parser = UnitParser(default_measurement_db)


def get_measurement(object_name: str) -> Optional[Quantity]:
    """
    Convenience function to get a measurement from the default database.
    
    Args:
        object_name: The name of the object to look up
        
    Returns:
        The Quantity object if found, None otherwise
    """
    return default_measurement_db.get_measurement(object_name)


def parse_quantity(text: str) -> Optional[Quantity]:
    """
    Convenience function to parse a quantity from text.
    
    Args:
        text: The text to parse
        
    Returns:
        A Quantity object if a valid quantity is found, None otherwise
    """
    return default_parser.parse_quantity(text)


def extract_quantities(text: str) -> List[Quantity]:
    """
    Convenience function to extract quantities from text.
    
    Args:
        text: The text to analyze
        
    Returns:
        List of Quantity objects found in the text
    """
    return default_parser.extract_quantities(text)


def find_units_in_text(text: str) -> List[str]:
    """
    Convenience function to find units in text.
    
    Args:
        text: The text to analyze
        
    Returns:
        List of unit strings found in the text
    """
    return default_parser.find_units_in_text(text)
