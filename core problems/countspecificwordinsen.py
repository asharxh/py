
sentence = input("Enter a sentence: ")
word_to_count = input("Enter the word to count: ")

sentence_lower = sentence.lower()
word_lower = word_to_count.lower()

words = sentence_lower.split()

count = 0

for w in words:
    if w == word_lower:
        count += 1 

print(f"The word '{word_to_count}' appears {count} time(s) in the sentence.")