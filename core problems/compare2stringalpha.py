def compare_strings_alphabetically():
    first = input("Enter first string: ")
    second = input("Enter second string: ")
    if first == second:
        print("Both strings are equal.")
    elif first < second:
        print("First string comes before second string alphabetically.")
    else:
        print("Second string comes before first string alphabetically.")

compare_strings_alphabetically()