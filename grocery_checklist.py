"""
Grocery Store Checklist
A Python program that helps people manage
their grocery shopping list"""

def main():
    grocery_list = []
    purchased_items = []
    """Displays the grocery menu and process people's choices."""
    while True:
        print("---------------------------")
        print("Grocery Store Checklist")
        print("---------------------------")
        print("Welcome to your grocery checklist!")
        print("\nMAIN MENU")
        print("1. Add grocery item")
        print("2. View grocery list")
        print("3. Mark item as purchased")
        print("4. Remove grocery item")
        print("5. View shopping summary")
        print("6. Exit")

        choice = input("\nChoose an option from the menu (1-6): ")
        if choice == "1":
            item = input("Enter the grocery item to add: ")
            if item:
                grocery_list.append(item)
                print(f"Added {item} to the grocery list.")
            else:
                print("No item entered.")
        elif choice == "2":
            if grocery_list:
                print("\nYOUR GROCERY LIST")

                for number, item in enumerate(grocery_list, start=1):
                    print(f"{number}. {item}")
            else:
                print("Your grocery list is empty.")
        elif choice == "3":
            if grocery_list:
                print("\nGROCERY ITEMS")

                for number, item in enumerate(grocery_list, start=1):
                    print(f"{number}. {item}")

                selection = input("Enter item number purchased: ")

                if selection.isdigit():
                    index = int(selection) - 1

                    if 0 <= index < len(grocery_list):
                        item = grocery_list[index]

                        if item not in purchased_items:
                            purchased_items.append(item)
                            print(f"{item} marked as purchased!")
                        else:
                            print("This item is already purchased.")
                    else:
                        print("Invalid item number.")
                else:
                    print("Please enter a valid number.")
            else:
                print("Your grocery list is empty.")
        elif choice == "4":
            if grocery_list:
                print("\nREMOVE GROCERY ITEM")

                for number, item in enumerate(grocery_list, start=1):
                    print(f"{number}. {item}")

                selection = input("Enter item number to remove: ")

                if selection.isdigit():
                    index = int(selection) - 1

                    if 0 <= index < len(grocery_list):
                        item = grocery_list.pop(index)
                        if item in purchased_items:
                            purchased_items.remove(item)
                        print(f"Removed {item} from the grocery list.")
                    else:
                        print("Invalid item number.")
                else:
                    print("Please enter a valid number.")
            else:
                print("Your grocery list is empty.")
        elif choice == "5":
            if grocery_list:
                print("\nSHOPPING SUMMARY")

                for number, item in enumerate(grocery_list, start=1):
                    status = "Purchased" if item in purchased_items else "Not purchased"
                    print(f"{number}. {item} - {status}")

                total_items = len(grocery_list)
                purchased_count = sum(
                    1 for item in grocery_list
                    if item in purchased_items
                    )
                remaining = total_items - purchased_count

                print(f"Total items: {total_items}")
                print(f"Purchased: {purchased_count}")
                print(f"Remaining: {remaining}")
            else:
                print("Your grocery list is empty.")
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()