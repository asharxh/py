import os

def load_books(filename="books.txt"):
    books = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 4:
                    title, author, year, status = parts
                    books.append({
                        "title": title,
                        "author": author,
                        "year": int(year),
                        "status": status
                    })
    return books

def save_books(books, filename="books.txt"):
    with open(filename, "w") as f:
        for book in books:
            f.write(f"{book['title']}|{book['author']}|{book['year']}|{book['status']}\n")

def display_book(book, index):
    print(f"{index+1}. '{book['title']}' by {book['author']} ({book['year']}) - {book['status']}")

def favorite_books_collection():
    books = load_books()
    
    while True:
        print("\n--- Favorite Books Collection ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. View Collection")
        print("4. Search Book")
        print("5. Sort Collection")
        print("6. Mark as Read/Unread")
        print("7. View Statistics")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year_input = input("Enter year of publication: ")
            if not year_input.isdigit():
                print("Invalid year.")
                continue
            year = int(year_input)
            status = "Unread"
            books.append({"title": title, "author": author, "year": year, "status": status})
            save_books(books)
            print(f"Added '{title}' by {author} to your collection.")

        elif choice == "2":
            if len(books) == 0:
                print("Collection is empty.")
                continue
            for idx, book in enumerate(books):
                display_book(book, idx)
            remove_input = input("Enter book number to remove: ")
            if not remove_input.isdigit() or int(remove_input) < 1 or int(remove_input) > len(books):
                print("Invalid input.")
                continue
            removed_book = books.pop(int(remove_input)-1)
            save_books(books)
            print(f"Removed '{removed_book['title']}' from your collection.")

        elif choice == "3":
            if len(books) == 0:
                print("Collection is empty.")
            else:
                print("Your Book Collection:")
                for idx, book in enumerate(books):
                    display_book(book, idx)

        elif choice == "4":
            keyword = input("Enter book title or author to search: ").lower()
            found = False
            for idx, book in enumerate(books):
                if keyword in book['title'].lower() or keyword in book['author'].lower():
                    display_book(book, idx)
                    found = True
            if not found:
                print("No matching books found.")

        elif choice == "5":
            print("Sort by: 1. Title 2. Author 3. Year")
            sort_choice = input("Enter your choice: ")
            if sort_choice == "1":
                books.sort(key=lambda x: x['title'].lower())
            elif sort_choice == "2":
                books.sort(key=lambda x: x['author'].lower())
            elif sort_choice == "3":
                books.sort(key=lambda x: x['year'])
            else:
                print("Invalid choice.")
                continue
            print("Collection sorted successfully.")
            save_books(books)

        elif choice == "6":
            if len(books) == 0:
                print("Collection is empty.")
                continue
            for idx, book in enumerate(books):
                display_book(book, idx)
            mark_input = input("Enter book number to mark as Read/Unread: ")
            if not mark_input.isdigit() or int(mark_input) < 1 or int(mark_input) > len(books):
                print("Invalid input.")
                continue
            index = int(mark_input) - 1
            book = books[index]
            book['status'] = "Read" if book['status'] == "Unread" else "Unread"
            save_books(books)
            print(f"Book '{book['title']}' marked as {book['status']}.")

        elif choice == "7":
            total_books = len(books)
            read_books = sum(1 for book in books if book['status'] == "Read")
            unread_books = total_books - read_books
            print(f"Total books: {total_books}, Read: {read_books}, Unread: {unread_books}")

        elif choice == "8":
            print("Exiting Favorite Books Collection.")
            break

        else:
            print("Invalid choice. Please select again.")

favorite_books_collection()