#!/usr/bin/env python
"""
Example demonstrating natural language parsing for grocery shopping.

This example shows how someone can describe groceries in everyday sentences
and have the package parse and print the corresponding quantities.
"""

from pyquantity.parser import QuantityParser


def main() -> None:
    print("Grocery Shopping Example with Natural Language Parsing")
    print("=" * 60)

    # Create a parser instance
    parser = QuantityParser()

    # Example 1: Simple grocery list in natural language
    print("\n1. Simple Grocery List:")
    grocery_text = "I bought 2 liters of milk, 500 grams of flour, and 1 kilogram of apples."
    print(f"Input: {grocery_text}")

    quantities = parser.extract_quantities(grocery_text)
    print("\nParsed quantities:")
    for i, qty in enumerate(quantities, 1):
        item_name = qty.get('item', 'unknown')
        print(f"  {i}. {item_name}: {qty['value']} {qty['unit']}")

    # Example 2: More complex grocery scenario
    print("\n2. Complex Grocery Scenario:")
    complex_text = "At the store, I purchased 3 bottles of water (each 1.5 liters), " \
                  "a 250-gram package of butter, and 2 kilograms of potatoes."
    print(f"Input: {complex_text}")

    quantities = parser.extract_quantities(complex_text)
    print("\nParsed quantities:")
    for i, qty in enumerate(quantities, 1):
        item_name = qty.get('item', 'unknown')
        print(f"  {i}. {item_name}: {qty['value']} {qty['unit']}")

    # Example 3: Conversational grocery description
    print("\n3. Conversational Grocery Description:")
    conversation_text = "I told the cook I bought 1.5 kg of sugar, 500 ml of cream, " \
                       "and a dozen eggs for the recipe."
    print(f"Input: {conversation_text}")

    quantities = parser.extract_quantities(conversation_text)
    print("\nParsed quantities:")
    for i, qty in enumerate(quantities, 1):
        item_name = qty.get('item', 'unknown')
        print(f"  {i}. {item_name}: {qty['value']} {qty['unit']}")

    # Example 4: Mixed units and quantities
    print("\n4. Mixed Units and Quantities:")
    mixed_text = "The shopping list includes: 2.5 lbs of chicken, 1 pint of berries, " \
                "300 grams of cheese, and 1.2 liters of orange juice."
    print(f"Input: {mixed_text}")

    quantities = parser.extract_quantities(mixed_text)
    print("\nParsed quantities:")
    for i, qty in enumerate(quantities, 1):
        item_name = qty.get('item', 'unknown')
        print(f"  {i}. {item_name}: {qty['value']} {qty['unit']}")

    # Example 5: Real-world scenario with person telling cook
    print("\n5. Person Telling Cook What Was Bought:")
    cook_text = "Hey chef, I got 3 kilograms of tomatoes, 1 kilogram of onions, " \
               "500 grams of garlic, 2 liters of olive oil, and 1.5 kilograms of pasta " \
               "for tonight's dinner service."
    print(f"Input: {cook_text}")

    quantities = parser.extract_quantities(cook_text)
    print("\nParsed groceries:")
    for i, qty in enumerate(quantities, 1):
        item_name = qty.get('item', 'unknown')
        print(f"  {i}. {item_name}: {qty['value']} {qty['unit']}")

    print("\n" + "=" * 60)
    print("Grocery shopping example completed!")

if __name__ == "__main__":
    main()
