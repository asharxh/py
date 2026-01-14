sentence = input("Enter a sentence: ")

words = sentence.split()

capitalized_words = []
for word in words:
    if len(word) > 0:
        capitalized_word = word[0].upper() + word[1:]
        capitalized_words.append(capitalized_word)
    else:
        capitalized_words.append(word)

capitalized_sentence = " ".join(capitalized_words)


print("Capitalized sentence:", capitalized_sentence)
