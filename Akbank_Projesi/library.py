class Library:
    def __init__(self, name="", author="", release_date="", page_number=""):  # constructor
        self.name = name
        self.author = author
        self.release_date = release_date
        self.page_number = page_number

    def __del__(self):  # destructor (destroy the object)
        return None

    def list_books(self):
        with open("books.txt", "r") as file:
            content = file.read().splitlines()

        # Ask the user for sorting options
        print("How would you like to sort the books?")
        print("1. Alphabetically by book name")
        print("2. Alphabetically by author")
        print("3. By release date (Oldest to newest)")
        print("4. By release date (Newest to oldest)")
        print("5. By page number ")
        sort_option = input("Enter your choice: ")

        # Sort books in desired order
        if sort_option == "1":
            sorted_content = sorted(content, key=lambda x: x.split(",")[0])
        elif sort_option == "2":
            sorted_content = sorted(content, key=lambda x: x.split(",")[1])
        elif sort_option == "3":
            sorted_content = sorted(content, key=lambda x: x.split(",")[2])
        elif sort_option == "4":
            sorted_content = sorted(content, key=lambda x: x.split(",")[2], reverse=True)
        elif sort_option == "5":
            sorted_content = sorted(content, key=lambda x: int(x.split(",")[3]))
        else:
            print("Invalid choice. Sorting alphabetically by book name.")
            sorted_content = sorted(content, key=lambda x: x.split(",")[0])

        # List sorted books
        for index, kitap in enumerate(sorted_content, start=1):
            name, author, release_date, page_number = kitap.strip().split(",")
            print(
                "Book {}. Name: {}, Author: {}".format(index, name, author))

    def remove_book(self):
        book_name = input("Enter the book name that you want to delete: ")
        book_name = book_name.title()
        try:
            with open("books.txt", "r") as file:
                lines = file.readlines()
            found = False  # checking if the book exists
            with open("books.txt", "w") as file:
                for line in lines:
                    if book_name in line:
                        found = True  # The book found in text file
                    else:
                        file.write(line)  # The book couldn't find , rewrite the line
            if found:
                print(f"{book_name} removed successfully.")
            else:
                print(f"The book '{book_name}' is not in the library. Operation failed.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("An error occurred:", str(e))

    def add_book(self):
        _name = input("Enter the book name: ")
        _name = _name.title()
        _author = input("Enter the book's author: ")
        _author = _author.title()
        _release_date = input("Enter the release date: ")
        _page_number = input("Enter the book's page number: ")
        with open("books.txt", "a+", encoding="utf-8") as content:
            content.write(f"{_name}, {_author}, {_release_date}, {_page_number}\n")
