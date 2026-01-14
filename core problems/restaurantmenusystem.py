print("=== Welcome to Python Restaurant ===\n")

menu = {
    "Pizza": 8.99,
    "Burger": 5.99,
    "Pasta": 7.49,
    "Salad": 4.99,
    "Fries": 2.99,
    "Soda": 1.49
}

print("----- MENU -----")
for item, price in menu.items():
    print(f"{item:10s} : ${price:.2f}")

order = {}
while True:
    item = input("\nEnter the item you want to order (or 'done' to finish): ").title()
    
    if item.lower() == "done":
        break
    
    if item not in menu:
        print("Sorry, that item is not on the menu.")
        continue
    
    quantity = input(f"Enter quantity for {item}: ")
    if not quantity.isdigit():
        print("Please enter a valid number.")
        continue
    
    order[item] = order.get(item, 0) + int(quantity)

total = 0
print("\n===== BILL =====")
for item, qty in order.items():
    price = menu[item] * qty
    total += price
    print(f"{item:10s} x{qty:<2} = ${price:.2f}")

print(f"Total Amount: ${total:.2f}")

tax = total * 0.07  # 7% tax
final_total = total + tax
print(f"Tax (7%): ${tax:.2f}")
print(f"Final Total: ${final_total:.2f}")

print("\nThank you for dining with us!")