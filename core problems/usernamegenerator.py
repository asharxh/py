import random

print("USERNAME GENERATOR")

while True:
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    print("\nChoose number type:")
    print("1. Enter your own number")
    print("2. Generate a random number (10–99)")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        number = input("Enter a number (e.g., 42): ")
    elif choice == '2':
        number = str(random.randint(10, 99))
    else:
        print("Invalid choice, using random number by default.")
        number = str(random.randint(10, 99))

    username1 = (first_name.lower() + last_name[:3].lower() + number)
    username2 = (first_name[0].lower() + "_" + last_name.lower() + number)
    username3 = (last_name.lower() + first_name[:2].lower() + number)

    print("\n Generated Usernames:")
    print(f"1️ {username1}")
    print(f"2️ {username2}")
    print(f"3️ {username3}")
    
    again = input("\nGenerate another username? (y/n): ").lower()
    if again != 'y':
        break
