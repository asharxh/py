def library_system():
    
    library = {
        "harry potter": {"author": "J.K", "available": True},
        "1984": {"author": "George Orwell", "available": True},
        "the hobbit": {"author": "J.R.R", "available": True},
        "game of thrones": {"author": "RR Martin", "available": True}
    }
    
    print("Welcome to Mini Library System")
    
    while True:
        print("\nOptions: [list] [borrow] [return] [exit]")
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == "list":
            print("\nBooks in Library: ")
            for title, details in library.items():
                status = "Available" if details["available"] else "Borrowed"
                print(f"- {title} by {details['author']} ({status})")
                
        elif choice == "borrow":
            book = input("Enter the book title to borrow: ").strip().lower()
            if book in library:
                if library[book]["available"]:
                    library[book]["available"] = False
                    print(f"You borrowed '{book}'.")
                else:
                    print(f"Sorry, '{book}' is already borrowed.")
            else:
                print("Book not found in the catalog.")
                
        elif choice == "return":
            book = input("Enter book title to return: ").strip().lower()
            if book in library:
                if not library[book]["available"]:
                    library[book]["available"] = True
                    print(f"You have returned '{book}'. Thank you!")
                else:
                    print(f"'{book}' was not borrowed.")
            else:
                print("Book not found in the catalog.")
                
        elif choice == "exit":
            print("Goodbye! Thanks for using the Library System.")
            break
        else:
            print("Invalid option! Please try again.")
            

if __name__ == "__main__":
    library_system()
