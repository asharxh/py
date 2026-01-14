def check_substring_existence():
    main_string = input("Enter the main string: ")
    sub_string = input("Enter the substring to check: ")
    if sub_string in main_string:
        print("Substring exists in the main string.")
    else:
        print("Substring does not exist in the main string.")

check_substring_existence()
