
print("Multiplication Table Generator")
try:
    number = int(input("Enter a number: "))
    limit = int(input("Enter the range limit: "))

    print(f"\nMultiplication Table for {number}")
    print("------------------------------")

    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")

except ValueError:
    print("Please enter valid integers only!")

print("\nTable generation completed.")