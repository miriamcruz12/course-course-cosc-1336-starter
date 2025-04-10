from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

def main():
    inventory = {}
    while True:
        print("\nInventory Menu")
        print("1-Add or Update Item")
        print("2-Delete Item")
        print("3-Exit")
        choice = input("Enter your choice: ")

        if choice == "1": 
            name = input("Enter widget name: ")
            qty = int(input("Enter quantity: "))
            add_inventory(inventory, name, qty)
            print(f"Updated Inventory: {inventory}")

        elif choice == "2":
            name = input("Enter widget name to delete: ")
            result = remove_inventory_widget(inventory, name)
            print(result)

        elif choice == "3": 
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main() 