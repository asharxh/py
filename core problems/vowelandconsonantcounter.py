text = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_counter = 0
consonant_counter = 0


for char in text:
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        if char in vowels:
            vowel_counter += 1
            
        else:
            consonant_counter += 1
            
print(f"Vowels : {vowel_counter}")
print(f"Consonants : {consonant_counter}")