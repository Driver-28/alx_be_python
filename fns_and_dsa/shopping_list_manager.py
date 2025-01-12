def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            if item:
                shopping_list.append(item)
                print(f'"{item}" added to the shopping list.')
            else:
                print("Item name cannot be empty.")
            pass
        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f'"{item}" removed from the shopping list.')
            else:
                print(f'"{item}" not found in the shopping list.')
            pass
        elif choice == '3':
            if shopping_list:
                print("\nCurrent shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("Shopping list is empty.")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()