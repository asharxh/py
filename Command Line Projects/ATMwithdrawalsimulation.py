def fully_upgraded_atm():
    atm_notes = {2000: 10, 500: 20, 200: 30, 100: 50}
    users = {
        "user1": {"pin": "1234", "balance": 5000, "transactions": []},
        "user2": {"pin": "4321", "balance": 10000, "transactions": []}
    }

    print("Welcome to the Fully Upgraded ATM System!")

    while True:
        print("\nMain Menu:")
        print("1. Login")
        print("2. Create New User")
        print("3. Exit")
        main_choice = input("Enter your choice: ")

        if main_choice == "3":
            print("Thank you for using the ATM. Goodbye!")
            break

        elif main_choice == "2":
            new_username = input("Enter new username: ")
            if new_username in users:
                print("Username already exists. Try a different one.")
                continue
            new_pin = input("Set a 4-digit PIN: ")
            if len(new_pin) != 4 or not new_pin.isdigit():
                print("PIN must be 4 digits.")
                continue
            initial_deposit_input = input("Enter initial deposit: ")
            if not initial_deposit_input.isdigit() or int(initial_deposit_input) < 0:
                print("Invalid deposit amount.")
                continue
            initial_deposit = int(initial_deposit_input)
            users[new_username] = {"pin": new_pin, "balance": initial_deposit, "transactions": [f"Initial Deposit: Rs {initial_deposit}"]}
            print(f"User {new_username} created successfully.")

        elif main_choice == "1":
            username = input("Enter your username: ")
            if username not in users:
                print("Username not found.")
                continue

            attempts = 0
            while attempts < 3:
                pin = input("Enter your PIN: ")
                if pin == users[username]["pin"]:
                    print("Login successful!")
                    break
                else:
                    attempts += 1
                    print(f"Incorrect PIN. Attempts left: {3 - attempts}")
            else:
                print("Too many incorrect PIN attempts. Returning to main menu.")
                continue

            while True:
                print(f"\nATM Options for {username}:")
                print("1. Balance Inquiry")
                print("2. Withdraw Cash")
                print("3. Deposit Cash")
                print("4. Transfer to Another User")
                print("5. Mini Statement (Last 5)")
                print("6. Full Transaction History")
                print("7. Logout")
                choice = input("Select an option: ")

                if choice == "1":
                    print(f"Current Balance: Rs {users[username]['balance']}")

                elif choice == "2":
                    amount_input = input("Enter amount to withdraw: ")
                    if not amount_input.isdigit() or int(amount_input) <= 0:
                        print("Invalid amount.")
                        continue
                    amount = int(amount_input)
                    if amount > users[username]["balance"]:
                        print("Insufficient funds in your account.")
                        continue
                    total_atm_cash = sum(note * count for note, count in atm_notes.items())
                    if amount > total_atm_cash:
                        print("ATM has insufficient cash.")
                        continue

                    remaining = amount
                    notes_to_dispense = {}
                    for note in sorted(atm_notes.keys(), reverse=True):
                        max_needed = remaining // note
                        if max_needed > 0:
                            notes_available = atm_notes[note]
                            notes_used = min(max_needed, notes_available)
                            if notes_used > 0:
                                notes_to_dispense[note] = notes_used
                                remaining -= notes_used * note

                    if remaining == 0:
                        print(f"Dispensing Rs {amount}:")
                        for note, count in notes_to_dispense.items():
                            print(f"Rs {note} x {count}")
                            atm_notes[note] -= count
                        users[username]["balance"] -= amount
                        users[username]["transactions"].append(f"Withdraw: Rs {amount}")
                    else:
                        print("Cannot dispense the exact amount with available notes.")

                elif choice == "3":
                    deposit_input = input("Enter amount to deposit: ")
                    if not deposit_input.isdigit() or int(deposit_input) <= 0:
                        print("Invalid deposit amount.")
                        continue
                    deposit = int(deposit_input)
                    users[username]["balance"] += deposit
                    users[username]["transactions"].append(f"Deposit: Rs {deposit}")
                    print(f"Rs {deposit} deposited successfully.")

                elif choice == "4":
                    target_user = input("Enter recipient username: ")
                    if target_user not in users:
                        print("Recipient not found.")
                        continue
                    transfer_input = input("Enter amount to transfer: ")
                    if not transfer_input.isdigit() or int(transfer_input) <= 0:
                        print("Invalid amount.")
                        continue
                    transfer_amount = int(transfer_input)
                    if transfer_amount > users[username]["balance"]:
                        print("Insufficient funds for transfer.")
                        continue
                    users[username]["balance"] -= transfer_amount
                    users[target_user]["balance"] += transfer_amount
                    users[username]["transactions"].append(f"Transfer to {target_user}: Rs {transfer_amount}")
                    users[target_user]["transactions"].append(f"Received from {username}: Rs {transfer_amount}")
                    print(f"Transferred Rs {transfer_amount} to {target_user} successfully.")

                elif choice == "5":
                    print("Mini Statement (Last 5 Transactions):")
                    transactions = users[username]["transactions"][-5:]
                    if not transactions:
                        print("No transactions yet.")
                    else:
                        for t in transactions:
                            print(t)
                    print(f"Current Balance: Rs {users[username]['balance']}")

                elif choice == "6":
                    print("Full Transaction History:")
                    transactions = users[username]["transactions"]
                    if not transactions:
                        print("No transactions yet.")
                    else:
                        for t in transactions:
                            print(t)
                    print(f"Current Balance: Rs {users[username]['balance']}")

                elif choice == "7":
                    print(f"Logging out {username}...")
                    break

                else:
                    print("Invalid option. Try again.")
        else:
            print("Invalid choice. Try again.")

fully_upgraded_atm()