user_string = input("Enter a string: ")

if len(user_string) == 0:
    print("Error: String is empty!")
else:
    first_char = user_string[0]
    last_char = user_string[len(user_string) - 1]

    print("First character:", first_char)
    print("Last character:", last_char)