import os

# Function to clear screen (for secrecy)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to find highest bidder
def find_highest_bidder(auction_data):
    highest = 0
    winner = {}
    for person, details in auction_data.items():
        if details['bid'] > highest:
            highest = details['bid']
            winner = {person: details}
    return winner

# Dictionary to store all bidders
auction_data = {}

print("🎉 Welcome to the Secret Auction 🎉")

while True:
    name = input("Enter your name: ").strip()
    try:
        bid = int(input("Enter your bid amount (in ₹): ").strip())
    except ValueError:
        print("❌ Invalid bid! Please enter a number.")
        continue

    address = input("Enter your address: ").strip()
    email = input("Enter your email: ").strip()
    phone = input("Enter your phone number: ").strip()

    # Store in dictionary
    auction_data[name] = {
        "bid": bid,
        "address": address,
        "email": email,
        "phone": phone
    }

    more = input("Are there any other bidders? (yes/no): ").lower()
    if more != 'yes':
        break
    clear()

# Reveal winner
winner = find_highest_bidder(auction_data)
for name, details in winner.items():
    print("\n🎉 THE WINNER IS:", name.upper())
    print(f"🏆 Bid: ₹{details['bid']}")
    print(f"🏡 Address: {details['address']}")
    print(f"📧 Email: {details['email']}")
    print(f"📱 Phone: {details['phone']}")
    print("===================================")

# Optionally export data
save = input("\nDo you want to save the auction data to a file? (y/n): ").lower()
if save == 'y':
    with open("auction_results.txt", "w") as file:
        for bidder, info in auction_data.items():
            file.write(f"Name: {bidder}\n")
            file.write(f"Bid: ₹{info['bid']}\n")
            file.write(f"Address: {info['address']}\n")
            file.write(f"Email: {info['email']}\n")
            file.write(f"Phone: {info['phone']}\n")
            file.write("-" * 30 + "\n")
    print("✅ Data saved to 'auction_results.txt'")
