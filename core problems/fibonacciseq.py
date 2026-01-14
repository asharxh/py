def fibonacci_sequence():
    number_input = input("Enter how many terms you want: ")
    number = int(number_input)
    if number <= 0:
        print("Please enter a positive integer")
    elif number == 1:
        print("Fibonacci sequence:")
        print(0)
    else:
        first = 0
        second = 1
        count = 0
        print("Fibonacci sequence:")
        while count < number:
            print(first)
            next_value = first + second
            first = second
            second = next_value
            count = count + 1

fibonacci_sequence()