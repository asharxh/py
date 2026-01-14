def advanced_food_order_billing_system():
    menu = {
        "Starters": {
            1: {"name": "French Fries", "price": 70},
            2: {"name": "Paneer Tikka", "price": 120},
            3: {"name": "Garlic Bread", "price": 80}
        },
        "Main Course": {
            1: {"name": "Pizza", "price": 200},
            2: {"name": "Burger", "price": 50},
            3: {"name": "Pasta", "price": 150},
            4: {"name": "Sandwich", "price": 80}
        },
        "Drinks": {
            1: {"name": "Coke", "price": 30},
            2: {"name": "Pepsi", "price": 30},
            3: {"name": "Orange Juice", "price": 50}
        },
        "Desserts": {
            1: {"name": "Ice Cream", "price": 60},
            2: {"name": "Brownie", "price": 80}
        }
    }

    order = {}
    print("Welcome to the Advanced Food Order System!")

    while True:
        print("\nMenu Categories:")
        for category in menu:
            print(f"- {category}")

        category_choice = input("Select a category (or type 'done' to checkout, 'view' to see current order): ").strip().title()
        if category_choice == "Done":
            break
        elif category_choice == "View":
            if len(order) == 0:
                print("No items in order yet.")
            else:
                print("Current Order:")
                for item in order:
                    print(f"{item:20} x {order[item]}")
            continue
        elif category_choice not in menu:
            print("Invalid category. Try again.")
            continue

        print(f"\n{category_choice} Menu:")
        for number, item_info in menu[category_choice].items():
            print(f"{number}. {item_info['name']} - Rs {item_info['price']}")

        while True:
            item_number_input = input("Enter item number to order (or 'back' to choose another category): ")
            if item_number_input.lower() == "back":
                break
            if not item_number_input.isdigit():
                print("Invalid input. Enter a number.")
                continue
            item_number = int(item_number_input)
            if item_number not in menu[category_choice]:
                print("Item number not in menu. Try again.")
                continue

            item_name = menu[category_choice][item_number]["name"]
            item_price = menu[category_choice][item_number]["price"]

            while True:
                quantity_input = input(f"Enter quantity for {item_name}: ")
                if quantity_input.isdigit() and int(quantity_input) > 0:
                    quantity = int(quantity_input)
                    break
                else:
                    print("Invalid quantity. Enter a positive integer.")

            if item_name in order:
                order[item_name] += quantity
            else:
                order[item_name] = quantity

            print(f"Added {quantity} x {item_name} to your order.")
            break

    if len(order) == 0:
        print("No items ordered. Exiting.")
        return

    print("\n----------- FINAL BILL -----------")
    total = 0
    for item in order:
        price = 0
        for category in menu:
            for num in menu[category]:
                if menu[category][num]["name"] == item:
                    price = menu[category][num]["price"]
        item_total = price * order[item]
        print(f"{item:20} x {order[item]:2} = Rs {item_total}")
        total += item_total

    tax_rate = 0.05
    tax = total * tax_rate
    discount = 0
    if total > 500:
        discount = total * 0.1

    final_total = total + tax - discount

    print("----------------------------------")
    print(f"Subtotal       : Rs {total}")
    print(f"Tax (5%)       : Rs {tax}")
    if discount > 0:
        print(f"Discount (10%) : Rs {discount}")
    print(f"Total Amount   : Rs {final_total}")
    print("----------------------------------")
    print("Thank you for your order!")

advanced_food_order_billing_system()