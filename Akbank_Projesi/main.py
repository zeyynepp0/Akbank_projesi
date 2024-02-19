from library import Library

lib = Library()

while True:
    print("****MENU****")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("""4) Exit the program by pressing "q" or "Q" """)
    choice = input("Please enter your choice: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice.lower() == "q":
        print("The program has been executed")
        break
    else:
        print("Invalid answer!!!Please try again.")
