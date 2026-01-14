def compare_three_strings():
    first = input("Enter first string: ")
    second = input("Enter second string: ")
    third = input("Enter third string: ")
    if first == second and second == third:
        print("All three strings are equal.")
    elif first == second or second == third or first == third:
        print("Two strings are equal.")
    else:
        print("All three strings are different.")

compare_three_strings()