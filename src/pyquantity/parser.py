"""
Natural language quantity parser for pyquantity.

This module provides functionality to extract quantities from text sentences
and return structured data.
"""

import re
from typing import Any

from .core import Quantity


class QuantityParser:
    """
    Parse natural language text to extract quantities with their values and units.

    This class provides methods to extract structured quantity information from
    sentences like "The voltage is 230 V and the current is 10 A".
    """

    # Common unit abbreviations and their full names
    UNIT_ABBREVIATIONS = {
        # Electrical units
        'v': 'volt', 'volts': 'volt',
        'a': 'ampere', 'amps': 'ampere',
        'w': 'watt', 'watts': 'watt',
        'ω': 'ohm', 'ohms': 'ohm',  # Include Ω symbol
        'f': 'farad', 'farads': 'farad',
        'h': 'henry', 'henrys': 'henry',
        'c': 'coulomb', 'coulombs': 'coulomb',
        's': 'siemens',
        'wb': 'weber', 'webers': 'weber',
        't': 'tesla', 'teslas': 'tesla',
        'hz': 'hertz',
        '°c': 'celsius', 'celsius': 'celsius',
        '°f': 'fahrenheit', 'fahrenheit': 'fahrenheit',

        # SI base units
        'm': 'meter', 'meters': 'meter', 'metre': 'meter', 'metres': 'meter',
        'kg': 'kilogram', 'kilograms': 'kilogram',
        'g': 'gram', 'grams': 'gram',
        'seconds': 'second', 'sec': 'second', 'secs': 'second',
        'k': 'kelvin',
        'mol': 'mole', 'moles': 'mole',
        'cd': 'candela', 'candelas': 'candela',

        # Common units
        'l': 'liter', 'liters': 'liter', 'litre': 'liter', 'litres': 'liter',
        'ml': 'milliliter', 'milliliters': 'milliliter', 'millilitre': 'milliliter',
        'km': 'kilometer', 'kilometers': 'kilometer',
        'cm': 'centimeter', 'centimeters': 'centimeter',
        'mm': 'millimeter', 'millimeters': 'millimeter',
        'km/h': 'kilometer/hour', 'mph': 'mile/hour',
        'kg/m³': 'kilogram/meter³',
        'm/s': 'meter/second', 'm/s²': 'meter/second²',

        # Grocery and cooking units
        'lb': 'pound', 'lbs': 'pound', 'pounds': 'pound',
        'oz': 'ounce', 'ounces': 'ounce',
        'pt': 'pint', 'pints': 'pint',
        'qt': 'quart', 'quarts': 'quart',
        'gal': 'gallon', 'gallons': 'gallon',
        'tsp': 'teaspoon', 'teaspoons': 'teaspoon',
        'tbsp': 'tablespoon', 'tablespoons': 'tablespoon',
        'cup': 'cup', 'cups': 'cup',
        'dozen': 'dozen', 'dozens': 'dozen',
    }

    # Common quantity keywords for context
    QUANTITY_KEYWORDS = {
        # Electrical
        'voltage': 'voltage', 'voltages': 'voltage',
        'current': 'current', 'currents': 'current',
        'power': 'power',
        'resistance': 'resistance', 'resistances': 'resistance',
        'capacitance': 'capacitance',
        'inductance': 'inductance',
        'frequency': 'frequency', 'frequencies': 'frequency',
        'charge': 'charge',
        'impedance': 'impedance',
        'conductance': 'conductance',
        'magnetic flux': 'magnetic_flux',
        'magnetic field': 'magnetic_field',

        # Physical
        'length': 'length', 'distance': 'distance', 'height': 'height', 'width': 'width',
        'weight': 'weight', 'mass': 'mass',
        'time': 'time', 'duration': 'duration',
        'temperature': 'temperature',
        'volume': 'volume',
        'area': 'area',
        'speed': 'speed', 'velocity': 'velocity',
        'acceleration': 'acceleration',
        'force': 'force',
        'pressure': 'pressure',
        'energy': 'energy',

        # General
        'value': 'value', 'measurement': 'measurement', 'reading': 'reading',
        'amount': 'amount', 'quantity': 'quantity',
    }

    # SI prefixes for unit recognition
    SI_PREFIXES = {
        'y': 'yocto', 'z': 'zepto', 'a': 'atto', 'f': 'femto',
        'p': 'pico', 'n': 'nano', 'µ': 'micro', 'μ': 'micro',
        'm': 'milli', 'c': 'centi', 'd': 'deci',
        'da': 'deca', 'h': 'hecto', 'k': 'kilo',
        'M': 'mega', 'G': 'giga', 'T': 'tera',
        'P': 'peta', 'E': 'exa', 'Z': 'zetta', 'Y': 'yotta'
    }

    def __init__(self) -> None:
        self.quantity_pattern = self._build_quantity_pattern()

    def _build_quantity_pattern(self) -> re.Pattern:
        """Build a regex pattern to match quantities in text."""
        # Pattern to match numbers (including decimals and scientific notation)
        number_pattern = r'\d+\.?\d*(?:[eE][-+]?\d+)?'

        # Pattern to match units (allow for prefixes, compound units, and special symbols)
        # Include common special characters like Ω, °, µ, etc.
        # Use case-insensitive matching and allow for various symbols
        unit_pattern = r'[a-zA-ZμµΩ°²³/%\-]+'

        # Combine into quantity pattern (use raw string for regex)
        quantity_pattern = rf'({number_pattern})\s*({unit_pattern})'

        return re.compile(quantity_pattern, re.IGNORECASE)

    def extract_quantities(self, text: str) -> list[dict[str, Any]]:
        """
        Extract quantities from text and return structured data.

        Args:
            text: The input text to parse

        Returns:
            List of dictionaries with extracted quantity information

        Example:
            >>> parser = QuantityParser()
            >>> parser.extract_quantities("The voltage is 230 V and current is 10 A")
            [
                {
                    'object': 'voltage',
                    'value': 230.0,
                    'unit': 'volt',
                    'original_text': '230 V',
                    'quantity': Quantity(230.0, 'volt')
                },
                {
                    'object': 'current',
                    'value': 10.0,
                    'unit': 'ampere',
                    'original_text': '10 A',
                    'quantity': Quantity(10.0, 'ampere')
                }
            ]
        """
        quantities = []

        # Find all quantity matches in the text
        matches = self.quantity_pattern.finditer(text)

        for match in matches:
            value_str, unit_str = match.groups()
            original_text = match.group(0)

            try:
                # Clean and normalize the unit for Quantity creation
                clean_unit = self._normalize_unit(unit_str)

                # Try to create a Quantity object to validate
                value = float(value_str)
                quantity = Quantity(value, clean_unit)

                # Determine the object type based on context and original unit
                object_type = self._determine_object_type(text, match.start(), match.end(), unit_str)

                # Extract the item name being measured
                item_name = self._extract_item_name(text, match.start(), match.end())

                # For display, use the original unit (but we'll keep both)

                quantities.append({
                    'object': object_type,
                    'value': value,
                    'unit': clean_unit,
                    'original_text': original_text,
                    'quantity': quantity,
                    'start_pos': match.start(),
                    'end_pos': match.end(),
                    'item': item_name
                })

            except (ValueError, KeyError):
                # Skip quantities that can't be parsed
                continue

        return quantities

    def _normalize_unit(self, unit_str: str) -> str:
        """Normalize a unit string to its standard form."""
        unit_str = unit_str.lower().strip()

        # First, check if the full unit (with possible plural) is in our abbreviations
        if unit_str in self.UNIT_ABBREVIATIONS:
            return self.UNIT_ABBREVIATIONS[unit_str]

        # Remove plural 's' if present
        if unit_str.endswith('s') and len(unit_str) > 1:
            singular_unit = unit_str[:-1]
            if singular_unit in self.UNIT_ABBREVIATIONS:
                return self.UNIT_ABBREVIATIONS[singular_unit]

        # Handle special case for ohm symbol (Ω)
        if unit_str == 'ω' or unit_str == 'Ω':
            return 'ohm'

        # Handle SI prefixes - check for valid prefix + base unit combinations
        # Sort prefixes by length (longest first) to handle multi-character prefixes
        for prefix in sorted(self.SI_PREFIXES.keys(), key=len, reverse=True):
            if unit_str.startswith(prefix):
                base_unit = unit_str[len(prefix):]
                # Check if the base unit (with or without plural) is valid
                if base_unit in self.UNIT_ABBREVIATIONS:
                    # Return the full prefixed unit name (e.g., 'milliampere' for 'ma')
                    full_prefix = self.SI_PREFIXES[prefix]
                    return f"{full_prefix}{self.UNIT_ABBREVIATIONS[base_unit]}"
                elif base_unit.endswith('s') and base_unit[:-1] in self.UNIT_ABBREVIATIONS:
                    full_prefix = self.SI_PREFIXES[prefix]
                    return f"{full_prefix}{self.UNIT_ABBREVIATIONS[base_unit[:-1]]}"
                # Handle special case for kΩ -> kiloohm
                elif base_unit == 'ω' or base_unit == 'Ω':
                    full_prefix = self.SI_PREFIXES[prefix]
                    return f"{full_prefix}ohm"

        # Return as-is if we can't normalize (will be validated by Quantity constructor)
        return unit_str

    def _determine_object_type(self, text: str, quantity_start: int, quantity_end: int, unit_str: str) -> str:
        """Determine the type of quantity based on surrounding context and unit."""
        # Look for keywords before and after the quantity
        text_before = text[:quantity_start].lower()
        text_after = text[quantity_end:].lower()

        # Find the closest keyword to the quantity
        closest_keyword = None
        closest_distance = float('inf')

        for keyword, object_type in self.QUANTITY_KEYWORDS.items():
            # Check in text before
            pos_before = text_before.rfind(keyword)
            if pos_before != -1:
                distance = quantity_start - (pos_before + len(keyword))
                if distance < closest_distance:
                    closest_distance = distance
                    closest_keyword = keyword
                    closest_object_type = object_type

            # Check in text after
            pos_after = text_after.find(keyword)
            if pos_after != -1:
                distance = pos_after
                if distance < closest_distance:
                    closest_distance = distance
                    closest_keyword = keyword
                    closest_object_type = object_type

        if closest_keyword:
            return closest_object_type

        # Default to generic types based on unit
        unit_to_object = {
            'volt': 'voltage', 'v': 'voltage',
            'ampere': 'current', 'a': 'current',
            'watt': 'power', 'w': 'power',
            'ohm': 'resistance', 'ω': 'resistance',
            'farad': 'capacitance', 'f': 'capacitance',
            'henry': 'inductance', 'h': 'inductance',
            'hertz': 'frequency', 'hz': 'frequency',
            'coulomb': 'charge', 'c': 'charge',
            'siemens': 'conductance', 's': 'conductance',
            'weber': 'magnetic_flux', 'wb': 'magnetic_flux',
            'tesla': 'magnetic_field', 't': 'magnetic_field',
            'meter': 'length', 'm': 'length',
            'kilogram': 'mass', 'kg': 'mass', 'gram': 'mass', 'g': 'mass',
            'seconds': 'time',
            'kelvin': 'temperature', 'k': 'temperature',
            'mole': 'amount', 'mol': 'amount',
            'candela': 'luminosity', 'cd': 'luminosity',
            'liter': 'volume', 'l': 'volume'
        }

        # Get the base unit (without prefix)
        base_unit = unit_str
        for prefix in self.SI_PREFIXES.keys():
            if unit_str.startswith(prefix):
                base_unit = unit_str[len(prefix):]
                break

        return unit_to_object.get(base_unit, 'measurement')

    def _extract_item_name(self, text: str, quantity_start: int, quantity_end: int) -> str:
        """Extract the item name being measured from the surrounding context."""
        text_after = text[quantity_end:].strip()

        # Look for common prepositions that often precede the item name
        prepositions = ['of', 'for', 'with', 'in', 'on', 'at', 'by']

        # Find the first preposition after the quantity
        for prep in prepositions:
            prep_pos = text_after.lower().find(prep + ' ')
            if prep_pos != -1:
                # Extract text after the preposition
                item_start = prep_pos + len(prep) + 1
                item_text = text_after[item_start:]

                # Extract until we hit punctuation or conjunction
                # Use word-based extraction instead of character-based
                words: list[str] = []
                current_word: list[str] = []
                for i, char in enumerate(item_text):
                    if char.isspace():
                        if current_word:
                            words.append(''.join(current_word))
                            current_word = []
                        # Check if next non-space character starts a conjunction
                        remaining_text = item_text[i:].lstrip()
                        if remaining_text.startswith('and ') or remaining_text.startswith('or '):
                            break
                        elif remaining_text and remaining_text[0] in [',', ';']:
                            break
                    elif char in [',', ';']:
                        if current_word:
                            words.append(''.join(current_word))
                            current_word = []
                        break
                    else:
                        current_word.append(char)

                # Add any remaining word only if we didn't break on punctuation/conjunction
                if current_word:
                    words.append(''.join(current_word))

                # Clean up the item name
                item_str = ' '.join(words).strip()
                # Remove trailing punctuation
                if item_str and item_str[-1] in [',', '.', ';']:
                    item_str = item_str[:-1].strip()
                return item_str

        # If no preposition found, try to extract noun phrases after the quantity
        # Use word-based extraction
        words2: list[str] = []
        current_word2: list[str] = []
        for i, char in enumerate(text_after):
            if char.isspace():
                if current_word2:
                    words2.append(''.join(current_word2))
                    current_word2 = []
                # Check if next non-space character starts a conjunction
                remaining_text = text_after[i:].lstrip()
                if remaining_text.startswith('and ') or remaining_text.startswith('or '):
                    break
                elif remaining_text and remaining_text[0] in [',', ';']:
                    break
            elif char in [',', ';']:
                if current_word2:
                    words2.append(''.join(current_word2))
                    current_word2 = []
                break
            else:
                current_word2.append(char)

        # Add any remaining word only if we didn't break on punctuation/conjunction
        if current_word2:
            words2.append(''.join(current_word2))

        # Clean up the item name
        item_str = ' '.join(words2).strip()
        # Remove trailing punctuation
        if item_str and item_str[-1] in [',', '.', ';']:
            item_str = item_str[:-1].strip()
        return item_str

    def extract_to_json(self, text: str) -> str:
        """
        Extract quantities and return as JSON string.

        Args:
            text: The input text to parse

        Returns:
            JSON string with extracted quantities
        """
        import json
        quantities = self.extract_quantities(text)

        # Convert Quantity objects to dict for JSON serialization
        json_data = []
        for q in quantities:
            quantity_dict = {
                'object': q['object'],
                'value': q['value'],
                'unit': q['unit'],
                'original_text': q['original_text']
            }
            # Include item name if available
            if 'item' in q:
                quantity_dict['item'] = q['item']
            json_data.append(quantity_dict)

        return json.dumps(json_data, indent=2)

    def extract_to_list(self, text: str) -> list[dict[str, Any]]:
        """
        Extract quantities and return as a list of dictionaries.

        Args:
            text: The input text to parse

        Returns:
            List of dictionaries with quantity information
        """
        quantities = self.extract_quantities(text)
        result = []
        for q in quantities:
            quantity_dict = {
                'object': q['object'],
                'value': q['value'],
                'unit': q['unit'],
                'original_text': q['original_text']
            }
            # Include item name if available
            if 'item' in q:
                quantity_dict['item'] = q['item']
            result.append(quantity_dict)
        return result


def parse_quantities(text: str, format: str = 'list') -> Any:
    """
    Convenience function to parse quantities from text.

    Args:
        text: The input text to parse
        format: Output format ('list', 'json', or 'objects')

    Returns:
        Parsed quantities in the requested format
    """
    parser = QuantityParser()

    if format == 'json':
        return parser.extract_to_json(text)
    elif format == 'list':
        return parser.extract_to_list(text)
    elif format == 'objects':
        return parser.extract_quantities(text)
    else:
        raise ValueError(f"Unknown format: {format}. Choose 'list', 'json', or 'objects'")
