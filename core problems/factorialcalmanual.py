def factorial_calculator():
    number_input = input("Enter a number: ")
    number = int(number_input)
    if number < 0:
        print("Factorial not defined for negative numbers")
    elif number == 0 or number == 1:
        print("Factorial is: 1")
    else:
        result = 1
        counter = 1
        while counter <= number:
            result = result * counter
            counter = counter + 1
        print("Factorial is:", result)

factorial_calculator()