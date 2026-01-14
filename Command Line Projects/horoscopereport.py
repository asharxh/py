import os
import random

ZODIAC_SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

def load_horoscopes(filename="horoscopes.txt"):
    horoscopes = {sign: [] for sign in ZODIAC_SIGNS}
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 2:
                    sign, message = parts
                    if sign in horoscopes:
                        horoscopes[sign].append(message)
    return horoscopes

def save_horoscopes(horoscopes, filename="horoscopes.txt"):
    with open(filename, "w") as f:
        for sign, messages in horoscopes.items():
            for msg in messages:
                f.write(f"{sign}|{msg}\n")

def display_horoscope(sign, horoscopes):
    if not horoscopes[sign]:
        print(f"No horoscope messages available for {sign}.")
    else:
        message = random.choice(horoscopes[sign])
        print(f"\nHoroscope for {sign}:\n{message}")

def horoscope_message_system():
    horoscopes = load_horoscopes()

    while True:
        print("\n--- Horoscope Message System ---")
        print("1. View Horoscope")
        print("2. Add/Update Horoscope Message")
        print("3. View All Horoscopes for a Sign")
        print("4. Search Horoscope Messages")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Select your Zodiac Sign:")
            for idx, sign in enumerate(ZODIAC_SIGNS, start=1):
                print(f"{idx}. {sign}")
            sign_choice = input("Enter number: ")
            if sign_choice.isdigit() and 1 <= int(sign_choice) <= 12:
                display_horoscope(ZODIAC_SIGNS[int(sign_choice)-1], horoscopes)
            else:
                print("Invalid choice.")

        elif choice == "2":
            sign_input = input("Enter zodiac sign to add/update: ").capitalize()
            if sign_input not in ZODIAC_SIGNS:
                print("Invalid zodiac sign.")
                continue
            message = input("Enter horoscope message: ").strip()
            if message:
                horoscopes[sign_input].append(message)
                save_horoscopes(horoscopes)
                print(f"Message added for {sign_input}.")
            else:
                print("Message cannot be empty.")

        elif choice == "3":
            sign_input = input("Enter zodiac sign to view all messages: ").capitalize()
            if sign_input not in ZODIAC_SIGNS:
                print("Invalid zodiac sign.")
                continue
            if not horoscopes[sign_input]:
                print(f"No messages for {sign_input}.")
            else:
                print(f"\nAll Horoscope Messages for {sign_input}:")
                for idx, msg in enumerate(horoscopes[sign_input], start=1):
                    print(f"{idx}. {msg}")

        elif choice == "4":
            keyword = input("Enter keyword to search in horoscope messages: ").lower()
            found = False
            for sign, messages in horoscopes.items():
                for msg in messages:
                    if keyword in msg.lower():
                        print(f"{sign}: {msg}")
                        found = True
            if not found:
                print("No matching messages found.")

        elif choice == "5":
            print("Exiting Horoscope Message System.")
            break

        else:
            print("Invalid choice. Please select again.")

horoscope_message_system()