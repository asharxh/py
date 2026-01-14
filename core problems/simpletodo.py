
todo = []
while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
    
        choice = int(input("Please Enter your choice 1-4: "))

        if choice == 1:
            task = input("Enter your task name")
            todo.append(task)
            print("Task Added")
        elif choice == 2:
            if not todo:
                print("No Tasks Available")
            else:
                print("\n Your Tasks")
                for i, task in enumerate(todo, start=1):
                    print(i, "-", task)
        elif choice == 3:
            if not todo:
                print("No Tasks to delete")
            else:
                num = int(input("Enter task number to delete: "))
                if 1<= num <= len(todo):
                    removed = todo.pop(num-1)
                    print(f"Task {removed} deleted. ")
                else:
                    print("Invalid task number. ")
        elif choice == 4:
            print("Goodbye")
            break
        else:
            print("inValid input, try again")
