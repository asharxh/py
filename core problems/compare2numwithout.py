a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
diff = a - b
if diff == 0:
    print("Both numbers are equal.")
elif diff // abs(diff) == 1:
    print(a, "is greater.")
else:
    print(b, "is greater.")