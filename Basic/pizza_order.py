print("🍕 Welcome to Python Pizza!")

# Ask for pizza size
size = input("Choose size (s/m/l): ").lower()
add_pepperoni = input("Do you want pepperoni? (y/n): ").lower()
extra_cheese = input("Do you want extra cheese? (y/n): ").lower()
home_delivery = input("Do you want home delivery? (y/n): ").lower()

# Base price
bill = 0

# Set base price based on size
if size == 's':
    bill += 100
elif size == 'm':
    bill += 200
elif size == 'l':
    bill += 300
else:
    print("Invalid size selected!")

# Add pepperoni cost
if add_pepperoni == 'y':
    if size == 's':
        bill += 30
    else:
        bill += 50

# Add cheese cost
if extra_cheese == 'y':
    bill += 20

# Add home delivery cost
if home_delivery == 'y':
    bill += 40

# Final Bill
print(f"Your total bill is ₹{bill}")
