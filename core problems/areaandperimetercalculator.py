import math

print("Area and Perimeter Cal ")

shape = input("Which Shape u wanna Calculate [Square] [Rectangle] [Circle]: ").lower().strip()

if shape == "square":
    side = input("Enter the side of square: ")
    perimeter = 4 * side
    area = side * side
    print(f"Square → Area: {area}, Perimeter: {perimeter}")
    
elif shape == "rechtangle":
    length = input("Enter the lenght of rechtangle: ")
    width = input("Enter the width of rectangle: ")
    area = length * width
    perimeter = 2 * (length + width)
    print(f"Rectangle → Area: {area}, Perimeter: {perimeter}")
    
elif shape == "circle":
    radius = float(input("Enter the radius: "))
    area = math.pi * (radius ** 2)
    perimeter = 2 * math.pi * radius
    print(f"Circle → Area: {area:.2f}, Circumference: {perimeter:.2f}")
    
else :
    print("Please Enter Valid Input! Try Again")
    

