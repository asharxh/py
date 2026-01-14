print("PHONEBOOK SYSTEMM")

phonebook = {}

while True:
    print("\n--- PHONE ---")
    print("1. Add New Contact")
    print("2. Search Contact by Name")
    print("3. Delete a Contact")
    print("4. View All Contacts")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")
    if choice == '1':
        name = input("Enter contact name: ").strip().title()
        number = input("Enter phone number: ").strip()
        if not number.isdigit() or len(number) != 10:
            print("Invalid phone number! Must be 10 digits.")
        else:
            phonebook[name] = number
            print(f" Contact '{name}' added successfully.")
    elif choice == '2':
        name = input("Enter name to search: ").strip().title()
        if name in phonebook:
            print(f"{name}: {phonebook[name]}")
        else:
            print("Contact not found.")
    elif choice == '3':
        name = input("Enter name to delete: ").strip().title()
        if name in phonebook:
            del phonebook[name]
            print(f"Contact '{name}' deleted.")
        else:
            print(" No such contact found.")
    elif choice == '4':
        if phonebook:
            print("\n All Contacts:")
            for name, number in sorted(phonebook.items()):
                print(f"- {name}: {number}")
        else:
            print("No contacts found.")
    elif choice == '5':
        print("Exiting Phonebook!")
        break
    else:
        print("Invalid option! Please choose between 1 and 5.")