students = []  

while True:
    print("\n--- Student Information System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":  
        sid = input("Enter ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        grade = input("Enter Grade: ")
        student = {"ID": sid, "Name": name, "Age": age, "Grade": grade}
        students.append(student)
        print("Student added successfully!")

    elif choice == "2":  
        if not students:
            print("No records found.")
        else:
            print("\n--- Student Records ---")
            for s in students:
                print(s)

    elif choice == "3":  
        search_id = input("Enter Student ID to search: ")
        found = False
        for s in students:
            if s["ID"] == search_id:
                print("Found:", s)
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "4": 
        update_id = input("Enter Student ID to update: ")
        for s in students:
            if s["ID"] == update_id:
                s["Name"] = input("Enter new Name: ")
                s["Age"] = input("Enter new Age: ")
                s["Grade"] = input("Enter new Grade: ")
                print("Student updated successfully!")
                break
        else:
            print("Student not found.")

    elif choice == "5": 
        delete_id = input("Enter Student ID to delete: ")
        for s in students:
            if s["ID"] == delete_id:
                students.remove(s)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found.")

    elif choice == "6":
        print("Exiting system. Goodbye!")
        break

    else:
        print("Invalid choice, try again.")