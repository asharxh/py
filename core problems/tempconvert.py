def tempchecker():
    print("One for Celsius to Fahrenheit")
    print("Two for Fahrenheit to Celsius")
    print("Three for Celsius to Kelvin")
    print("Four for Kelvin to Celsius")
    choice = int(input("Enter ur choice (1-4)"))
    temp = float(input("Enter the temprature Value: "))
    if choice == 1:
        result = (temp*9/5)+32
        print(result)
    elif choice == 2:
        result = (temp-32)*5/9
        print(result)
    elif choice == 3:
        result = temp + 273.15
        print(result)
    elif choice== 4:
        result = temp - 273.15
        print(result)
    else:
        print("Enter Valid Letter")

tempchecker()
