def check_prime():
    number_input = input("Enter a number: ")
    number = int(number_input)
    if number < 2:
        print("Not Prime")
    else:
        divisor = 2
        is_prime = True
        while divisor < number:
            if number % divisor == 0:
                is_prime = False
                break
            else:
                divisor = divisor + 1
        if is_prime == True:
            print("Prime")
        else:
            print("Not Prime")

check_prime()