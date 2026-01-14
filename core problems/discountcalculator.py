print("DISCOUNT CALCULATOR")

price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter discount percentage (0–100): "))

if 0 <= discount_percent <= 100:
    
    discount_amount = (price * discount_percent) / 100
    final_price = price - discount_amount

    print("\n--- Calculation Result ---")
    print(f"Original Price: {price:.2f}")
    print(f"Discount: {discount_percent}% → {discount_amount:.2f}")
    print(f"Final Price after Discount:  {final_price:.2f}")

    if discount_percent > 50:
        print("Huge discount!!")
else:
    print("Invalid discount percentage! Must be between 0 and 100.")