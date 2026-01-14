print("== TRIANGLE TYPE FINDER ==")

a = float(input("enter side a: "))
b = float(input("Enter side b: "))
c = float(input("enter side c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("This is an Equilateral Triangle.")
    elif a == b or b == c or a == c:
        print("This is an Isosceles Triangle.")
    else:
        print("This is a Scalene Triangle.")
else:
    print("Invalid Triangle! The sides do not satisfy the triangle inequality rule.")
