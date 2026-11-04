"""
Program: Grocery Store Checklist Tests
Author: Ahmed Ibrahim
Date: 11/04/2026
Purpose: Test grocery management and JSON persistence.
Resources: Original Project 1, Python Crash Course book, and pytest
"""

import pytest

from shopping_list import ShoppingList
from storage import load_list, save_list

def test_add_items():
    """adding an item removes surrounding whitespace."""
    groceries = ShoppingList()
    assert groceries.add_item(" Milk ") == "Milk"
    assert groceries.items == ["Milk"]

def test_reject_duplicate():
    """Duplicate names are rejected regardless of capitalization."""
    groceries = ShoppingList()
    groceries.add_item("Milk")

    with pytest.raises(ValueError):
        groceries.add_item("milk")

    assert groceries.items == ["Milk"]

def test_reject_empty_item():
    """Blank item names are rejected."""
    groceries = ShoppingList()

    with pytest.raises(ValueError):
        groceries.add_item("   ")

def test_purchase_and_summary():
    """Purchased and remaining counts reflect item status."""
    groceries = ShoppingList()
    groceries.add_item("Milk")
    groceries.add_item("Eggs")
    groceries.mark_purchased(1)

    assert groceries.get_summary() == {
        "total": 2,
        "purchased": 1,
        "remaining": 1
    }

def test_remove_purchased_item():
    """Removing a purchased item also removes its purchased status."""
    groceries = ShoppingList()
    groceries.add_item("Milk")
    groceries.mark_purchased(1)
    groceries.remove_item(1)

    assert groceries.items == []
    assert groceries.purchased_items == []

def test_invalid_numnber():
    """An out-of-range item number is rejected."""
    groceries = ShoppingList()

    with pytest.raises(ValueError):
        groceries.mark_purchased(1)

def test_already_purchased():
    """An item cannot be marked purchased twice."""
    groceries = ShoppingList()
    groceries.add_item("Milk")
    groceries.mark_purchased(1)

    with pytest.raises(ValueError):
        groceries.mark_purchased(1)

    assert groceries.purchased_items == ["Milk"]

def test_save_and_load(tmp_path):
    """Saving and loading preserves items and purchased status."""
    filename = tmp_path / "groceries.json"
    groceries = ShoppingList()
    groceries.add_item("Milk")
    groceries.add_item("Eggs")
    groceries.mark_purchased(1)

    save_list(groceries, filename)
    restored = load_list(filename)

    assert restored.items == ["Milk", "Eggs"]
    assert restored.purchased_items == ["Milk"]

def test_missing_file(tmp_path):
    """A missing save file produces an empty shopping list."""
    groceries = load_list(tmp_path / "missing.json")

    assert groceries.items == []
    assert groceries.purchased_items == []

def test_invalid_json(tmp_path):
    """Malformed JSON is rejected."""
    filename = tmp_path / "invalid.json"
    filename.write_text("not valid json", encoding="utf-8")

    with pytest.raises(ValueError):
        load_list(filename)

def test_invalid_purchased_data(tmp_path):
    """Purchased items must exist in the grocery list."""
    filename = tmp_path / "invalid_items.json"
    filename.write_text(
        '{"items": ["Milk"], "purchased_items": ["Eggs"]}',
        encoding="utf-8"
    )

    with pytest.raises(ValueError):
        load_list(filename)


   
