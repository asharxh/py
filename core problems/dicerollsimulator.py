print("DICE ROLL SIMULATOR")
print("Note: You will enter the dice face manually (1–6).")

while True:
    user_input = input("Enter a number between 1 and 6 (or 'q' to quit): ")

    if user_input.lower() == 'q':
        print("Exiting Dice Simulator. Goodbye!")
        break

    if not user_input.isdigit():
        print("Invalid input! Please enter a number.")
        continue

    dice_face = int(user_input)

    if 1 <= dice_face <= 6:
        print(f"You rolled a {dice_face}!")
        
        dice_faces = {
            1: ["-----", "|   |", "| o |", "|   |", "-----"],
            2: ["-----", "|o  |", "|   |", "|  o|", "-----"],
            3: ["-----", "|o  |", "| o |", "|  o|", "-----"],
            4: ["-----", "|o o|", "|   |", "|o o|", "-----"],
            5: ["-----", "|o o|", "| o |", "|o o|", "-----"],
            6: ["-----", "|o o|", "|o o|", "|o o|", "-----"]
        }
        for line in dice_faces[dice_face]:
            print(line)

    else:
        print("Invalid number! Please enter between 1 and 6.")