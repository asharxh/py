def count_word():
    sentence = input("Enter a sentence: ")
    word_to_count = input("Enter the word to count: ")
    sentence_lower = sentence.lower()
    word_lower = word_to_count.lower()
    words = sentence_lower.split()
    count = 0
    for w in words:
        if w == word_lower:
            count += 1
    print(f"The word '{word_to_count}' appears {count} time(s).")

def remove_duplicates():
    numbers_input = input("Enter numbers separated by spaces: ")
    numbers_str = numbers_input.split()
    numbers = []
    for num in numbers_str:
        numbers.append(int(num))
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    print("Original list:", numbers)
    print("List after removing duplicates:", unique_numbers)

def capitalize_words():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    capitalized_words = []
    for word in words:
        if len(word) > 0:
            capitalized_word = word[0].upper() + word[1:]
            capitalized_words.append(capitalized_word)
        else:
            capitalized_words.append(word)
    capitalized_sentence = " ".join(capitalized_words)
    print("Capitalized sentence:", capitalized_sentence)

def first_last_character():
    user_string = input("Enter a string: ")
    if len(user_string) == 0:
        print("Error: String is empty!")
    else:
        first_char = user_string[0]
        last_char = user_string[len(user_string) - 1]
        print("First character:", first_char)
        print("Last character:", last_char)

def swap_variables():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Before swapping: a =", a, "b =", b)
    a = a + b
    b = a - b
    a = a - b
    print("After swapping: a =", a, "b =", b)

while True:
    print("\nSelect a project to run:")
    print("1. Count specific word in a sentence")
    print("2. Remove duplicates from a list")
    print("3. Capitalize every word in a sentence")
    print("4. Find first & last character of a string")
    print("5. Swap two variables without temp variable")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        count_word()
    elif choice == "2":
        remove_duplicates()
    elif choice == "3":
        capitalize_words()
    elif choice == "4":
        first_last_character()
    elif choice == "5":
        swap_variables()
    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 6.")