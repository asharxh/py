sentence = input("Enter a sentence: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")
if old_word == "":
    new_sentence = sentence
else:
    i = 0
    n = len(sentence)
    m = len(old_word)
    parts = []
    while i < n:
        if i + m <= n and sentence[i:i+m] == old_word:
            parts.append(new_word)
            i += m
        else:
            parts.append(sentence[i])
            i += 1
    new_sentence = "".join(parts)
print("Updated sentence:", new_sentence)