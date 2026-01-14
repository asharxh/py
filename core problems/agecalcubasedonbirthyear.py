import datetime

birth_year = input("Enter ur birth Year: ")
#current_year = input("Enter current Year: ") ---- We can also take user input for current year
current_year = datetime.now().year

if birth_year > current_year:
    print("Invalid Input! try again")
else:
    age = birth_year - current_year

    print(f"Your age is {age} ")
