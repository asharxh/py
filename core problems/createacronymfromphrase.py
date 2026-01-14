def create_acronym():
    phrase = input("Enter a phrase: ")
    words = phrase.split()
    acronym = ""
    index = 0
    while index < len(words):
        word = words[index]
        if len(word) > 0:
            first_letter = word[0].upper()
            acronym = acronym + first_letter
        index = index + 1
    print("Acronym is:", acronym)

create_acronym()