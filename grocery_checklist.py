"""
Program: Grocery Store Checklist
Author: Ahmed Ibrahim
Date: 11/04/2026 
Purpose: Display the menu and coordinate grocery list operations.
Resources: Original Project 1 and Python Crash Course book
"""

from storage import save_list, load_list

def display_items(shopping_list):
    """Display numbered grocery items and their purchased status."""
    if not shopping_list.items:
        print("Your grocery list is empty.")
        return

    for number, item in enumerate(shopping_list.items, start=1):
        status = (
            "Purchased"
            if item in shopping_list.purchased_items
            else "Not Purchased"
        )
        print(f"{number}. {item} - {status}")

def save_changes(shopping_list):
    """Attempt to save changes and report wheter saving succeeded."""
    try:
        save_list(shopping_list)
    except OSError as error:
        print(f"Changes are in memory, but could not be saved: {error}")
        return False

    print("Grocery list saved.")
    return True

def main():
    """Load the grocery list and process menu choices."""
    try:
        shopping_list = load_list()
    except (OSError, ValueError, UnicodeError) as error:
        print(f"Could not open saved grocery data: {error}")
        print(f"Fix or rename grocery_data.json, then run the program again.")
        return

    while True:
        print("\nGROCERY STORE CHECKLIST")
        print("1. Add grocery item")
        print("2. View grocery list")
        print("3. Mark item as purchased")
        print("4. Remove grocery item")
        print("5. View shopping summary")
        print("6. Save and exit")

        choice = input("Choose an option (1-6): ").strip()

        try:
            if choice == "1":
                name = input("Enter the grocery item to add: ")
                item = shopping_list.add_item(name)
                print(f"Added {item} to the grocery list.")
                save_changes(shopping_list)

            elif choice == "2":
                display_items(shopping_list)
            elif choice in ["3", "4"]:
                display_items(shopping_list)

                if not shopping_list.items:
                    continue

                number = int(input("Enter the item number: "))

                if choice == "3":
                    item = shopping_list.mark_purchased(number)
                    print(f"{item} marked as purchased!")
                else:
                    item = shopping_list.remove_item(number)
                    print(f"Removed {item} from the grocery list.")

                save_changes(shopping_list)

            elif choice == "5":
                display_items(shopping_list)
                summary = shopping_list.get_summary()
                print(f"Total items: {summary['total']}")
                print(f"Purchased: {summary['purchased']}")
                print(f"Remaining: {summary['remaining']}")

            elif choice == "6":
                if save_changes(shopping_list):
                    print("Goodbye!")
                    break

                print("Please resolve the saving problem and try again.")

            else:
                print("Invalid choice. Enter a number between 1 and 6.")

        except ValueError as error:
            print(f"Invalid input: {error}")

if __name__ == "__main__":
    main()
              