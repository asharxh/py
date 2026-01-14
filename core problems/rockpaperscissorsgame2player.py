print("Rock-Paper-Scissors Game")
print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.\n")

choices = ["rock", "paper", "scissors"]

while True:
    player1 = input("Player 1, enter Rock, Paper, or Scissors: ").lower().strip()
    player2 = input("Player 2, enter Rock, Paper, or Scissors: ").lower().strip()

    if player1 not in choices or player2 not in choices:
        print(" Invalid input. Please enter Rock, Paper, or Scissors.\n")
        continue

    if player1 == player2:
        print(" It's a tie!")
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):
        print(" Player 1 wins!")
    else:
        print(" Player 2 wins!")

    again = input("\nDo you want to play again? (yes/no): ").lower().strip()
    if again != "yes":
        print(" Thanks for playing!")
        break