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
            new = input("Insert the item you want to add: ")
            shopping_list.append(new)
        elif choice == '2':
            new = input("Insert the item you want to remove: ")
            if new in shopping_list:
                shopping_list.remove(new)
            else:
                print("Itrm is not in the list")
        elif choice == '3':
            for i in range(len(shopping_list)):
                print(shopping_list[i])
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()