
contacts = {}
while True:
    print("1. Add contact")
    print("2. View contact")
    print("3. search contact")
    print("4. delete contact")
    print("5. Exit")
    
    choice = input("please enter ur choice 1-5: ")
    
    
    if choice=="1":
        name = input("Enter ur name: ")
        phone = input("Enter ur phone number: ")
        contacts[name] = {"phone" : phone}
        print("Contact Added! ")
    
    elif choice =="2":
        if not contacts:
            print("No contacts Saved.: ")
        else:
            print("\n--- All Contact ---")
            for name, info in contacts.items():
                print(f"Name : {name}, Phone : {info['phone']}")
                
    elif choice == "3":
        search = input("Enter the name to Search: ")
        if search in contacts:
            info = contacts[search]
            print(f"Name : {search}, Phone: {info['phone']}")
        else:
            print("Contact not Found")
            
    elif choice =="4":
        delete_name = input("Enter name to delete: ")
        if delete_name in contacts:
            del contacts[delete_name]
            print("Deleted")
        else:
            print("Contact not Found")
        
    elif choice=="5":
        print("Goodbye")
        break
    else:
        print("Invalid input, try again")
