def sort_three_numbers():
    first_input = input("Enter first number: ")
    second_input = input("Enter second number: ")
    third_input = input("Enter third number: ")
    first = int(first_input)
    second = int(second_input)
    third = int(third_input)
    if first <= second and first <= third:
        if second <= third:
            print("Sorted order:", first, second, third)
        else:
            print("Sorted order:", first, third, second)
    elif second <= first and second <= third:
        if first <= third:
            print("Sorted order:", second, first, third)
        else:
            print("Sorted order:", second, third, first)
    else:
        if first <= second:
            print("Sorted order:", third, first, second)
        else:
            print("Sorted order:", third, second, first)

sort_three_numbers()