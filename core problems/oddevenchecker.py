def number():
    num = int(input("Enter your Number"))
    if num%2 == 0:
        print(num, "Number is ever")
    else:
        print(num, "Number is Odd")
    return
number()