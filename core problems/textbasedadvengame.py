def intro():
    print("Welcome to the advanture game: ")
    print("You wake up in a mystrious forest. You must find your way out. ")
    print("Your choice will determine your fate..\n")
    
def forest():
    print("You are in a dark forest. Youu see a path leading north and a cave to the east. ")
    choice = input("Do you go NORTH OR EAST? ").lower()
    
    if choice == "north":
        village()
    elif choice == "east":
        cave()
    else:
        print("Invalid choice")
        forest()
        
def cave():
    print("You enter into cave... Its dark and you hear a growl.")
    choice = input("Do you fight the monster or RUN? ").lower()
    
    if choice == "fight":
        print("Monster was too strong. You were Defeated! ")
        game_over()
    elif choice == "run":
        print("Good Choice Escape back to forest! ")
        forest()
    else:
        print("invalid input! Try again ")
        cave()
        
def village():
    print("You enter into village , Villagers Welcome you.")
    choice = input("Do you wanna stay or Continue north! ")
    if choice == "stay":
        print("You found safety! You Win ")
        play_again()
    elif choice == "continue":
        castle()
    else:
        print("Invalid input!! ")
        village()
    
def castle():
    print("You arrive at an abandoned Castle. A Treasure chest Found. ")
    choice = input("Wanna open chest or leave: ")
    if choice == "open":
        print("You found treasure. you Win! ")
    elif choice == "leave":
        print("You walk away")
        play_again()
    else: 
        print("Invalid input! ")
        castle()
            
def game_over():
    print("Game over! ")
    play_again()
        
def play_again():
    choice = input("Do you wanna play again (Yes/No): ").lower()
    if choice == "yes":
        intro()
        forest()
    else:
        print("Thanks for Playing! ")
            
def main():
    intro()
    forest()
        
if __name__ == "__main__":
    main()
