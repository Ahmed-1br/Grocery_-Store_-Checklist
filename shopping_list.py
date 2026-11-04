"""
Program: Grocery Store Checklist
Author: Ahmed Ibrahim
Date: 11/04/2026
Purpose: Manage grocery items and their purchased status.
Resources: Original Project 1 and Python Crash Course book
"""

class ShoppingList:
    """Manage a grocery list and track purchased items."""

    def __init__(self):
        """Create empty grocery and purchased lists."""
        self.items = []
        self.purchased_items = []

    def add_item(self, name):
        """Add a nonempty, unique item and return its cleaned name."""
        name = name.strip()

        if not name:
            raise ValueError("Please enter an item name.")

        if name.lower() in [item.lower() for item in self.items]:
            raise ValueError("This item is already on your grocery list.")

        self.items.append(name)
        return name

    def get_item(self, number):
        """Return an item using its one-based menu number."""
        if not 1 <= number <= len(self.items):
            raise ValueError("Invalid item number.")

        return self.items[number - 1]

    def mark_purchased(self, number):
        """Mark an item as purchased and return its name."""
        item = self.get_item(number)

        if item in self.purchased_items:
            raise ValueError("This item is already purchased.")

        self.purchased_items.append(item)
        return item

    def remove_item(self, number):
        """Remove an item and its purchased status."""
        item = self.get_item(number)
        self.items.remove(item)

        if item in self.purchased_items:
            self.purchased_items.remove(item)

        return item

    def get_summary(self):
        """Return total, purchased, and remaining items counts."""
        total = len(self.items)
        purchased = len(self.purchased_items)

        return {
            "total": total,
            "purchased": purchased,
            "remaining": total - purchased
        }