print(" Tip Calculator (Split Bill) \n")
print("Calculate how much each person should pay, including a tip.\n")

while True:
    try:
        bill = float(input("Enter the total bill amount: $"))
        people = int(input("How many people are splitting the bill? "))
        tip_percent = float(input("Enter tip percentage (e.g., 10, 15, 20): "))

        if bill <= 0 or people <= 0 or tip_percent < 0:
            print(" Please enter valid positive numbers.\n")
            continue

        tip_amount = (bill * tip_percent) / 100
        total_bill = bill + tip_amount
        each_person = total_bill / people

        print("\nBill Summary. ")
        print(f"Total Bill: ${bill:.2f}")
        print(f"Tip ({tip_percent}%): ${tip_amount:.2f}")
        print(f"Total with Tip: ${total_bill:.2f}")
        print(f"Each Person Pays: ${each_person:.2f}\n")


        again = input("Would you like to calculate another bill? (yes/no): ").lower()
        if again != "yes":
            print(" Thank you! Enjoy your meal!")
            break

    except ValueError:
        print("Invalid input. Please enter numbers only.\n")
