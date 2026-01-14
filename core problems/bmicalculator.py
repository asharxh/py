print(" BMI Calculator\n")
print("This program calculates your Body Mass Index (BMI) and shows your health category.\n")

while True:
    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))

        if weight <= 0 or height <= 0:
            print(" Weight and height must be positive numbers.\n")
            continue

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Health Category: {category}\n")

        again = input("Do you want to calculate again? (yes/no): ").lower()
        if again != "yes":
            print(" Stay healthy! Goodbye!")
            break

    except ValueError:
        print(" Invalid input. Please enter numeric values.\n")
