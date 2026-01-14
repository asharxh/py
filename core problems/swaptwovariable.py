def swap_arithmetic():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Before swapping: a =", a, "b =", b)
    a = a + b
    b = a - b
    a = a - b
    print("After swapping: a =", a, "b =", b)

def swap_tuple_unpacking():
    a = input("Enter the first value: ")
    b = input("Enter the second value: ")
    print("Before swapping: a =", a, "b =", b)
    a, b = b, a
    print("After swapping: a =", a, "b =", b)

def swap_temp_variable():
    a = input("Enter the first value: ")
    b = input("Enter the second value: ")
    print("Before swapping: a =", a, "b =", b)
    temp = a
    a = b
    b = temp
    print("After swapping: a =", a, "b =", b)

while True:
    print("\nSelect a swap method:")
    print("1. Swap using arithmetic (numbers only)")
    print("2. Swap using tuple unpacking (any type)")
    print("3. Swap using temporary variable (any type)")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        swap_arithmetic()
    elif choice == "2":
        swap_tuple_unpacking()
    elif choice == "3":
        swap_temp_variable()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please enter 1-4.")