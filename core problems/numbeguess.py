import random

secret = random.randint(1, 100)

attemp = 0

print("Im thinking of a Number b/w 1 to 100...Can u guess")

while True:
    guess = int(input("Enter your Guess"))
    attemp += 1
    
    if guess < secret:
        print("Too Low")
    elif guess > secret:
        print("To high")
    else:
        print(f"Correct! You guessed it in {attemp} attemps")
        break