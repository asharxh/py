def shopping_cart():
    products = {
    "apple" : 1.5,
    "banana" : 0.8,
    "milk" : 2.0,
    "bread" : 2.5,
    "eggs" : 3.0
    }

    cart = {}
    
    print("Welcome to shopping cart System! ")
    print("Available Products: ")
    for item, price in products.items():
        print(f" - {item.title()} : ${price:.2f}")
    print("\n")    
        
    while True:
        print("Options [add] [remove] [view] [checkout]")
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == "add":
            item = input("Enter product name to add: ").strip().lower()
            if item in products:
                quantity = int(input("Enter quantity: "))
                cart[item] = cart.get(item, 0) + quantity
                print(f"Add {quantity} {item}(s) to cart.")
            else: 
                print("Product not found")
                
        elif choice == "remove":
            item = input("Enter product name to remove: ").strip().lower()
            if item in cart:
                quantity = int(input("Enter quantity to remove: "))
                if quantity >= cart[item]:
                    del cart[item] 
                    print(f"Removed all {item} from cart")
                else:
                    cart[item] -= quantity
                    print(f"Removed {quantity} {item} from cart. ")
            else:
                print("Item not in Cart")
                
        elif choice == "view":
            if not cart:
                print("Your cart is empty. ")
            else:
                print("Your Cart. ")
                total = 0
                for item, qty in cart.items():
                    price = products[item] * qty
                    total += price
                    print(f" - {item.title()} x{qty} =${price:.2f}")
                print(f"Total: ${total:.2f}")
                
        elif choice == "checkout":
            if not cart:
                print("Cart is Empty. ")
            else:
                print("Check summary: ")
                total = 0
                for item, qty in cart.items():
                    price = products[item] * qty
                    total += price
                    print(f"- {item.title()}x {qty} = ${price:.2f}")
                print(f"final total price: ${total:.2f}")
            print("Thank you for shopping with Us")
            break
        else:
            print("Please Enter Valid Choice! Choose again. ")
                             
if __name__ == "__main__":
    shopping_cart()