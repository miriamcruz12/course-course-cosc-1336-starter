from src.homework.g_lists_and_tuples.lists import get_lowest_list_value, get_highest_list_value

def main():
    while True:
        print("\nMenu:")
        print("1 - Show the list low/high values")
        print("2 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            numbers = []
            while True:
                try:
                    value = int(input("Enter a list value: "))
                    numbers.append(value)
                    if len(numbers) >= 3:
                        cont = input("Do you want to enter another value? (yes/no): ").lower()
                        if cont != "yes":
                            break
                except ValueError:
                    print("Please enter a valid integer.")

            if numbers:
                print("Lowest value:", get_lowest_list_value(numbers))
                print("Highest value:", get_highest_list_value(numbers))
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.") 

__name__ == "__main__"
main() 