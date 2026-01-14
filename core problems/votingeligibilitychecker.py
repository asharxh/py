def votingeli():
    print("HELLO WELCOME TO VOTING ELIGIBILITY CHECKER")
    age = int(input("Please enter ur Age:  "))
    
    if age >= 18:
        print("Congratulation You can Vote")
    else:
        print("You cant vote, Sorry: ")


votingeli()
