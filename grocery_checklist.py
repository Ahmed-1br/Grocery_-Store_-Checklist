"""
Grocery Store Checklist
A Python program that helps people manage
their grocery shopping list"""

def main():
    grocery_list = []
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
            print("You selected Mark item as purchased.")
        elif choice == "4":
            print("You selected Remove grocery item.")
        elif choice == "5":
            print("You selected View shopping summary.")
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()