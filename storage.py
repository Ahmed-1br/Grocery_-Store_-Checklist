"""
Program: Grocery Store Checklist
Author: Ahmed Ibrahim
Date: 11/04/2026
Purpose: Save and load grocery lists and using JSON
Resources: Original Project 1 and Python Crash Course book
"""

import json
from pathlib import Path

from shopping_list import ShoppingList

DATA_FILE = Path(__file__).parent / "grocery_data.json"

def save_list(shopping_list, filename=DATA_FILE):
    """Save grocery items and purchased status to a JSON file."""
    data = {
        "items": shopping_list.items,
        "purchased_items": shopping_list.purchased_items
    }

    Path(filename).write_text(
        json.dumps(data, indent=4), encoding="utf-8"
    )

def load_list(filename=DATA_FILE):
    """Load a saved list or return an empty list if no file exists."""
    shopping_list = ShoppingList()

    try:
        contents = Path(filename).read_text(encoding="utf-8")
    except FileNotFoundError:
        return shopping_list

    try:
        data = json.loads(contents)

        if not isinstance(data, dict):
            raise ValueError("Saved data must be a dictionary.")

        items = data["items"]
        purchased_items = data["purchased_items"]

        if not isinstance(items, list) or not isinstance(purchased_items, list):
            raise ValueError("Saved items must be lists.")

        for item in items:
            if not isinstance(item, str):
                raise ValueError("Item names must be text.")
            shopping_list.add_item(item)

        for item in purchased_items:
            if not isinstance(item, str) or item not in shopping_list.items:
                raise ValueError("Invalid purchased item.")

            number = shopping_list.items.index(item) + 1
            shopping_list.mark_purchased(number)

    except (ValueError, KeyError) as error:
        raise ValueError(f"Unable to load saved grocery data: {error}") from error

    return shopping_list

       
           