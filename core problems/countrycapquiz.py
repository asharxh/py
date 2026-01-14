def country_capital_quiz():
    countries = {
        "India": "New Delhi",
        "France": "Paris",
        "Japan": "Tokyo",
        "Australia": "Canberra",
        "Canada": "Ottawa"
    }
    score = 0
    total = len(countries)
    for country in countries:
        answer = input("What is the capital of " + country + "? ")
        if answer.strip().lower() == countries[country].lower():
            print("Correct!")
            score = score + 1
        else:
            print("Wrong! The correct answer is:", countries[country])
    print("Your final score is", score, "out of", total)

country_capital_quiz()