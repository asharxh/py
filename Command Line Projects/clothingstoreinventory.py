import os

def load_inventory(filename="inventory.txt"):
    inventory = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 5:
                    product_id, name, category, price, quantity = parts
                    inventory.append({
                        "id": product_id,
                        "name": name,
                        "category": category,
                        "price": float(price),
                        "quantity": int(quantity)
                    })
    return inventory

def save_inventory(inventory, filename="inventory.txt"):
    with open(filename, "w") as f:
        for product in inventory:
            f.write(f"{product['id']}|{product['name']}|{product['category']}|{product['price']}|{product['quantity']}\n")

def display_product(product):
    print(f"ID: {product['id']} | Name: {product['name']} | Category: {product['category']} | Price: Rs {product['price']} | Quantity: {product['quantity']}")

def clothing_store_inventory():
    inventory = load_inventory()

    while True:
        print("\n--- Clothing Store Inventory ---")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Inventory")
        print("4. Search Product")
        print("5. Update Stock/Price")
        print("6. Sort Inventory")
        print("7. View Low-Stock Items")
        print("8. View Total Inventory Value")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            product_id = input("Enter product ID: ")
            if any(p['id'] == product_id for p in inventory):
                print("Product ID already exists.")
                continue
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            price_input = input("Enter product price: ")
            quantity_input = input("Enter product quantity: ")
            if not price_input.replace('.','',1).isdigit() or not quantity_input.isdigit():
                print("Invalid price or quantity.")
                continue
            price = float(price_input)
            quantity = int(quantity_input)
            inventory.append({"id": product_id, "name": name, "category": category, "price": price, "quantity": quantity})
            save_inventory(inventory)
            print(f"Product '{name}' added successfully.")

        elif choice == "2":
            pid = input("Enter product ID to remove: ")
            for product in inventory:
                if product['id'] == pid:
                    inventory.remove(product)
                    save_inventory(inventory)
                    print(f"Product '{product['name']}' removed successfully.")
                    break
            else:
                print("Product ID not found.")

        elif choice == "3":
            if len(inventory) == 0:
                print("Inventory is empty.")
            else:
                print("Current Inventory:")
                for product in inventory:
                    display_product(product)

        elif choice == "4":
            keyword = input("Enter product name, category, or ID to search: ").lower()
            found = False
            for product in inventory:
                if keyword in product['name'].lower() or keyword in product['category'].lower() or keyword == product['id'].lower():
                    display_product(product)
                    found = True
            if not found:
                print("No matching products found.")

        elif choice == "5":
            pid = input("Enter product ID to update: ")
            for product in inventory:
                if product['id'] == pid:
                    price_input = input(f"Enter new price for '{product['name']}' (current: Rs {product['price']}): ")
                    quantity_input = input(f"Enter new quantity for '{product['name']}' (current: {product['quantity']}): ")
                    if price_input:
                        if not price_input.replace('.','',1).isdigit():
                            print("Invalid price.")
                            break
                        product['price'] = float(price_input)
                    if quantity_input:
                        if not quantity_input.isdigit():
                            print("Invalid quantity.")
                            break
                        product['quantity'] = int(quantity_input)
                    save_inventory(inventory)
                    print(f"Product '{product['name']}' updated successfully.")
                    break
            else:
                print("Product ID not found.")

        elif choice == "6":
            print("Sort by: 1. Name 2. Category 3. Price 4. Quantity")
            sort_choice = input("Enter choice: ")
            if sort_choice == "1":
                inventory.sort(key=lambda x: x['name'].lower())
            elif sort_choice == "2":
                inventory.sort(key=lambda x: x['category'].lower())
            elif sort_choice == "3":
                inventory.sort(key=lambda x: x['price'])
            elif sort_choice == "4":
                inventory.sort(key=lambda x: x['quantity'])
            else:
                print("Invalid choice.")
                continue
            save_inventory(inventory)
            print("Inventory sorted successfully.")

        elif choice == "7":
            low_stock = [p for p in inventory if p['quantity'] < 5]
            if not low_stock:
                print("No low-stock items.")
            else:
                print("Low-Stock Items:")
                for product in low_stock:
                    display_product(product)

        elif choice == "8":
            total_value = sum(p['price'] * p['quantity'] for p in inventory)
            print(f"Total inventory value: Rs {total_value}")

        elif choice == "9":
            print("Exiting Clothing Store Inventory.")
            break

        else:
            print("Invalid choice. Please select again.")

clothing_store_inventory()