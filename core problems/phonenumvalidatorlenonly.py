def phone_number_validator():
    number = input("Enter phone number: ")
    if len(number) == 10:
        print("Valid phone number.")
    else:
        print("Invalid phone number. It must contain exactly 10 digits.")

phone_number_validator()